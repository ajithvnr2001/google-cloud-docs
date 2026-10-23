---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-batch-prediction-job-text-sentiment-analysis-sample/
title: Create a batch prediction job for text sentiment analysis \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:21.863727+00:00
---

# Create a batch prediction job for text sentiment analysis  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-batch-prediction-job-text-sentiment-analysis-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Create a batch prediction job for text sentiment analysis Stay organized with collections  Save and categorize content based on your preferences. 

Creates a batch prediction job for text sentiment analysis using the create_batch_prediction_job method.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.aiplatform.v1.[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html);
    import com.google.cloud.aiplatform.v1.[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html);
    import com.google.cloud.aiplatform.v1.[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html);
    import com.google.cloud.aiplatform.v1.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html);
    import com.google.cloud.aiplatform.v1.[JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.cloud.aiplatform.v1.[ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html);
    import java.io.IOException;
    
    public class CreateBatchPredictionJobTextSentimentAnalysisSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "PROJECT";
        String location = "us-central1";
        String displayName = "DISPLAY_NAME";
        String modelId = "MODEL_ID";
        String gcsSourceUri = "GCS_SOURCE_URI";
        String gcsDestinationOutputUriPrefix = "GCS_DESTINATION_OUTPUT_URI_PREFIX";
        createBatchPredictionJobTextSentimentAnalysisSample(
            project, location, displayName, modelId, gcsSourceUri, gcsDestinationOutputUriPrefix);
      }
    
      static void createBatchPredictionJobTextSentimentAnalysisSample(
          String project,
          String location,
          String displayName,
          String modelId,
          String gcsSourceUri,
          String gcsDestinationOutputUriPrefix)
          throws IOException {
        // The AI Platform services require regional API endpoints.
        [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html) settings =
            [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html) client = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html).create(settings)) {
          try {
            String modelName = [ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html).of(project, location, modelId).toString();
            [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html) gcsSource = [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html).newBuilder().[addUris](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.Builder.html#com_google_cloud_aiplatform_v1_GcsSource_Builder_addUris_java_lang_String_)(gcsSourceUri).build();
            [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.html) inputConfig =
                [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).InputConfig.newBuilder()
                    .[setInstancesFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_InputConfig_Builder_setInstancesFormat_java_lang_String_)("jsonl")
                    .setGcsSource(gcsSource)
                    .build();
            [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html) gcsDestination =
                [GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html).newBuilder().[setOutputUriPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.Builder.html#com_google_cloud_aiplatform_v1_GcsDestination_Builder_setOutputUriPrefix_java_lang_String_)(gcsDestinationOutputUriPrefix).build();
            [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).[OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.OutputConfig.html) outputConfig =
                [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).OutputConfig.newBuilder()
                    .[setPredictionsFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.OutputConfig.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_OutputConfig_Builder_setPredictionsFormat_java_lang_String_)("jsonl")
                    .setGcsDestination(gcsDestination)
                    .build();
            [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) batchPredictionJob =
                [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).newBuilder()
                    .setDisplayName(displayName)
                    .setModel(modelName)
                    .[setInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_Builder_setInputConfig_com_google_cloud_aiplatform_v1_BatchPredictionJob_InputConfig_)(inputConfig)
                    .setOutputConfig(outputConfig)
                    .build();
            [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location);
            [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) response = client.createBatchPredictionJob(parent, batchPredictionJob);
            System.out.format("response: %s\n", response);
          } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) ex) {
            System.out.format("Exception: %s\n", ex.[getLocalizedMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails_getLocalizedMessage__)());
          }
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
    
    // const batchPredictionDisplayName = 'YOUR_BATCH_PREDICTION_DISPLAY_NAME';
    // const modelId = 'YOUR_MODEL_ID';
    // const gcsSourceUri = 'YOUR_GCS_SOURCE_URI';
    // const gcsDestinationOutputUriPrefix = 'YOUR_GCS_DEST_OUTPUT_URI_PREFIX';
    //    eg. "gs://<your-gcs-bucket>/destination_path"
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    
    // Imports the Google Cloud Job Service Client library
    const {JobServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const jobServiceClient = new [JobServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function createBatchPredictionJobTextSentimentAnalysis() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}`;
      const modelName = `projects/${project}/locations/${location}/models/${modelId}`;
    
      const inputConfig = {
        instancesFormat: 'jsonl',
        gcsSource: {uris: [gcsSourceUri]},
      };
      const outputConfig = {
        predictionsFormat: 'jsonl',
        gcsDestination: {outputUriPrefix: gcsDestinationOutputUriPrefix},
      };
      const batchPredictionJob = {
        displayName: batchPredictionDisplayName,
        model: modelName,
        inputConfig,
        outputConfig,
      };
      const request = {
        parent,
        batchPredictionJob,
      };
    
      // Create batch prediction job request
      const [response] = await jobServiceClient.createBatchPredictionJob(request);
    
      console.log('Create batch prediction job text sentiment analysis response');
      console.log(`Name : ${response.name}`);
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    createBatchPredictionJobTextSentimentAnalysis();

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value
    
    
    def create_batch_prediction_job_text_sentiment_analysis_sample(
        project: str,
        display_name: str,
        model_name: str,
        gcs_source_uri: str,
        gcs_destination_output_uri_prefix: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.job_service.JobServiceClient.html)(client_options=client_options)
        model_parameters_dict = {}
        model_parameters = json_format.ParseDict(model_parameters_dict, Value())
    
        batch_prediction_job = {
            "display_name": display_name,
            # Format: 'projects/{project}/locations/{location}/models/{model_id}'
            "model": model_name,
            "model_parameters": model_parameters,
            "input_config": {
                "instances_format": "jsonl",
                "gcs_source": {"uris": [gcs_source_uri]},
            },
            "output_config": {
                "predictions_format": "jsonl",
                "gcs_destination": {"output_uri_prefix": gcs_destination_output_uri_prefix},
            },
        }
        parent = f"projects/{project}/locations/{location}"
        response = client.[create_batch_prediction_job](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.job_service.JobServiceClient.html#google_cloud_aiplatform_v1_services_job_service_JobServiceClient_create_batch_prediction_job)(
            parent=parent, batch_prediction_job=batch_prediction_job
        )
        print("response:", response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
