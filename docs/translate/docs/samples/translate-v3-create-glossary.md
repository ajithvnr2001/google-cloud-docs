---
url: https://docs.cloud.google.com/translate/docs/samples/translate-v3-create-glossary/
title: Create a glossary (Advanced edition only) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:34.371913+00:00
---

# Create a glossary (Advanced edition only)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/samples/translate-v3-create-glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Samples ](https://docs.cloud.google.com/translate/docs/samples)



#  Create a glossary (Advanced edition only) Stay organized with collections  Save and categorize content based on your preferences. 

Create a glossary.

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
    
    // createGlossary creates a glossary to use for other operations.
    func createGlossary(w io.Writer, projectID string, location string, glossaryID string, glossaryInputURI string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// glossaryID := "my-glossary-display-name"
    	// glossaryInputURI := "gs://cloud-samples-data/translation/glossary.csv"
    
    	ctx := context.Background()
    	client, err := translate.[NewTranslationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)()
    
    	req := &translatepb.CreateGlossaryRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		Glossary: &translatepb.Glossary{
    			Name: fmt.Sprintf("projects/%s/locations/%s/glossaries/%s", projectID, location, glossaryID),
    			Languages: &translatepb.Glossary_LanguageCodesSet_{
    				LanguageCodesSet: &translatepb.Glossary_LanguageCodesSet{
    					LanguageCodes: []string{"en", "ja"},
    				},
    			},
    			InputConfig: &translatepb.GlossaryInputConfig{
    				Source: &translatepb.GlossaryInputConfig_GcsSource{
    					GcsSource: &translatepb.GcsSource{
    						InputUri: glossaryInputURI,
    					},
    				},
    			},
    		},
    	}
    
    	// The CreateGlossary operation is async.
    	op, err := client.CreateGlossary(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateGlossary: %w", err)
    	}
    	fmt.Fprintf(w, "Processing operation name: %q\n", op.Name())
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created: %v\n", resp.GetName())
    	fmt.Fprintf(w, "Input URI: %v\n", resp.InputConfig.GetGcsSource().GetInputUri())
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.translate.v3.[CreateGlossaryMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateGlossaryMetadata.html);
    import com.google.cloud.translate.v3.[CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateGlossaryRequest.html);
    import com.google.cloud.translate.v3.[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html);
    import com.google.cloud.translate.v3.[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html);
    import com.google.cloud.translate.v3.[GlossaryInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryInputConfig.html);
    import com.google.cloud.translate.v3.[GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    
    public class CreateGlossary {
    
      public static void createGlossary() throws InterruptedException, ExecutionException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        String glossaryId = "your-glossary-display-name";
        List<String> languageCodes = new ArrayList<>();
        languageCodes.add("your-language-code");
        String inputUri = "gs://your-gcs-bucket/path/to/input/file.txt";
        createGlossary(projectId, glossaryId, languageCodes, inputUri);
      }
    
      // Create a equivalent term sets glossary
      // https://cloud.google.com/translate/docs/advanced/glossary#format-glossary
      public static void createGlossary(
          String projectId, String glossaryId, List<String> languageCodes, String inputUri)
          throws IOException, ExecutionException, InterruptedException {
    
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
    
          // Supported Languages: https://cloud.google.com/translate/docs/languages
          [Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html).[LanguageCodesSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.LanguageCodesSet.html) languageCodesSet =
              [Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html).LanguageCodesSet.newBuilder().[addAllLanguageCodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.LanguageCodesSet.Builder.html#com_google_cloud_translate_v3_Glossary_LanguageCodesSet_Builder_addAllLanguageCodes_java_lang_Iterable_java_lang_String__)(languageCodes).build();
    
          // Configure the source of the file from a GCS bucket
          [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html) gcsSource = [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html).newBuilder().setInputUri(inputUri).build();
          [GlossaryInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryInputConfig.html) inputConfig =
              [GlossaryInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryInputConfig.html).newBuilder().setGcsSource(gcsSource).build();
    
          [Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html) glossary =
              [Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html).newBuilder()
                  .setName(glossaryName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html#com_google_cloud_translate_v3_GlossaryName_toString__)())
                  .[setLanguageCodesSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.Builder.html#com_google_cloud_translate_v3_Glossary_Builder_setLanguageCodesSet_com_google_cloud_translate_v3_Glossary_LanguageCodesSet_)(languageCodesSet)
                  .setInputConfig(inputConfig)
                  .build();
    
          [CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateGlossaryRequest.html) request =
              [CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateGlossaryRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)())
                  .setGlossary(glossary)
                  .build();
    
          // Start an asynchronous request
          OperationFuture<Glossary, CreateGlossaryMetadata> future =
              client.[createGlossaryAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html#com_google_cloud_translate_v3_TranslationServiceClient_createGlossaryAsync__org_jspecify_annotations_Nullable_com_google_cloud_translate_v3_LocationName_com_google_cloud_translate_v3_Glossary_)(request);
    
          System.out.println("Waiting for operation to complete...");
          [Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html) response = future.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
          System.out.println("Created Glossary.");
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
    // const glossaryId = 'your-glossary-display-name';
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)');
    
    // Instantiates a client
    const translationClient = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    
    async function createGlossary() {
      // Construct glossary
      const glossary = {
        languageCodesSet: {
          languageCodes: ['en', 'es'],
        },
        inputConfig: {
          gcsSource: {
            inputUri: 'gs://cloud-samples-data/translation/glossary.csv',
          },
        },
        name: `projects/${projectId}/locations/${location}/glossaries/${glossaryId}`,
      };
    
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        glossary: glossary,
      };
    
      // Create glossary using a long-running operation
      const [operation] = await translationClient.createGlossary(request);
    
      // Wait for the operation to complete
      await operation.promise();
    
      console.log('Created glossary:');
      console.log(`InputUri ${[request](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.translate.html).glossary.inputConfig.gcsSource.inputUri}`);
    }
    
    createGlossary();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/translate/v2/translateclient). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Translate\V3\Client\TranslationServiceClient;
    use Google\Cloud\Translate\V3\CreateGlossaryRequest;
    use Google\Cloud\Translate\V3\GcsSource;
    use Google\Cloud\Translate\V3\Glossary;
    use Google\Cloud\Translate\V3\Glossary\LanguageCodesSet;
    use Google\Cloud\Translate\V3\GlossaryInputConfig;
    
    /**
     * @param string $projectId     Your Google Cloud project ID.
     * @param string $glossaryId    Your glossary ID.
     * @param string $inputUri      Path to to source input (e.g. "gs://cloud-samples-data/translation/glossary.csv").
     */
    function v3_create_glossary(
        string $projectId,
        string $glossaryId,
        string $inputUri
    ): void {
        $translationServiceClient = new TranslationServiceClient();
    
        $formattedParent = $translationServiceClient->locationName(
            $projectId,
            'us-central1'
        );
        $formattedName = $translationServiceClient->glossaryName(
            $projectId,
            'us-central1',
            $glossaryId
        );
        $languageCodesElement = 'en';
        $languageCodesElement2 = 'ja';
        $languageCodes = [$languageCodesElement, $languageCodesElement2];
        $languageCodesSet = new LanguageCodesSet();
        $languageCodesSet->setLanguageCodes($languageCodes);
        $gcsSource = (new GcsSource())
            ->setInputUri($inputUri);
        $inputConfig = (new GlossaryInputConfig())
            ->setGcsSource($gcsSource);
        $glossary = (new Glossary())
            ->setName($formattedName)
            ->setLanguageCodesSet($languageCodesSet)
            ->setInputConfig($inputConfig);
    
        try {
            $request = (new CreateGlossaryRequest())
                ->setParent($formattedParent)
                ->setGlossary($glossary);
            $operationResponse = $translationServiceClient->createGlossary($request);
            $operationResponse->pollUntilComplete();
            if ($operationResponse->operationSucceeded()) {
                $response = $operationResponse->getResult();
                printf('Created Glossary.' . PHP_EOL);
                printf('Glossary name: %s' . PHP_EOL, $response->getName());
                printf('Entry count: %s' . PHP_EOL, $response->getEntryCount());
                printf(
                    'Input URI: %s' . PHP_EOL,
                    $response->getInputConfig()
                        ->getGcsSource()
                        ->getInputUri()
                );
            } else {
                $error = $operationResponse->getError();
                // handleError($error)
            }
        } finally {
            $translationServiceClient->close();
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import translate_v3 as translate
    
    
    def create_glossary(
        project_id: str = "YOUR_PROJECT_ID",
        input_uri: str = "YOUR_INPUT_URI",
        glossary_id: str = "YOUR_GLOSSARY_ID",
        timeout: int = 180,
    ) -> translate.Glossary:
        """
        Create a equivalent term sets glossary. Glossary can be words or
        short phrases (usually fewer than five words).
        https://cloud.google.com/translate/docs/advanced/glossary#format-glossary
        """
        client = translate.TranslationServiceClient()
    
        # Supported language codes: https://cloud.google.com/translate/docs/languages
        source_lang_code = "en"
        target_lang_code = "ja"
        location = "us-central1"  # The location of the glossary
    
        name = client.glossary_path(project_id, location, glossary_id)
        language_codes_set = translate.types.Glossary.LanguageCodesSet(
            language_codes=[source_lang_code, target_lang_code]
        )
    
        gcs_source = translate.types.GcsSource(input_uri=input_uri)
    
        input_config = translate.types.GlossaryInputConfig(gcs_source=gcs_source)
    
        glossary = translate.types.Glossary(
            name=name, language_codes_set=language_codes_set, input_config=input_config
        )
    
        parent = f"projects/{project_id}/locations/{location}"
        # glossary is a custom dictionary Translation API uses
        # to translate the domain-specific terminology.
        operation = client.create_glossary(parent=parent, glossary=glossary)
    
        result = operation.result(timeout)
        print(f"Created: {result.name}")
        print(f"Input Uri: {result.input_config.gcs_source.input_uri}")
    
        return result
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtranslation). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
