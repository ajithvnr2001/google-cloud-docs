---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-sdk-tuning/
title: Tune language foundation model (Generative AI) \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:29:54.771795+00:00
---

# Tune language foundation model (Generative AI)  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-sdk-tuning/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Tune language foundation model (Generative AI) Stay organized with collections  Save and categorize content based on your preferences. 

Tune language foundation models with a tuning dataset. 

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[CreatePipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePipelineJobRequest.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.cloud.aiplatform.v1.[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob.html);
    import com.google.cloud.aiplatform.v1.[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob.html).[RuntimeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob.RuntimeConfig.html);
    import com.google.cloud.aiplatform.v1.[PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    
    public class CreatePipelineJobModelTuningSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "PROJECT";
        String location = "europe-west4"; // europe-west4 and us-central1 are the supported regions
        String pipelineJobDisplayName = "PIPELINE_JOB_DISPLAY_NAME";
        String modelDisplayName = "MODEL_DISPLAY_NAME";
        String outputDir = "OUTPUT_DIR";
        String datasetUri = "DATASET_URI";
        int trainingSteps = 300;
    
        createPipelineJobModelTuningSample(
            project,
            location,
            pipelineJobDisplayName,
            modelDisplayName,
            outputDir,
            datasetUri,
            trainingSteps);
      }
    
      // Create a model tuning job
      public static void createPipelineJobModelTuningSample(
          String project,
          String location,
          String pipelineJobDisplayName,
          String modelDisplayName,
          String outputDir,
          String datasetUri,
          int trainingSteps)
          throws IOException {
        final String endpoint = String.format("%s-aiplatform.googleapis.com:443", location);
        [PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html) pipelineServiceSettings =
            [PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html) client = [PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html).create(pipelineServiceSettings)) {
          Map<String, Value> parameterValues = new HashMap<>();
          parameterValues.put("project", stringToValue(project));
          parameterValues.put("model_display_name", stringToValue(modelDisplayName));
          parameterValues.put("dataset_uri", stringToValue(datasetUri));
          parameterValues.put(
              "location",
              stringToValue(
                  "us-central1")); // Deployment is only supported in us-central1 for Public Preview
          parameterValues.put("large_model_reference", stringToValue("text-bison@001"));
          parameterValues.put("train_steps", numberToValue(trainingSteps));
          parameterValues.put("accelerator_type", stringToValue("GPU")); // Optional: GPU or TPU
    
          [RuntimeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob.RuntimeConfig.html) runtimeConfig =
              [RuntimeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob.RuntimeConfig.html).newBuilder()
                  .setGcsOutputDirectory(outputDir)
                  .[putAllParameterValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob.RuntimeConfig.Builder.html#com_google_cloud_aiplatform_v1_PipelineJob_RuntimeConfig_Builder_putAllParameterValues_java_util_Map_java_lang_String_com_google_protobuf_Value__)(parameterValues)
                  .build();
    
          [PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob.html) pipelineJob =
              [PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob.html).newBuilder()
                  .[setTemplateUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob.Builder.html#com_google_cloud_aiplatform_v1_PipelineJob_Builder_setTemplateUri_java_lang_String_)(
                      "https://us-kfp.pkg.dev/ml-pipeline/large-language-model-pipelines/tune-large-model/v2.0.0")
                  .setDisplayName(pipelineJobDisplayName)
                  .[setRuntimeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob.Builder.html#com_google_cloud_aiplatform_v1_PipelineJob_Builder_setRuntimeConfig_com_google_cloud_aiplatform_v1_PipelineJob_RuntimeConfig_)(runtimeConfig)
                  .build();
    
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location);
          [CreatePipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePipelineJobRequest.html) request =
              [CreatePipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePipelineJobRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html#com_google_cloud_aiplatform_v1_LocationName_toString__)())
                  .setPipelineJob(pipelineJob)
                  .build();
    
          [PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob.html) response = client.createPipelineJob(request);
          System.out.format("response: %s\n", response);
          System.out.format("Name: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob.html#com_google_cloud_aiplatform_v1_PipelineJob_getName__)());
        }
      }
    
      static [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html) stringToValue(String str) {
        return [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue(str).build();
      }
    
      static [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html) numberToValue(int n) {
        return [Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setNumberValue(n).build();
      }
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
