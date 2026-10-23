---
url: https://docs.cloud.google.com/translate/docs/samples/translate-v3-batch-translate-text/
title: Translate text in batches (Advanced edition only) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:43.964508+00:00
---

# Translate text in batches (Advanced edition only)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/samples/translate-v3-batch-translate-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Samples ](https://docs.cloud.google.com/translate/docs/samples)



#  Translate text in batches (Advanced edition only) Stay organized with collections  Save and categorize content based on your preferences. 

Translate a large volume of text.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Batch requests (Advanced)](https://docs.cloud.google.com/translate/docs/advanced/batch-translation)



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
    
    // batchTranslateText translates a large volume of text in asynchronous batch mode.
    func batchTranslateText(w io.Writer, projectID string, location string, inputURI string, outputURI string, sourceLang string, targetLang string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// inputURI := "gs://cloud-samples-data/text.txt"
    	// outputURI := "gs://YOUR_BUCKET_ID/path_to_store_results/"
    	// sourceLang := "en"
    	// targetLang := "ja"
    
    	ctx := context.Background()
    	client, err := translate.[NewTranslationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)()
    
    	req := &translatepb.BatchTranslateTextRequest{
    		Parent:              fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		SourceLanguageCode:  sourceLang,
    		TargetLanguageCodes: []string{targetLang},
    		InputConfigs: []*translatepb.InputConfig{
    			{
    				Source: &translatepb.InputConfig_GcsSource{
    					GcsSource: &translatepb.GcsSource{InputUri: inputURI},
    				},
    				// Optional. Can be "text/plain" or "text/html".
    				MimeType: "text/plain",
    			},
    		},
    		OutputConfig: &translatepb.OutputConfig{
    			Destination: &translatepb.OutputConfig_GcsDestination{
    				GcsDestination: &translatepb.GcsDestination{
    					OutputUriPrefix: outputURI,
    				},
    			},
    		},
    	}
    
    	// The BatchTranslateText operation is async.
    	op, err := client.BatchTranslateText(ctx, req)
    	if err != nil {
    		return fmt.Errorf("BatchTranslateText: %w", err)
    	}
    	fmt.Fprintf(w, "Processing operation name: %q\n", op.Name())
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "Total characters: %v\n", resp.GetTotalCharacters())
    	fmt.Fprintf(w, "Translated characters: %v\n", resp.GetTranslatedCharacters())
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.translate.v3.[BatchTranslateMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateMetadata.html);
    import com.google.cloud.translate.v3.[BatchTranslateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateResponse.html);
    import com.google.cloud.translate.v3.[BatchTranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateTextRequest.html);
    import com.google.cloud.translate.v3.[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsDestination.html);
    import com.google.cloud.translate.v3.[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html);
    import com.google.cloud.translate.v3.[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.InputConfig.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
    import com.google.cloud.translate.v3.[OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.OutputConfig.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.ThreadLocalRandom;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class BatchTranslateText {
    
      public static void batchTranslateText()
          throws InterruptedException, ExecutionException, IOException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        // Supported Languages: https://cloud.google.com/translate/docs/languages
        String sourceLanguage = "your-source-language";
        String targetLanguage = "your-target-language";
        String inputUri = "gs://your-gcs-bucket/path/to/input/file.txt";
        String outputUri = "gs://your-gcs-bucket/path/to/results/";
        batchTranslateText(projectId, sourceLanguage, targetLanguage, inputUri, outputUri);
      }
    
      // Batch translate text
      public static void batchTranslateText(
          String projectId,
          String sourceLanguage,
          String targetLanguage,
          String inputUri,
          String outputUri)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create()) {
          // Supported Locations: `us-central1`
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html).of(projectId, "us-central1");
    
          [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html) gcsSource = [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html).newBuilder().setInputUri(inputUri).build();
          // Supported Mime Types: https://cloud.google.com/translate/docs/supported-formats
          [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.InputConfig.html) inputConfig =
              [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.InputConfig.html).newBuilder().setGcsSource(gcsSource).setMimeType("text/plain").build();
    
          [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsDestination.html) gcsDestination =
              [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsDestination.html).newBuilder().setOutputUriPrefix(outputUri).build();
          [OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.OutputConfig.html) outputConfig =
              [OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.OutputConfig.html).newBuilder().setGcsDestination(gcsDestination).build();
    
          [BatchTranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateTextRequest.html) request =
              [BatchTranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateTextRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)())
                  .setSourceLanguageCode(sourceLanguage)
                  .addTargetLanguageCodes(targetLanguage)
                  .addInputConfigs(inputConfig)
                  .setOutputConfig(outputConfig)
                  .build();
    
          OperationFuture<BatchTranslateResponse, BatchTranslateMetadata> future =
              client.[batchTranslateTextAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html#com_google_cloud_translate_v3_TranslationServiceClient_batchTranslateTextAsync_com_google_cloud_translate_v3_BatchTranslateTextRequest_)(request);
    
          System.out.println("Waiting for operation to complete...");
    
          // random number between 300 - 450 (maximum allowed seconds)
          long randomNumber = ThreadLocalRandom.current().nextInt(450, 600);
          [BatchTranslateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateResponse.html) response = future.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(randomNumber, TimeUnit.SECONDS);
    
          System.out.printf("Total Characters: %s\n", response.[getTotalCharacters](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateResponse.html#com_google_cloud_translate_v3_BatchTranslateResponse_getTotalCharacters__)());
          System.out.printf("Translated Characters: %s\n", response.[getTranslatedCharacters](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateResponse.html#com_google_cloud_translate_v3_BatchTranslateResponse_getTranslatedCharacters__)());
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
    // const location = 'us-central1';
    // const inputUri = 'gs://cloud-samples-data/text.txt';
    // const outputUri = 'gs://YOUR_BUCKET_ID/path_to_store_results/';
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)');
    
    // Instantiates a client
    const translationClient = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    async function batchTranslateText() {
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        sourceLanguageCode: 'en',
        targetLanguageCodes: ['ja'],
        inputConfigs: [
          {
            mimeType: 'text/plain', // mime types: text/plain, text/html
            gcsSource: {
              inputUri: inputUri,
            },
          },
        ],
        outputConfig: {
          gcsDestination: {
            outputUriPrefix: outputUri,
          },
        },
      };
    
      // Setup timeout for long-running operation. Timeout specified in ms.
      const options = {timeout: 240000};
      // Batch translate text using a long-running operation with a timeout of 240000ms.
      const [operation] = await translationClient.batchTranslateText(
        request,
        options
      );
    
      // Wait for operation to complete.
      const [response] = await operation.promise();
    
      console.log(`Total Characters: ${response.totalCharacters}`);
      console.log(`Translated Characters: ${response.translatedCharacters}`);
    }
    
    batchTranslateText();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/translate/v2/translateclient). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Translate\V3\BatchTranslateTextRequest;
    use Google\Cloud\Translate\V3\Client\TranslationServiceClient;
    use Google\Cloud\Translate\V3\GcsDestination;
    use Google\Cloud\Translate\V3\GcsSource;
    use Google\Cloud\Translate\V3\InputConfig;
    use Google\Cloud\Translate\V3\OutputConfig;
    
    /**
     * @param string $inputUri      Path to to source input (e.g. "gs://cloud-samples-data/text.txt").
     * @param string $outputUri     Path to store results (e.g. "gs://YOUR_BUCKET_ID/results/").
     * @param string $projectId     Your Google Cloud project ID.
     * @param string $location      Project location (e.g. us-central1)
     * @param string $targetLanguage    Language to translate to.
     * @param string $sourceLanguage    Language of the source.
     */
    function v3_batch_translate_text(
        string $inputUri,
        string $outputUri,
        string $projectId,
        string $location,
        string $targetLanguage,
        string $sourceLanguage
    ): void {
        $translationServiceClient = new TranslationServiceClient();
    
        $targetLanguageCodes = [$targetLanguage];
        $gcsSource = (new GcsSource())
            ->setInputUri($inputUri);
    
        // Optional. Can be "text/plain" or "text/html".
        $mimeType = 'text/plain';
        $inputConfigsElement = (new InputConfig())
            ->setGcsSource($gcsSource)
            ->setMimeType($mimeType);
        $inputConfigs = [$inputConfigsElement];
        $gcsDestination = (new GcsDestination())
            ->setOutputUriPrefix($outputUri);
        $outputConfig = (new OutputConfig())
            ->setGcsDestination($gcsDestination);
        $formattedParent = $translationServiceClient->locationName($projectId, $location);
    
        try {
            $request = (new BatchTranslateTextRequest())
                ->setParent($formattedParent)
                ->setSourceLanguageCode($sourceLanguage)
                ->setTargetLanguageCodes($targetLanguageCodes)
                ->setInputConfigs($inputConfigs)
                ->setOutputConfig($outputConfig);
            $operationResponse = $translationServiceClient->batchTranslateText($request);
            $operationResponse->pollUntilComplete();
            if ($operationResponse->operationSucceeded()) {
                $response = $operationResponse->getResult();
                printf('Total Characters: %s' . PHP_EOL, $response->getTotalCharacters());
                printf('Translated Characters: %s' . PHP_EOL, $response->getTranslatedCharacters());
            } else {
                $error = $operationResponse->getError();
                print($error->getMessage());
            }
        } finally {
            $translationServiceClient->close();
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)
    
    
    def batch_translate_text(
        input_uri: str = "gs://YOUR_BUCKET_ID/path/to/your/file.txt",
        output_uri: str = "gs://YOUR_BUCKET_ID/path/to/save/results/",
        project_id: str = "YOUR_PROJECT_ID",
        timeout: int = 180,
    ) -> translate.TranslateTextResponse:
        """Translates a batch of texts on GCS and stores the result in a GCS location.
    
        Args:
            input_uri: The input URI of the texts to be translated.
            output_uri: The output URI of the translated texts.
            project_id: The ID of the project that owns the destination bucket.
            timeout: The timeout for this batch translation operation.
    
        Returns:
            The translated texts.
        """
    
        client = [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)()
    
        location = "us-central1"
        # Supported file types: https://cloud.google.com/translate/docs/supported-formats
        gcs_source = {"input_uri": input_uri}
    
        input_configs_element = {
            "gcs_source": gcs_source,
            "mime_type": "text/plain",  # Can be "text/plain" or "text/html".
        }
        gcs_destination = {"output_uri_prefix": output_uri}
        output_config = {"gcs_destination": gcs_destination}
        parent = f"projects/{project_id}/locations/{location}"
    
        # Supported language codes: https://cloud.google.com/translate/docs/languages
        operation = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[batch_translate_text](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_batch_translate_text)(
            request={
                "parent": parent,
                "source_language_code": "en",
                "target_language_codes": ["ja"],  # Up to 10 language codes here.
                "input_configs": [input_configs_element],
                "output_config": output_config,
            }
        )
    
        print("Waiting for operation to complete...")
        response = operation.result(timeout)
    
        print(f"Total Characters: {response.total_characters}")
        print(f"Translated Characters: {response.translated_characters}")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtranslation). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
