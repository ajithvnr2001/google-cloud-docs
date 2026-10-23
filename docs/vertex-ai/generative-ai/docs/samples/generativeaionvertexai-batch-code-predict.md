---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-batch-code-predict/
title: Batch code prediction with a pre-trained model \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:50.885791+00:00
---

# Batch code prediction with a pre-trained model  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-batch-code-predict/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Batch code prediction with a pre-trained model Stay organized with collections  Save and categorize content based on your preferences. 

Perform batch code prediction using a pre-trained code generation model.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	aiplatform "cloud.google.com/go/aiplatform/apiv1"
    	aiplatformpb "cloud.google.com/go/aiplatform/apiv1/aiplatformpb"
    	"google.golang.org/api/option"
    	"google.golang.org/protobuf/types/known/structpb"
    )
    
    // batchCodePredict perform batch code prediction using a pre-trained code generation model
    func batchCodePredict(w io.Writer, projectID, location, name, outputURI string, inputURIs []string) error {
    	// inputURI := []string{"gs://cloud-samples-data/batch/prompt_for_batch_code_predict.jsonl"}
    	// outputURI: existing template path. Following formats are allowed:
    	// 	- gs://BUCKET_NAME/DIRECTORY/
    	// 	- bq://project_name.llm_dataset
    
    	ctx := context.Background()
    	apiEndpoint := fmt.Sprintf("%s-aiplatform.googleapis.com:443", location)
    	// Pretrained code model
    	model := "publishers/google/models/gemini-2.5-flash"
    	parameters := map[string]interface{}{
    		"temperature":     0.2,
    		"maxOutputTokens": 200,
    	}
    	parametersValue, err := structpb.NewValue(parameters)
    	if err != nil {
    		fmt.Fprintf(w, "unable to convert parameters to Value: %v", err)
    		return err
    	}
    
    	client, err := aiplatform.[NewJobClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1.html#cloud_google_com_go_aiplatform_apiv1_JobClient_NewJobClient)(ctx, option.WithEndpoint(apiEndpoint))
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	req := &aiplatformpb.CreateBatchPredictionJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		BatchPredictionJob: &aiplatformpb.BatchPredictionJob{
    			DisplayName:     name,
    			Model:           model,
    			ModelParameters: parametersValue,
    			InputConfig: &aiplatformpb.BatchPredictionJob_InputConfig{
    				Source: &aiplatformpb.BatchPredictionJob_InputConfig_GcsSource{
    					GcsSource: &aiplatformpb.GcsSource{
    						Uris: inputURIs,
    					},
    				},
    				// List of supported formarts: https://cloud.google.com/vertex-ai/docs/reference/rpc/google.cloud.aiplatform.v1#model
    				InstancesFormat: "jsonl",
    			},
    			OutputConfig: &aiplatformpb.BatchPredictionJob_OutputConfig{
    				Destination: &aiplatformpb.BatchPredictionJob_OutputConfig_GcsDestination{
    					GcsDestination: &aiplatformpb.GcsDestination{
    						OutputUriPrefix: outputURI,
    					},
    				},
    				// List of supported formarts: https://cloud.google.com/vertex-ai/docs/reference/rpc/google.cloud.aiplatform.v1#model
    				PredictionsFormat: "jsonl",
    			},
    		},
    	}
    
    	job, err := client.CreateBatchPredictionJob(ctx, req)
    	if err != nil {
    		return err
    	}
    	fmt.Fprint(w, job.GetDisplayName())
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html);
    import com.google.cloud.aiplatform.v1.[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html);
    import com.google.cloud.aiplatform.v1.[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html);
    import com.google.cloud.aiplatform.v1.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html);
    import com.google.cloud.aiplatform.v1.[JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.gson.Gson;
    import com.google.protobuf.[InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html);
    import com.google.protobuf.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    
    public class BatchCodePredictionSample {
    
      public static void main(String[] args) throws IOException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String location = "us-central1";
        // inputUri: URI of the input dataset.
        // Could be a BigQuery table or a Google Cloud Storage file.
        // E.g. "gs://[BUCKET]/[DATASET].jsonl" OR "bq://[PROJECT].[DATASET].[TABLE]"
        String inputUri = "gs://cloud-samples-data/batch/prompt_for_batch_code_predict.jsonl";
        // outputUri: URI where the output will be stored.
        // Could be a BigQuery table or a Google Cloud Storage file.
        // E.g. "gs://[BUCKET]/[OUTPUT].jsonl" OR "bq://[PROJECT].[DATASET].[TABLE]"
        String outputUri = "gs://YOUR_BUCKET/batch_code_predict_output";
        String codeModel = "code-bison";
    
        batchCodePredictionSample(project, location, inputUri, outputUri, codeModel);
      }
    
      // Perform batch code prediction using a pre-trained code generation model.
      // Example of using Google Cloud Storage bucket as the input and output data source
      public static [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) batchCodePredictionSample(
          String project, String location, String inputUri, String outputUri, String codeModel)
          throws IOException {
        [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) response;
        [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html) jobServiceSettings =  [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html).newBuilder()
            .setEndpoint("us-central1-aiplatform.googleapis.com:443").build();
        [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location);
        String modelName = String.format(
            "projects/%s/locations/%s/publishers/google/models/%s", project, location, codeModel);
        // Construct your modelParameters
        Map<String, String> modelParameters = new HashMap<>();
        modelParameters.put("maxOutputTokens", "200");
        modelParameters.put("temperature", "0.2");
        modelParameters.put("topP", "0.95");
        modelParameters.put("topK", "40");
        [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html) parameterValue = mapToValue(modelParameters);
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html) client = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html).create(jobServiceSettings)) {
          [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) batchPredictionJob =
              [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).newBuilder()
                  .setDisplayName("my batch code prediction job " + System.currentTimeMillis())
                  .setModel(modelName)
                  .[setInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_Builder_setInputConfig_com_google_cloud_aiplatform_v1_BatchPredictionJob_InputConfig_)(
                      [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).InputConfig.newBuilder()
                          .setGcsSource([GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html).newBuilder().[addUris](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.Builder.html#com_google_cloud_aiplatform_v1_GcsSource_Builder_addUris_java_lang_String_)(inputUri).build())
                          .[setInstancesFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_InputConfig_Builder_setInstancesFormat_java_lang_String_)("jsonl")
                          .build())
                  .setOutputConfig(
                      [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).OutputConfig.newBuilder()
                          .setGcsDestination([GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.html).newBuilder()
                              .[setOutputUriPrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination.Builder.html#com_google_cloud_aiplatform_v1_GcsDestination_Builder_setOutputUriPrefix_java_lang_String_)(outputUri).build())
                          .[setPredictionsFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.OutputConfig.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_OutputConfig_Builder_setPredictionsFormat_java_lang_String_)("jsonl")
                          .build())
                  .[setModelParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_Builder_setModelParameters_com_google_protobuf_Value_)(parameterValue)
                  .build();
    
          response = client.createBatchPredictionJob(parent, batchPredictionJob);
    
          System.out.format("response: %s\n", response);
          System.out.format("\tName: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_getName__)());
        }
        return response;
      }
    
      private static [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html) mapToValue(Map<String, String> map) throws [InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html) {
        Gson gson = new Gson();
        String json = gson.toJson(map);
        [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html).Builder builder = [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Value.html).newBuilder();
        [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(json, builder);
        return [builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree.html#com_google_protobuf_TextFormatParseInfoTree_builder__).build();
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
