---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-export-model-tabular-classification-sample/
title: Export a model for tabular classification \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:29.169085+00:00
---

# Export a model for tabular classification  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-export-model-tabular-classification-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Export a model for tabular classification Stay organized with collections  Save and categorize content based on your preferences. 

Exports a model for tabular classification using the export_model method.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Export AutoML tabular models](https://docs.cloud.google.com/vertex-ai/docs/export/export-model-tabular)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[ExportModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[ExportModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelRequest.html);
    import com.google.cloud.aiplatform.v1.[ExportModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelResponse.html);
    import com.google.cloud.aiplatform.v1.[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html);
    import com.google.cloud.aiplatform.v1.[ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html);
    import com.google.cloud.aiplatform.v1.[ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.html);
    import com.google.cloud.aiplatform.v1.[ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceSettings.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class ExportModelTabularClassificationSample {
      public static void main(String[] args)
          throws InterruptedException, ExecutionException, TimeoutException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        String gcsDestinationOutputUriPrefix = "gs://your-gcs-bucket/destination_path";
        String project = "YOUR_PROJECT_ID";
        String modelId = "YOUR_MODEL_ID";
        exportModelTableClassification(gcsDestinationOutputUriPrefix, project, modelId);
      }
    
      static void exportModelTableClassification(
          String gcsDestinationOutputUriPrefix, String project, String modelId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        [ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceSettings.html) modelServiceSettings =
            [ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.html) modelServiceClient = [ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.html).create(modelServiceSettings)) {
          String location = "us-central1";
          [ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html) modelName = [ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html).of(project, location, modelId);
    
          [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html).Builder gcsDestination = [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html).newBuilder();
          gcsDestination.[setOutputUriPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.Builder.html#com_google_cloud_aiplatform_v1_GcsDestination_Builder_setOutputUriPrefix_java_lang_String_)(gcsDestinationOutputUriPrefix);
          [ExportModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelRequest.html).[OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.OutputConfig.html) outputConfig =
              [ExportModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelRequest.html).OutputConfig.newBuilder()
                  .[setExportFormatId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelRequest.OutputConfig.Builder.html#com_google_cloud_aiplatform_v1_ExportModelRequest_OutputConfig_Builder_setExportFormatId_java_lang_String_)("tf-saved-model")
                  .setArtifactDestination(gcsDestination)
                  .build();
    
          OperationFuture<ExportModelResponse, ExportModelOperationMetadata> exportModelResponseFuture =
              modelServiceClient.[exportModelAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.html#com_google_cloud_aiplatform_v1_ModelServiceClient_exportModelAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_ModelName_com_google_cloud_aiplatform_v1_ExportModelRequest_OutputConfig_)(modelName, outputConfig);
          System.out.format(
              "Operation name: %s\n", exportModelResponseFuture.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
          System.out.println("Waiting for operation to finish...");
          [ExportModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelResponse.html) exportModelResponse =
              exportModelResponseFuture.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(300, TimeUnit.SECONDS);
          System.out.format(
              "Export Model Tabular Classification Response: %s", exportModelResponse.toString());
        }
      }
    }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.\
     * (Not necessary if passing values as arguments)
     */
    
    // const gcsDestinationOutputUriPrefix ='YOUR_GCS_DESTINATION_\
    // OUTPUT_URI_PREFIX'; eg. "gs://<your-gcs-bucket>/destination_path"
    // const modelId = 'YOUR_MODEL_ID';
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    
    // Imports the Google Cloud Model Service Client library
    const {ModelServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const modelServiceClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function exportModelTabularClassification() {
      // Configure the name resources
      const name = `projects/${project}/locations/${location}/models/${modelId}`;
      // Configure the outputConfig resources
      const outputConfig = {
        exportFormatId: 'tf-saved-model',
        artifactDestination: {
          outputUriPrefix: gcsDestinationOutputUriPrefix,
        },
      };
      const request = {
        name,
        outputConfig,
      };
    
      // Export Model request
      const [response] = await modelServiceClient.exportModel(request);
      console.log(`Long running operation : ${response.name}`);
    
      // Wait for operation to complete
      await response.promise();
      console.log(`Export model response : ${JSON.stringify(response.result)}`);
    }
    exportModelTabularClassification();

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform_v1beta1
    
    
    def export_model_tabular_classification_sample(
        project: str,
        model_id: str,
        gcs_destination_output_uri_prefix: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
        timeout: int = 300,
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform_v1beta1.[ModelServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.services.model_service.ModelServiceClient.html)(client_options=client_options)
        gcs_destination = {"output_uri_prefix": gcs_destination_output_uri_prefix}
        output_config = {
            "artifact_destination": gcs_destination,
            "export_format_id": "tf-saved-model",
        }
        name = client.[model_path](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.services.model_service.ModelServiceClient.html#google_cloud_aiplatform_v1beta1_services_model_service_ModelServiceClient_model_path)(project=project, location=location, model=model_id)
        response = client.[export_model](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.services.model_service.ModelServiceClient.html#google_cloud_aiplatform_v1beta1_services_model_service_ModelServiceClient_export_model)(name=name, output_config=output_config)
        print("Long running operation:", response.operation.name)
        print("output_info:", response.metadata.output_info)
        export_model_response = response.result(timeout=timeout)
        print("export_model_response:", export_model_response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
