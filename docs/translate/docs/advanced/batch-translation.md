---
url: https://docs.cloud.google.com/translate/docs/advanced/batch-translation/
title: Batch requests (Advanced) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:15.237678+00:00
---

# Batch requests (Advanced)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/batch-translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback 

#  Batch requests (Advanced) Stay organized with collections  Save and categorize content based on your preferences. 

The advanced version of the Cloud Translation API supports batch translation of large amounts of text in a command offline. There's a limit of 100 files, with 10 maximum target languages per batch. Also, the total content size should be no more than 100M Unicode codepoints, and the encoding must be UTF-8.

## Before you begin

Before you can start using the Cloud Translation API, you should complete the [Cloud Translation setup](https://docs.cloud.google.com/translate/docs/setup) page, which includes creating a project, enabling the Cloud Translation API, and setting up authentication. The setup page also provides instructions for installing client libraries for common programming languages, which is optional.

### Permissions

For batch translations, you must have access to Cloud Storage buckets in addition to the Cloud Translation [permissions](https://docs.cloud.google.com/translate/docs/intro-to-v3#iam). Batch translation input files are read from a Cloud Storage bucket and output files are written to a Cloud Storage bucket. For example, to read input files from a bucket, you must have at least read object permissions (provided by the role `roles/storage.objectViewer`) on the bucket. For more information about Cloud Storage roles, see the Cloud Storage [documentation](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

## Input file

Only two MIME types are supported: `text/html` (HTML) and `text/plain` (`tsv` and `txt`).

### Using a TSV file

If a file extension is TSV, it can contain either one or two columns. The first column (optional) is the ID of the text request. If the first column is missing, Google uses the row number (0-based) from the input file as the ID in the output file. The second column is the actual text to be translated. For best results, each row be less than or equal to 10K Unicode codepoints, otherwise an error may be returned.

**Note:** The input TSV must be RFC 4180 compliant. See the [reference documentation](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/batchTranslateText) for more details. You could use [csvlint](https://github.com/Clever/csvlint) to check potential formatting errors in your TSV file.

### Using text or HTML

The other supported file extensions are text files (.txt) or HTML, which is treated as a single large chunk of text.

## Batch request

With a batch translation request, you provide the path to an input configuration file ([InputConfig](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/batchTranslateText#InputConfig)) containing the content you want translated and provide a path to an output location ([OutputConfig](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/batchTranslateText#OutputConfig)) for the final translation. You need at least two different Cloud Storage buckets. The source bucket contains content to be translated, and the destination bucket will contain the resulting translated file(s). The destination folder must be empty before the translation process begins.

As the request is processing, we write the results to the output location in real time. Even if you [cancel the request](https://docs.cloud.google.com/translation/docs/advanced/long-running-operation#cancel-operation) halfway through, input file-level partial output are still produced in the output Cloud Storage location. Therefore, the translated number of characters are still charged.

**Note:** You can request batch translation using AutoML models and glossaries. Both output files use the model you've specified. See [reference documentation](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/batchTranslateText#OutputConfig) for the detailed execution logic and output format.**Note:** The LOCATION_ID in the request must match the LOCATION_ID of AutoML models and glossaries.

### REST

This example shows two input files sent for translating. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText

Request JSON body: 
    
    
    {
      "sourceLanguageCode": "en",
      "targetLanguageCodes": ["es", "fr"],
      "inputConfigs": [
       {
          "gcsSource": {
            "inputUri": "gs://bucket-name-source/input-file-name1"
          }
        },
        {
          "gcsSource": {
            "inputUri": "gs://bucket-name-source/input-file-name2"
          }
        }
      ],
      "outputConfig": {
          "gcsDestination": {
            "outputUriPrefix": "gs://bucket-name-destination/"
          }
       }
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
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText"

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
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-number/locations/us-central1/operations/20191107-08251564068323-5d3895ce-0000-2067-864c-001a1136fb06",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3.BatchTranslateMetadata",
        "state": "RUNNING"
      }
    }
    

The response contains the ID for a [long-running operation](https://docs.cloud.google.com/translate/docs/advanced/long-running-operation). 

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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## Making a batch request using an AutoML model

You can use a custom model for batch requests. There are various scenarios when multiple target languages are involved.

### Specifying an AutoML model for target language

### REST

This example shows how to specify a custom model for the target language. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText

Request JSON body: 
    
    
    {
      "models":{"es":"projects/PROJECT_NUMBER_OR_ID/locations/us-central1/models/model-id"},
      "sourceLanguageCode": "en",
      "targetLanguageCodes": ["es"],
      "inputConfigs": [
       {
          "gcsSource": {
            "inputUri": "gs://bucket-name-source/input-file-name1"
          }
        },
        {
          "gcsSource": {
            "inputUri": "gs://bucket-name-source/input-file-name2"
          }
        }
      ],
      "outputConfig": {
          "gcsDestination": {
            "outputUriPrefix": "gs://bucket-name-destination/"
          }
       }
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
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText"

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
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-number/locations/us-central1/operations/20190725-08251564068323-5d3895ce-0000-2067-864c-001a1136fb06",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3.BatchTranslateMetadata",
        "state": "RUNNING"
      }
    }
    

The response contains the ID for a [long-running operation](https://docs.cloud.google.com/translate/docs/advanced/long-running-operation). 

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
    
    // batchTranslateTextWithModel translates a large volume of text in asynchronous batch mode.
    func batchTranslateTextWithModel(w io.Writer, projectID string, location string, inputURI string, outputURI string, sourceLang string, targetLang string, modelID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// inputURI := "gs://cloud-samples-data/text.txt"
    	// outputURI := "gs://YOUR_BUCKET_ID/path_to_store_results/"
    	// sourceLang := "en"
    	// targetLang := "de"
    	// modelID := "your-model-id"
    
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
    		Models: map[string]string{
    			targetLang: fmt.Sprintf("projects/%s/locations/%s/models/%s", projectID, location, modelID),
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
    
    public class BatchTranslateTextWithModel {
    
      public static void batchTranslateTextWithModel()
          throws InterruptedException, ExecutionException, IOException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        // Supported Languages: https://cloud.google.com/translate/docs/languages
        String sourceLanguage = "your-source-language";
        String targetLanguage = "your-target-language";
        String inputUri = "gs://your-gcs-bucket/path/to/input/file.txt";
        String outputUri = "gs://your-gcs-bucket/path/to/results/";
        String modelId = "YOUR-MODEL-ID";
        batchTranslateTextWithModel(
            projectId, sourceLanguage, targetLanguage, inputUri, outputUri, modelId);
      }
    
      // Batch translate text using AutoML Translation model
      public static void batchTranslateTextWithModel(
          String projectId,
          String sourceLanguage,
          String targetLanguage,
          String inputUri,
          String outputUri,
          String modelId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model. (us-central1)
          String location = "us-central1";
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html).of(projectId, location);
    
          // Configure the source of the file from a GCS bucket
          [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html) gcsSource = [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html).newBuilder().setInputUri(inputUri).build();
          // Supported Mime Types: https://cloud.google.com/translate/docs/supported-formats
          [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.InputConfig.html) inputConfig =
              [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.InputConfig.html).newBuilder().setGcsSource(gcsSource).setMimeType("text/plain").build();
    
          // Configure where to store the output in a GCS bucket
          [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsDestination.html) gcsDestination =
              [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsDestination.html).newBuilder().setOutputUriPrefix(outputUri).build();
          [OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.OutputConfig.html) outputConfig =
              [OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.OutputConfig.html).newBuilder().setGcsDestination(gcsDestination).build();
    
          // Configure the model used in the request
          String modelPath =
              String.format("projects/%s/locations/%s/models/%s", projectId, location, modelId);
    
          // Build the request that will be sent to the API
          [BatchTranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateTextRequest.html) request =
              [BatchTranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateTextRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)())
                  .setSourceLanguageCode(sourceLanguage)
                  .addTargetLanguageCodes(targetLanguage)
                  .addInputConfigs(inputConfig)
                  .setOutputConfig(outputConfig)
                  .putModels(targetLanguage, modelPath)
                  .build();
    
          // Start an asynchronous request
          OperationFuture<BatchTranslateResponse, BatchTranslateMetadata> future =
              client.[batchTranslateTextAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html#com_google_cloud_translate_v3_TranslationServiceClient_batchTranslateTextAsync_com_google_cloud_translate_v3_BatchTranslateTextRequest_)(request);
    
          System.out.println("Waiting for operation to complete...");
    
          // random number between 300 - 450 (maximum allowed seconds)
          long randomNumber = ThreadLocalRandom.current().nextInt(450, 600);
          [BatchTranslateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateResponse.html) response = future.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(randomNumber, TimeUnit.SECONDS);
    
          // Display the translation for each input text provided
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
    // const modelId = 'YOUR_MODEL_ID';
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)');
    
    // Instantiates a client
    const client = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    async function batchTranslateTextWithModel() {
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
        models: {
          ja: `projects/${projectId}/locations/${location}/models/${modelId}`,
        },
      };
    
      const options = {timeout: 240000};
      // Create a job using a long-running operation
      const [operation] = await client.batchTranslateText(request, options);
    
      // Wait for the operation to complete
      const [response] = await operation.promise();
    
      // Display the translation for each input text provided
      console.log(`Total Characters: ${response.totalCharacters}`);
      console.log(`Translated Characters: ${response.translatedCharacters}`);
    }
    
    batchTranslateTextWithModel();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)
    
    
    def batch_translate_text_with_model(
        input_uri: str = "gs://YOUR_BUCKET_ID/path/to/your/file.txt",
        output_uri: str = "gs://YOUR_BUCKET_ID/path/to/save/results/",
        project_id: str = "YOUR_PROJECT_ID",
        model_id: str = "YOUR_MODEL_ID",
    ) -> translate.TranslationServiceClient:
        """Batch translate text using Translation model.
        Model can be AutoML or General[built-in] model.
    
        Args:
            input_uri: The input file to translate.
            output_uri: The output file to save the translation results.
            project_id: The ID of the GCP project that owns the model.
            model_id: The model ID.
    
        Returns:
            The response from the batch translation API.
        """
    
        client = [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)()
    
        # Supported file types: https://cloud.google.com/translate/docs/supported-formats
        gcs_source = {"input_uri": input_uri}
        location = "us-central1"
    
        input_configs_element = {
            "gcs_source": gcs_source,
            "mime_type": "text/plain",  # Can be "text/plain" or "text/html".
        }
        gcs_destination = {"output_uri_prefix": output_uri}
        output_config = {"gcs_destination": gcs_destination}
        parent = f"projects/{project_id}/locations/{location}"
    
        model_path = "projects/{}/locations/{}/models/{}".format(
            project_id, location, model_id  # The location of AutoML model.
        )
    
        # Supported language codes: https://cloud.google.com/translate/docs/languages
        models = {"ja": model_path}  # takes a target lang as key.
    
        operation = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[batch_translate_text](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_batch_translate_text)(
            request={
                "parent": parent,
                "source_language_code": "en",
                "target_language_codes": ["ja"],  # Up to 10 language codes here.
                "input_configs": [input_configs_element],
                "output_config": output_config,
                "models": models,
            }
        )
    
        print("Waiting for operation to complete...")
        response = operation.result()
    
        # Display the translation for each input text provided.
        print(f"Total Characters: {response.total_characters}")
        print(f"Translated Characters: {response.translated_characters}")
    
        return response
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

### Specifying AutoML models for multiple target languages

### REST

When you have multiple target languages, you can specify a custom model for each target language. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText

Request JSON body: 
    
    
    {
      "models":{
        "es":"projects/PROJECT_NUMBER_OR_ID/locations/us-central1/models/model-id1",
        "fr":"projects/PROJECT_NUMBER_OR_ID/locations/us-central1/models/model-id2"},
      "sourceLanguageCode": "en",
      "targetLanguageCodes": ["es", "fr"],
      "inputConfigs": [
       {
          "gcsSource": {
            "inputUri": "gs://bucket-name-source/input-file-name1"
          }
        },
        {
          "gcsSource": {
            "inputUri": "gs://bucket-name-source/input-file-name2"
          }
        }
      ],
      "outputConfig": {
          "gcsDestination": {
            "outputUriPrefix": "gs://bucket-name-destination/"
          }
       }
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
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText"

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
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-number/locations/us-central1/operations/20191105-08251564068323-5d3895ce-0000-2067-864c-001a1136fb06",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3.BatchTranslateMetadata",
        "state": "RUNNING"
      }
    }
    

The response contains the ID for a [long-running operation](https://docs.cloud.google.com/translate/docs/advanced/long-running-operation). 

### Specifying an AutoML model for a target language and not others

You can specify a custom model for a particular target language while not specifying a model for the other target languages. Using the code for Specifying custom models for multiple target language, just modify the `models` field to specify the target language for the model, `es` in this example, and leaving `fr` unspecified:

  * `"models": {'es':'projects/PROJECT_NUMBER_OR_ID/locations/us-central1/models/model-id'},`



where `PROJECT_NUMBER_OR_ID` is your Google Cloud project number or ID, and `model-id` is the name you've given your AutoML model.

### Translating text using a glossary

### REST

This example shows how to specify a glossary for the target language. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * glossary-id: your glossary ID, for example, "my-en-to-es-glossary" 



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText

Request JSON body: 
    
    
    {
      "sourceLanguageCode": "en",
      "targetLanguageCodes": ["es"],
      "glossaries": {
        "es": {
          "glossary": "projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries/glossary-id"
        }
      },
      "inputConfigs": [{
          "gcsSource": {
            "inputUri": "gs://bucket-name-source/input-file-name1"
          }
        },
        {
          "gcsSource": {
            "inputUri": "gs://bucket-name-source/input-file-name2"
          }
        }
      ],
      "outputConfig": {
        "gcsDestination": {
          "outputUriPrefix": "gs://bucket-name-destination/"
        }
      }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-number/locations/us-central1/operations/operation-id",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3.BatchTranslateMetadata",
        "state": "RUNNING"
      }
    }
    

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
    
    // batchTranslateTextWithGlossary translates a large volume of text in asynchronous batch mode.
    func batchTranslateTextWithGlossary(w io.Writer, projectID string, location string, inputURI string, outputURI string, sourceLang string, targetLang string, glossaryID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// inputURI := "gs://cloud-samples-data/text.txt"
    	// outputURI := "gs://YOUR_BUCKET_ID/path_to_store_results/"
    	// sourceLang := "en"
    	// targetLang := "ja"
    	// glossaryID := "your-glossary-id"
    
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
    		Glossaries: map[string]*translatepb.TranslateTextGlossaryConfig{
    			targetLang: {
    				Glossary: fmt.Sprintf("projects/%s/locations/%s/glossaries/%s", projectID, location, glossaryID),
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
    import com.google.cloud.translate.v3.[GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html);
    import com.google.cloud.translate.v3.[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.InputConfig.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
    import com.google.cloud.translate.v3.[OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.OutputConfig.html);
    import com.google.cloud.translate.v3.[TranslateTextGlossaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextGlossaryConfig.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.ThreadLocalRandom;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class BatchTranslateTextWithGlossary {
    
      public static void batchTranslateTextWithGlossary()
          throws InterruptedException, ExecutionException, IOException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        // Supported Languages: https://cloud.google.com/translate/docs/languages
        String sourceLanguage = "your-source-language";
        String targetLanguage = "your-target-language";
        String inputUri = "gs://your-gcs-bucket/path/to/input/file.txt";
        String outputUri = "gs://your-gcs-bucket/path/to/results/";
        String glossaryId = "your-glossary-display-name";
        batchTranslateTextWithGlossary(
            projectId, sourceLanguage, targetLanguage, inputUri, outputUri, glossaryId);
      }
    
      // Batch Translate Text with a Glossary.
      public static void batchTranslateTextWithGlossary(
          String projectId,
          String sourceLanguage,
          String targetLanguage,
          String inputUri,
          String outputUri,
          String glossaryId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model. (us-central1)
          String location = "us-central1";
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html).of(projectId, location);
    
          // Configure the source of the file from a GCS bucket
          [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html) gcsSource = [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html).newBuilder().setInputUri(inputUri).build();
          // Supported Mime Types: https://cloud.google.com/translate/docs/supported-formats
          [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.InputConfig.html) inputConfig =
              [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.InputConfig.html).newBuilder().setGcsSource(gcsSource).setMimeType("text/plain").build();
    
          // Configure where to store the output in a GCS bucket
          [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsDestination.html) gcsDestination =
              [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsDestination.html).newBuilder().setOutputUriPrefix(outputUri).build();
          [OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.OutputConfig.html) outputConfig =
              [OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.OutputConfig.html).newBuilder().setGcsDestination(gcsDestination).build();
    
          // Configure the glossary used in the request
          [GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html) glossaryName = [GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html).of(projectId, location, glossaryId);
          [TranslateTextGlossaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextGlossaryConfig.html) glossaryConfig =
              [TranslateTextGlossaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextGlossaryConfig.html).newBuilder().setGlossary(glossaryName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html#com_google_cloud_translate_v3_GlossaryName_toString__)()).build();
    
          // Build the request that will be sent to the API
          [BatchTranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateTextRequest.html) request =
              [BatchTranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateTextRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)())
                  .setSourceLanguageCode(sourceLanguage)
                  .addTargetLanguageCodes(targetLanguage)
                  .addInputConfigs(inputConfig)
                  .setOutputConfig(outputConfig)
                  .putGlossaries(targetLanguage, glossaryConfig)
                  .build();
    
          // Start an asynchronous request
          OperationFuture<BatchTranslateResponse, BatchTranslateMetadata> future =
              client.[batchTranslateTextAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html#com_google_cloud_translate_v3_TranslationServiceClient_batchTranslateTextAsync_com_google_cloud_translate_v3_BatchTranslateTextRequest_)(request);
    
          System.out.println("Waiting for operation to complete...");
    
          // random number between 300 - 450 (maximum allowed seconds)
          long randomNumber = ThreadLocalRandom.current().nextInt(450, 600);
          [BatchTranslateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateResponse.html) response = future.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(randomNumber, TimeUnit.SECONDS);
    
          // Display the translation for each input text provided
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
    // const glossaryId = 'YOUR_GLOSSARY_ID';
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)');
    
    // Instantiates a client
    const client = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    async function batchTranslateTextWithGlossary() {
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        sourceLanguageCode: 'en',
        targetLanguageCodes: ['es'],
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
        glossaries: {
          es: {
            glossary: `projects/${projectId}/locations/${location}/glossaries/${glossaryId}`,
          },
        },
      };
    
      const options = {timeout: 240000};
      // Create a job using a long-running operation
      const [operation] = await client.batchTranslateText(request, options);
    
      // Wait for the operation to complete
      const [response] = await operation.promise();
    
      // Display the translation for each input text provided
      console.log(`Total Characters: ${response.totalCharacters}`);
      console.log(`Translated Characters: ${response.translatedCharacters}`);
    }
    
    batchTranslateTextWithGlossary();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)
    
    
    def batch_translate_text_with_glossary(
        input_uri: str = "gs://YOUR_BUCKET_ID/path/to/your/file.txt",
        output_uri: str = "gs://YOUR_BUCKET_ID/path/to/save/results/",
        project_id: str = "YOUR_PROJECT_ID",
        glossary_id: str = "YOUR_GLOSSARY_ID",
        timeout: int = 320,
    ) -> translate.TranslateTextResponse:
        """Translates a batch of texts on GCS and stores the result in a GCS location.
        Glossary is applied for translation.
    
        Args:
            input_uri (str): The input file to translate.
            output_uri (str): The output file to save the translations to.
            project_id (str): The ID of the GCP project that owns the location.
            glossary_id (str): The ID of the glossary to use.
            timeout (int): The amount of time, in seconds, to wait for the operation to complete.
    
        Returns:
            The response from the batch.
        """
    
        client = [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)()
    
        # Supported language codes: https://cloud.google.com/translate/docs/languages
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
    
        # glossary is a custom dictionary Translation API uses
        # to translate the domain-specific terminology.
        glossary_path = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[glossary_path](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_glossary_path)(
            project_id, "us-central1", glossary_id  # The location of the glossary
        )
    
        glossary_config = [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[TranslateTextGlossaryConfig](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.types.TranslateTextGlossaryConfig.html)(glossary=glossary_path)
    
        glossaries = {"ja": glossary_config}  # target lang as key
    
        operation = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[batch_translate_text](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_batch_translate_text)(
            request={
                "parent": parent,
                "source_language_code": "en",
                "target_language_codes": ["ja"],  # Up to 10 language codes here.
                "input_configs": [input_configs_element],
                "glossaries": glossaries,
                "output_config": output_config,
            }
        )
    
        print("Waiting for operation to complete...")
        response = operation.result(timeout)
    
        print(f"Total Characters: {response.total_characters}")
        print(f"Translated Characters: {response.translated_characters}")
    
        return response
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

### Translating text using an AutoML Translation custom model and glossary

### REST

This example shows how to specify a custom model and glossary for the target language. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText

Request JSON body: 
    
    
    {
      "models": {
        "es": "projects/project_number_or_id/locations/us-central1/models/model-id"
      },
      "sourceLanguageCode": "en",
      "targetLanguageCodes": ["es"],
      "glossaries": {
        "es": {
          "glossary": "projects/project_number_or_id/locations/us-central1/glossaries/glossary-id"
        }
      },
      "inputConfigs": [{
          "gcsSource": {
            "inputUri": "gs://bucket-name-source/input-file-name"
          }
        },
        {
          "gcsSource": {
          "inputUri": "gs://bucket-name-source/input-file-name2"
          }
        }
      ],
      "outputConfig": {
        "gcsDestination": {
          "outputUriPrefix": "gs://bucket-name-destination/"
        }
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:batchTranslateText" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-number/locations/us-central1/operations/operation-id",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3.BatchTranslateMetadata",
        "state": "RUNNING"
      }
    }
    

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
    
    // batchTranslateTextWithGlossaryAndModel translates a large volume of text in asynchronous batch mode.
    func batchTranslateTextWithGlossaryAndModel(w io.Writer, projectID string, location string, inputURI string, outputURI string, sourceLang string, targetLang string, glossaryID string, modelID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// inputURI := "gs://cloud-samples-data/text.txt"
    	// outputURI := "gs://YOUR_BUCKET_ID/path_to_store_results/"
    	// sourceLang := "en"
    	// targetLang := "ja"
    	// glossaryID := "your-glossary-id"
    	// modelID := "your-model-id"
    
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
    		Glossaries: map[string]*translatepb.TranslateTextGlossaryConfig{
    			targetLang: {
    				Glossary: fmt.Sprintf("projects/%s/locations/%s/glossaries/%s", projectID, location, glossaryID),
    			},
    		},
    		OutputConfig: &translatepb.OutputConfig{
    			Destination: &translatepb.OutputConfig_GcsDestination{
    				GcsDestination: &translatepb.GcsDestination{
    					OutputUriPrefix: outputURI,
    				},
    			},
    		},
    		Models: map[string]string{
    			targetLang: fmt.Sprintf("projects/%s/locations/%s/models/%s", projectID, location, modelID),
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
    import com.google.cloud.translate.v3.[GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html);
    import com.google.cloud.translate.v3.[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.InputConfig.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
    import com.google.cloud.translate.v3.[OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.OutputConfig.html);
    import com.google.cloud.translate.v3.[TranslateTextGlossaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextGlossaryConfig.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.ThreadLocalRandom;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class BatchTranslateTextWithGlossaryAndModel {
    
      public static void batchTranslateTextWithGlossaryAndModel()
          throws InterruptedException, ExecutionException, IOException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        // Supported Languages: https://cloud.google.com/translate/docs/languages
        String sourceLanguage = "your-source-language";
        String targetLanguage = "your-target-language";
        String inputUri = "gs://your-gcs-bucket/path/to/input/file.txt";
        String outputUri = "gs://your-gcs-bucket/path/to/results/";
        String glossaryId = "your-glossary-display-name";
        String modelId = "YOUR-MODEL-ID";
        batchTranslateTextWithGlossaryAndModel(
            projectId, sourceLanguage, targetLanguage, inputUri, outputUri, glossaryId, modelId);
      }
    
      // Batch translate text with Model and Glossary
      public static void batchTranslateTextWithGlossaryAndModel(
          String projectId,
          String sourceLanguage,
          String targetLanguage,
          String inputUri,
          String outputUri,
          String glossaryId,
          String modelId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model. (us-central1)
          String location = "us-central1";
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html).of(projectId, location);
    
          // Configure the source of the file from a GCS bucket
          [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html) gcsSource = [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html).newBuilder().setInputUri(inputUri).build();
          // Supported Mime Types: https://cloud.google.com/translate/docs/supported-formats
          [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.InputConfig.html) inputConfig =
              [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.InputConfig.html).newBuilder().setGcsSource(gcsSource).setMimeType("text/plain").build();
    
          // Configure where to store the output in a GCS bucket
          [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsDestination.html) gcsDestination =
              [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsDestination.html).newBuilder().setOutputUriPrefix(outputUri).build();
          [OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.OutputConfig.html) outputConfig =
              [OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.OutputConfig.html).newBuilder().setGcsDestination(gcsDestination).build();
    
          // Configure the glossary used in the request
          [GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html) glossaryName = [GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html).of(projectId, location, glossaryId);
          [TranslateTextGlossaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextGlossaryConfig.html) glossaryConfig =
              [TranslateTextGlossaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextGlossaryConfig.html).newBuilder().setGlossary(glossaryName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html#com_google_cloud_translate_v3_GlossaryName_toString__)()).build();
    
          // Configure the model used in the request
          String modelPath =
              String.format("projects/%s/locations/%s/models/%s", projectId, location, modelId);
    
          // Build the request that will be sent to the API
          [BatchTranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateTextRequest.html) request =
              [BatchTranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateTextRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)())
                  .setSourceLanguageCode(sourceLanguage)
                  .addTargetLanguageCodes(targetLanguage)
                  .addInputConfigs(inputConfig)
                  .setOutputConfig(outputConfig)
                  .putGlossaries(targetLanguage, glossaryConfig)
                  .putModels(targetLanguage, modelPath)
                  .build();
    
          // Start an asynchronous request
          OperationFuture<BatchTranslateResponse, BatchTranslateMetadata> future =
              client.[batchTranslateTextAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html#com_google_cloud_translate_v3_TranslationServiceClient_batchTranslateTextAsync_com_google_cloud_translate_v3_BatchTranslateTextRequest_)(request);
    
          System.out.println("Waiting for operation to complete...");
    
          // random number between 300 - 450 (maximum allowed seconds)
          long randomNumber = ThreadLocalRandom.current().nextInt(450, 600);
          [BatchTranslateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateResponse.html) response = future.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(randomNumber, TimeUnit.SECONDS);
    
          // Display the translation for each input text provided
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
    // const glossaryId = 'YOUR_GLOSSARY_ID';
    // const modelId = 'YOUR_MODEL_ID';
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)');
    
    // Instantiates a client
    const client = new [TranslationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)();
    async function batchTranslateTextWithGlossaryAndModel() {
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
        glossaries: {
          ja: {
            glossary: `projects/${projectId}/locations/${location}/glossaries/${glossaryId}`,
          },
        },
        models: {
          ja: `projects/${projectId}/locations/${location}/models/${modelId}`,
        },
      };
    
      const options = {timeout: 240000};
      // Create a job using a long-running operation
      const [operation] = await client.batchTranslateText(request, options);
    
      // Wait for operation to complete
      const [response] = await operation.promise();
    
      // Display the translation for each input text provided
      console.log(`Total Characters: ${response.totalCharacters}`);
      console.log(`Translated Characters: ${response.translatedCharacters}`);
    }
    
    batchTranslateTextWithGlossaryAndModel();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)
    
    
    def batch_translate_text_with_glossary_and_model(
        input_uri: str,
        output_uri: str,
        project_id: str,
        model_id: str,
        glossary_id: str,
    ) -> translate.TranslateTextResponse:
        """Batch translate text with Glossary and Translation model.
        Args:
            input_uri: The input text to be translated.
            output_uri: The output text to be translated.
            project_id: The ID of the GCP project that owns the model.
            model_id: The ID of the model
            glossary_id: The ID of the glossary
    
        Returns:
            The translated text.
        """
    
        client = [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)()
    
        # Supported language codes: https://cloud.google.com/translate/docs/languages
        location = "us-central1"
    
        target_language_codes = ["ja"]
        gcs_source = {"input_uri": input_uri}
    
        # Optional. Can be "text/plain" or "text/html".
        mime_type = "text/plain"
        input_configs_element = {"gcs_source": gcs_source, "mime_type": mime_type}
        input_configs = [input_configs_element]
        gcs_destination = {"output_uri_prefix": output_uri}
        output_config = {"gcs_destination": gcs_destination}
        parent = f"projects/{project_id}/locations/{location}"
        model_path = "projects/{}/locations/{}/models/{}".format(
            project_id, "us-central1", model_id
        )
        models = {"ja": model_path}
    
        glossary_path = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[glossary_path](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_glossary_path)(
            project_id, "us-central1", glossary_id  # The location of the glossary
        )
    
        glossary_config = [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html).[TranslateTextGlossaryConfig](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.types.TranslateTextGlossaryConfig.html)(glossary=glossary_path)
        glossaries = {"ja": glossary_config}  # target lang as key
    
        operation = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[batch_translate_text](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_batch_translate_text)(
            request={
                "parent": parent,
                "source_language_code": "en",
                "target_language_codes": target_language_codes,
                "input_configs": input_configs,
                "output_config": output_config,
                "models": models,
                "glossaries": glossaries,
            }
        )
    
        print("Waiting for operation to complete...")
        response = operation.result()
    
        # Display the translation for each input text provided
        print(f"Total Characters: {response.total_characters}")
        print(f"Translated Characters: {response.translated_characters}")
    
        return response
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## Operation status

A batch request is a long-running operation, so it may take a substantial amount of time to complete. You can poll the status of this operation to see if it has completed, or you can cancel the operation.

For more information, see [Long-running operations](https://docs.cloud.google.com/translation/docs/advanced/long-running-operation).

## Additional resources

  * For help on resolving common issues or errors, see the [Troubleshooting](https://docs.cloud.google.com/translate/troubleshooting) page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
