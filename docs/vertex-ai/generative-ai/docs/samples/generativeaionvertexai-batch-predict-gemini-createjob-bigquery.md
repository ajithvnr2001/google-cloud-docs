---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-batch-predict-gemini-createjob-bigquery/
title: Batch Predict with Gemini using BigQuery data \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:08.418525+00:00
---

# Batch Predict with Gemini using BigQuery data  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-batch-predict-gemini-createjob-bigquery/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Batch Predict with Gemini using BigQuery data Stay organized with collections  Save and categorize content based on your preferences. 

Perform batch text prediction with Gemini using BigQuery data source as input.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get batch predictions for Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/batch-prediction-api)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	aiplatform "cloud.google.com/go/aiplatform/apiv1"
    	aiplatformpb "cloud.google.com/go/aiplatform/apiv1/aiplatformpb"
    
    	"google.golang.org/api/option"
    	"google.golang.org/protobuf/types/known/structpb"
    )
    
    // batchPredictBQ submits a batch prediction job using BigQuery data source as its input
    func batchPredictBQ(w io.Writer, projectID, location string, inputURI string, outputURI string) error {
    	// location  := "us-central1"
    	// inputURI  := "bq://storage-samples.generative_ai.batch_requests_for_multimodal_input"
    	// outputURI := "bq://<cloud-project-name>.<dataset-name>.<table-name>"
    	modelName := "gemini-2.5-flash"
    	jobName := "batch-predict-bq-test-001"
    
    	ctx := context.Background()
    	apiEndpoint := fmt.Sprintf("%s-aiplatform.googleapis.com:443", location)
    	client, err := aiplatform.[NewJobClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1.html#cloud_google_com_go_aiplatform_apiv1_JobClient_NewJobClient)(ctx, option.WithEndpoint(apiEndpoint))
    	if err != nil {
    		return fmt.Errorf("unable to create aiplatform client: %w", err)
    	}
    	defer client.Close()
    
    	modelParameters, err := structpb.NewValue(map[string]interface{}{
    		"temperature":     0.2,
    		"maxOutputTokens": 200,
    	})
    	if err != nil {
    		return fmt.Errorf("unable to convert model parameters to protobuf value: %w", err)
    	}
    
    	req := &aiplatformpb.CreateBatchPredictionJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		BatchPredictionJob: &aiplatformpb.BatchPredictionJob{
    			DisplayName:     jobName,
    			Model:           fmt.Sprintf("publishers/google/models/%s", modelName),
    			ModelParameters: modelParameters,
    			// Check the API reference for `BatchPredictionJob` for supported input and output formats:
    			// https://cloud.google.com/vertex-ai/docs/reference/rpc/google.cloud.aiplatform.v1#google.cloud.aiplatform.v1.BatchPredictionJob
    			InputConfig: &aiplatformpb.BatchPredictionJob_InputConfig{
    				Source: &aiplatformpb.BatchPredictionJob_InputConfig_BigquerySource{
    					BigquerySource: &aiplatformpb.BigQuerySource{
    						InputUri: inputURI,
    					},
    				},
    				InstancesFormat: "bigquery",
    			},
    
    			OutputConfig: &aiplatformpb.BatchPredictionJob_OutputConfig{
    				Destination: &aiplatformpb.BatchPredictionJob_OutputConfig_BigqueryDestination{
    					BigqueryDestination: &aiplatformpb.BigQueryDestination{
    						OutputUri: outputURI,
    					},
    				},
    				PredictionsFormat: "bigquery",
    			},
    		},
    	}
    
    	job, err := client.CreateBatchPredictionJob(ctx, req)
    	if err != nil {
    		return err
    	}
    	fullJobId := job.GetName()
    	fmt.Fprintf(w, "submitted batch predict job for model %q\n", job.GetModel())
    	fmt.Fprintf(w, "job id: %q\n", fullJobId)
    	fmt.Fprintf(w, "job state: %s\n", job.GetState())
    	// Example response:
    	// submitted batch predict job for model "publishers/google/models/gemini-2.0-flash-001"
    	// job id: "projects/.../locations/.../batchPredictionJobs/1234567890000000000"
    	// job state: JOB_STATE_PENDING
    
    	for {
    		time.Sleep(5 * time.Second)
    
    		job, err := client.GetBatchPredictionJob(ctx, &aiplatformpb.GetBatchPredictionJobRequest{
    			Name: fullJobId,
    		})
    		if err != nil {
    			return fmt.Errorf("error: couldn't get updated job state: %w", err)
    		}
    
    		if job.GetEndTime() != nil {
    			fmt.Fprintf(w, "batch predict job finished with state %s\n", job.GetState())
    			break
    		} else {
    			fmt.Fprintf(w, "batch predict job is running... job state is %s\n", job.GetState())
    		}
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html);
    import com.google.cloud.aiplatform.v1.[BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html);
    import com.google.cloud.aiplatform.v1.[BigQuerySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQuerySource.html);
    import com.google.cloud.aiplatform.v1.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html);
    import com.google.cloud.aiplatform.v1.[JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import java.io.IOException;
    
    public class CreateBatchPredictionGeminiBigqueryJobSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Update these variables before running the sample.
        String project = "PROJECT_ID";
        String bigqueryDestinationOutputUri = "bq://PROJECT_ID.MY_DATASET.MY_TABLE";
    
        createBatchPredictionGeminiBigqueryJobSample(project, bigqueryDestinationOutputUri);
      }
    
      // Create a batch prediction job using BigQuery input and output datasets.
      public static [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) createBatchPredictionGeminiBigqueryJobSample(
          String project, String bigqueryDestinationOutputUri) throws IOException {
        String location = "us-central1";
        [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html) settings =
            [JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings.html).newBuilder()
                .setEndpoint(String.format("%s-aiplatform.googleapis.com:443", location))
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html) client = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.html).create(settings)) {
          [BigQuerySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQuerySource.html) bigquerySource =
              [BigQuerySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQuerySource.html).newBuilder()
                  .[setInputUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQuerySource.Builder.html#com_google_cloud_aiplatform_v1_BigQuerySource_Builder_setInputUri_java_lang_String_)("bq://storage-samples.generative_ai.batch_requests_for_multimodal_input")
                  .build();
          [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.html) inputConfig =
              [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).InputConfig.newBuilder()
                  .[setInstancesFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.InputConfig.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_InputConfig_Builder_setInstancesFormat_java_lang_String_)("bigquery")
                  .setBigquerySource(bigquerySource)
                  .build();
          [BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html) bigqueryDestination =
              [BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html).newBuilder().setOutputUri(bigqueryDestinationOutputUri).build();
          [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).[OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.OutputConfig.html) outputConfig =
              [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).OutputConfig.newBuilder()
                  .[setPredictionsFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.OutputConfig.Builder.html#com_google_cloud_aiplatform_v1_BatchPredictionJob_OutputConfig_Builder_setPredictionsFormat_java_lang_String_)("bigquery")
                  .setBigqueryDestination(bigqueryDestination)
                  .build();
          String modelName =
              String.format(
                  "projects/%s/locations/%s/publishers/google/models/%s",
                  project, location, "gemini-2.5-flash");
    
          [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html) batchPredictionJob =
              [BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob.html).newBuilder()
                  .setDisplayName("my-display-name")
                  .setModel(modelName) // Add model parameters per request in the input BigQuery table.
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
    // URI of the output BigQuery table.
    // E.g. "bq://[PROJECT].[DATASET].[TABLE]"
    // outputUri = 'bq://projectid.dataset.table';
    
    // URI of the multimodal input BigQuery table.
    // E.g. "bq://[PROJECT].[DATASET].[TABLE]"
    const inputUri =
      'bq://storage-samples.generative_ai.batch_requests_for_multimodal_input';
    const location = 'us-central1';
    const parent = `projects/${projectId}/locations/${location}`;
    const modelName = `${parent}/publishers/google/models/gemini-2.5-flash`;
    
    // Specify the location of the api endpoint.
    const clientOptions = {
      apiEndpoint: `${location}-aiplatform.googleapis.com`,
    };
    
    // Instantiate the client.
    const jobServiceClient = new aiplatformLib.[JobServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    // Create a Gemini batch prediction job using BigQuery input and output datasets.
    async function create_batch_prediction_gemini_bq() {
      const bqSource = new aiplatform.BigQuerySource({
        inputUri: inputUri,
      });
    
      const inputConfig = new aiplatform.BatchPredictionJob.InputConfig({
        bigquerySource: bqSource,
        instancesFormat: 'bigquery',
      });
    
      const bqDestination = new aiplatform.BigQueryDestination({
        outputUri: outputUri,
      });
    
      const outputConfig = new aiplatform.BatchPredictionJob.OutputConfig({
        bigqueryDestination: bqDestination,
        predictionsFormat: 'bigquery',
      });
    
      const batchPredictionJob = new aiplatform.BatchPredictionJob({
        displayName: 'Batch predict with Gemini - BigQuery',
        model: modelName, // Add model parameters per request in the input BigQuery table.
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
    
    await create_batch_prediction_gemini_bq();

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
