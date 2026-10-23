---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-batch-prediction-job-bigquery-sample/
title: Create a batch prediction job for BigQuery \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:39.579595+00:00
---

# Create a batch prediction job for BigQuery  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-batch-prediction-job-bigquery-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Create a batch prediction job for BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

Creates a batch prediction job for BigQuery using the create_batch_prediction_job method.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get batch inferences and explanations](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/e2e-automl-batch-predictions)
  * [Get batch inferences for a forecast model](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/forecasting-batch-predictions)
  * [Get batch inferences for AutoML models](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/classification-regression/get-batch-predictions)
  * [Get inferences for a forecast model](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/forecasting/get-predictions)
  * [Get TabNet batch inferences](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/tabnet-batch-predictions)
  * [Get Wide & Deep batch inferences](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular-workflows/wide-and-deep-batch-predictions)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html);
    import com.google.cloud.aiplatform.v1.[BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html);
    import com.google.cloud.aiplatform.v1.[BigQuerySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQuerySource.html);
    import com.google.cloud.aiplatform.v1.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html);
    import com.google.cloud.aiplatform.v1.[JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.cloud.aiplatform.v1.[ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html);
    import com.google.gson.JsonObject;
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.IOException;
    
    public class CreateBatchPredictionJobBigquerySample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "PROJECT";
        String displayName = "DISPLAY_NAME";
        String modelName = "MODEL_NAME";
        String instancesFormat = "INSTANCES_FORMAT";
        String bigquerySourceInputUri = "BIGQUERY_SOURCE_INPUT_URI";
        String predictionsFormat = "PREDICTIONS_FORMAT";
        String bigqueryDestinationOutputUri = "BIGQUERY_DESTINATION_OUTPUT_URI";
        createBatchPredictionJobBigquerySample(
            project,
            displayName,
            modelName,
            instancesFormat,
            bigquerySourceInputUri,
            predictionsFormat,
            bigqueryDestinationOutputUri);
      }
    
      static void createBatchPredictionJobBigquerySample(
          String project,
          String displayName,
          String model,
          String instancesFormat,
          String bigquerySourceInputUri,
          String predictionsFormat,
          String bigqueryDestinationOutputUri)
          throws IOException {
        [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html) settings =
            [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
        String location = "us-central1";
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html) client = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html).create(settings)) {
          JsonObject jsonModelParameters = new JsonObject();
          [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html).Builder modelParametersBuilder = [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html).newBuilder();
          [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(jsonModelParameters.toString(), modelParametersBuilder);
          [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html) modelParameters = modelParametersBuilder.build();
          [BigQuerySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQuerySource.html) bigquerySource =
              [BigQuerySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQuerySource.html).newBuilder().[setInputUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQuerySource.Builder.html#com_google_cloud_aiplatform_v1_BigQuerySource_Builder_setInputUri_java_lang_String_)(bigquerySourceInputUri).build();
          [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.html) inputConfig =
              [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).InputConfig.newBuilder()
                  .[setInstancesFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_InputConfig_Builder_setInstancesFormat_java_lang_String_)(instancesFormat)
                  .setBigquerySource(bigquerySource)
                  .build();
          [BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html) bigqueryDestination =
              [BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html).newBuilder().setOutputUri(bigqueryDestinationOutputUri).build();
          [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).[OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.OutputConfig.html) outputConfig =
              [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).OutputConfig.newBuilder()
                  .[setPredictionsFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.OutputConfig.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_OutputConfig_Builder_setPredictionsFormat_java_lang_String_)(predictionsFormat)
                  .setBigqueryDestination(bigqueryDestination)
                  .build();
          String modelName = [ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html).of(project, location, model).toString();
          [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) batchPredictionJob =
              [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).newBuilder()
                  .setDisplayName(displayName)
                  .setModel(modelName)
                  .[setModelParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_Builder_setModelParameters_com_google_protobuf_Value_)(modelParameters)
                  .[setInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_Builder_setInputConfig_com_google_cloud_aiplatform_v1_BatchPredictionJob_InputConfig_)(inputConfig)
                  .setOutputConfig(outputConfig)
                  .build();
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location);
          [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) response = client.createBatchPredictionJob(parent, batchPredictionJob);
          System.out.format("response: %s\n", response);
          System.out.format("\tName: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getName__)());
        }
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform_v1beta1
    from google.protobuf import json_format
    from google.protobuf.struct_pb2 import Value
    
    
    def create_batch_prediction_job_bigquery_sample(
        project: str,
        display_name: str,
        model_name: str,
        instances_format: str,
        bigquery_source_input_uri: str,
        predictions_format: str,
        bigquery_destination_output_uri: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform_v1beta1.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.services.job_service.JobServiceClient.html)(client_options=client_options)
        model_parameters_dict = {}
        model_parameters = json_format.ParseDict(model_parameters_dict, Value())
    
        batch_prediction_job = {
            "display_name": display_name,
            # Format: 'projects/{project}/locations/{location}/models/{model_id}'
            "model": model_name,
            "model_parameters": model_parameters,
            "input_config": {
                "instances_format": instances_format,
                "bigquery_source": {"input_uri": bigquery_source_input_uri},
            },
            "output_config": {
                "predictions_format": predictions_format,
                "bigquery_destination": {"output_uri": bigquery_destination_output_uri},
            },
            # optional
            "generate_explanation": True,
        }
        parent = f"projects/{project}/locations/{location}"
        response = client.[create_batch_prediction_job](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.services.job_service.JobServiceClient.html#google_cloud_aiplatform_v1beta1_services_job_service_JobServiceClient_create_batch_prediction_job)(
            parent=parent, batch_prediction_job=batch_prediction_job
        )
        print("response:", response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
