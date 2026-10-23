---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-batch-predict-gemini-createjob-gcs/
title: Batch Predict with Gemini using GCS data \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:51.251655+00:00
---

# Batch Predict with Gemini using GCS data  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-batch-predict-gemini-createjob-gcs/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Batch Predict with Gemini using GCS data Stay organized with collections  Save and categorize content based on your preferences. 

Perform batch text prediction with Gemini using GCS data source as input.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get batch predictions for Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/batch-prediction-api)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html);
    import com.google.cloud.aiplatform.v1.[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html);
    import com.google.cloud.aiplatform.v1.[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html);
    import com.google.cloud.aiplatform.v1.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html);
    import com.google.cloud.aiplatform.v1.[JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import java.io.IOException;
    
    public class CreateBatchPredictionGeminiJobSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Update these variables before running the sample.
        String project = "PROJECT_ID";
        String gcsDestinationOutputUriPrefix = "gs://MY_BUCKET/";
    
        createBatchPredictionGeminiJobSample(project, gcsDestinationOutputUriPrefix);
      }
    
      // Create a batch prediction job using a JSONL input file and output URI, both in Cloud
      // Storage.
      public static [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) createBatchPredictionGeminiJobSample(
          String project, String gcsDestinationOutputUriPrefix) throws IOException {
        String location = "us-central1";
        [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html) settings =
            [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html).newBuilder()
                .setEndpoint(String.format("%s-aiplatform.googleapis.com:443", location))
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html) client = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html).create(settings)) {
          [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html) gcsSource =
              [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html).newBuilder()
                  .[addUris](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.Builder.html#com_google_cloud_aiplatform_v1_GcsSource_Builder_addUris_java_lang_String_)(
                      "gs://cloud-samples-data/generative-ai/batch/"
                          + "batch_requests_for_multimodal_input.jsonl")
                  // Or try
                  // "gs://cloud-samples-data/generative-ai/batch/gemini_multimodal_batch_predict.jsonl"
                  // for a batch prediction that uses audio, video, and an image.
                  .build();
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
          String modelName =
              String.format(
                  "projects/%s/locations/%s/publishers/google/models/%s",
                  project, location, "gemini-2.5-flash");
    
          [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) batchPredictionJob =
              [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).newBuilder()
                  .setDisplayName("my-display-name")
                  .setModel(modelName) // Add model parameters per request in the input jsonl file.
                  .[setInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_Builder_setInputConfig_com_google_cloud_aiplatform_v1_BatchPredictionJob_InputConfig_)(inputConfig)
                  .setOutputConfig(outputConfig)
                  .build();
    
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location);
          [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) response = client.createBatchPredictionJob(parent, batchPredictionJob);
          System.out.format("\tName: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getName__)());
          // Example response:
          //   Name: projects/<project>/locations/us-central1/batchPredictionJobs/<job-id>
          return response;
        }
      }
    }
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the aiplatform library
    const aiplatformLib = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    const aiplatform = aiplatformLib.protos.google.cloud.aiplatform.v1;
    
    /**
     * TODO(developer):  Uncomment/update these variables before running the sample.
     */
    // projectId = 'YOUR_PROJECT_ID';
    // URI of the output folder in Google Cloud Storage.
    // E.g. "gs://[BUCKET]/[OUTPUT]"
    // outputUri = 'gs://my-bucket';
    
    // URI of the input file in Google Cloud Storage.
    // E.g. "gs://[BUCKET]/[DATASET].jsonl"
    // Or try:
    // "gs://cloud-samples-data/generative-ai/batch/gemini_multimodal_batch_predict.jsonl"
    // for a batch prediction that uses audio, video, and an image.
    const inputUri =
      'gs://cloud-samples-data/generative-ai/batch/batch_requests_for_multimodal_input.jsonl';
    const location = 'us-central1';
    const parent = `projects/${projectId}/locations/${location}`;
    const modelName = `${parent}/publishers/google/models/gemini-2.5-flash`;
    
    // Specify the location of the api endpoint.
    const clientOptions = {
      apiEndpoint: `${location}-aiplatform.googleapis.com`,
    };
    
    // Instantiate the client.
    const jobServiceClient = new aiplatformLib.[JobServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    // Create a Gemini batch prediction job using Google Cloud Storage input and output buckets.
    async function create_batch_prediction_gemini_gcs() {
      const gcsSource = new aiplatform.GcsSource({
        uris: [inputUri],
      });
    
      const inputConfig = new aiplatform.BatchPredictionJob.InputConfig({
        gcsSource: gcsSource,
        instancesFormat: 'jsonl',
      });
    
      const gcsDestination = new aiplatform.GcsDestination({
        outputUriPrefix: outputUri,
      });
    
      const outputConfig = new aiplatform.BatchPredictionJob.OutputConfig({
        gcsDestination: gcsDestination,
        predictionsFormat: 'jsonl',
      });
    
      const batchPredictionJob = new aiplatform.BatchPredictionJob({
        displayName: 'Batch predict with Gemini - GCS',
        model: modelName,
        inputConfig: inputConfig,
        outputConfig: outputConfig,
      });
    
      const request = {
        parent: parent,
        batchPredictionJob,
      };
    
      // Create batch prediction job request
      const [response] = await jobServiceClient.createBatchPredictionJob(request);
      console.log('Response name: ', response.name);
      // Example response:
      // Response name: projects/<project>/locations/us-central1/batchPredictionJobs/<job-id>
    }
    
    await create_batch_prediction_gemini_gcs();

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
