---
url: https://docs.cloud.google.com/translate/docs/samples/translate-v3-get-glossary/
title: Get a glossary (Advanced edition only) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:28.205466+00:00
---

# Get a glossary (Advanced edition only)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/samples/translate-v3-get-glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Samples ](https://docs.cloud.google.com/translate/docs/samples)



#  Get a glossary (Advanced edition only) Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve a specified glossary.

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
    
    // getGlossary gets the specified glossary.
    func getGlossary(w io.Writer, projectID string, location string, glossaryID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// glossaryID := "glossary-id"
    
    	ctx := context.Background()
    	client, err := translate.[NewTranslationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)()
    
    	req := &translatepb.GetGlossaryRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/glossaries/%s", projectID, location, glossaryID),
    	}
    
    	resp, err := client.GetGlossary(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetGlossary: %w", err)
    	}
    
    	fmt.Fprintf(w, "Glossary name: %v\n", resp.GetName())
    	fmt.Fprintf(w, "Entry count: %v\n", resp.GetEntryCount())
    	fmt.Fprintf(w, "Input URI: %v\n", resp.GetInputConfig().GetGcsSource().GetInputUri())
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.translate.v3.[GetGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetGlossaryRequest.html);
    import com.google.cloud.translate.v3.[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html);
    import com.google.cloud.translate.v3.[GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    
    public class GetGlossary {
    
      public static void getGlossary() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        String glossaryId = "your-glossary-display-name";
        getGlossary(projectId, glossaryId);
      }
    
      // Get a particular glossary based on the glossary ID
      public static void getGlossary(String projectId, String glossaryId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model. (us-central1)
          [GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html) glossaryName = [GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html).of(projectId, "us-central1", glossaryId);
          [GetGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetGlossaryRequest.html) request =
              [GetGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetGlossaryRequest.html).newBuilder().setName(glossaryName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html#com_google_cloud_translate_v3_GlossaryName_toString__)()).build();
    
          [Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html) response = client.getGlossary(request);
    
          System.out.printf("Glossary name: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html#com_google_cloud_translate_v3_Glossary_getName__)());
          System.out.printf("Entry count: %s\n", response.[getEntryCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html#com_google_cloud_translate_v3_Glossary_getEntryCount__)());
          System.out.printf("Input URI: %s\n", response.[getInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html#com_google_cloud_translate_v3_Glossary_getInputConfig__)().getGcsSource().getInputUri());
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
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)');
    
    // Instantiates a client
    const translationClient = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    
    async function getGlossary() {
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        name: `projects/${projectId}/locations/${location}/glossaries/${glossaryId}`,
      };
    
      // Get glossary
      const [response] = await translationClient.getGlossary(request);
    
      console.log(`Glossary name: ${response.name}`);
      console.log(`Entry count: ${response.entryCount}`);
      console.log(`Input URI: ${response.inputConfig.gcsSource.inputUri}`);
    }
    
    getGlossary();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/translate/v2/translateclient). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Translate\V3\Client\TranslationServiceClient;
    use Google\Cloud\Translate\V3\GetGlossaryRequest;
    
    /**
     * @param string $projectId     Your Google Cloud project ID.
     * @param string $glossaryId    Your glossary ID.
     */
    function v3_get_glossary(string $projectId, string $glossaryId): void
    {
        $translationServiceClient = new TranslationServiceClient();
    
        $formattedName = $translationServiceClient->glossaryName(
            $projectId,
            'us-central1',
            $glossaryId
        );
    
        try {
            $request = (new GetGlossaryRequest())
                ->setName($formattedName);
            $response = $translationServiceClient->getGlossary($request);
            printf('Glossary name: %s' . PHP_EOL, $response->getName());
            printf('Entry count: %s' . PHP_EOL, $response->getEntryCount());
            printf(
                'Input URI: %s' . PHP_EOL,
                $response->getInputConfig()
                    ->getGcsSource()
                    ->getInputUri()
            );
        } finally {
            $translationServiceClient->close();
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import translate_v3 as translate
    
    
    def get_glossary(
        project_id: str = "YOUR_PROJECT_ID", glossary_id: str = "YOUR_GLOSSARY_ID"
    ) -> translate.Glossary:
        """Get a particular glossary based on the glossary ID.
    
        Args:
            project_id: The GCP project ID.
            glossary_id: The ID of the glossary to retrieve.
    
        Returns:
            The glossary.
        """
        client = translate.TranslationServiceClient()
    
        name = client.glossary_path(project_id, "us-central1", glossary_id)
    
        response = client.get_glossary(name=name)
        print(f"Glossary name: {response.name}")
        print(f"Entry count: {response.entry_count}")
        print(f"Input URI: {response.input_config.gcs_source.input_uri}")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtranslation). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
