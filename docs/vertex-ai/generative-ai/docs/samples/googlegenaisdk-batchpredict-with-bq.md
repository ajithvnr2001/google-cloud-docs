---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-batchpredict-with-bq/
title: Batch Predict with Gemini using BigQuery data \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:25.384954+00:00
---

# Batch Predict with Gemini using BigQuery data  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-batchpredict-with-bq/

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

  * [Batch inference for BigQuery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference/new-job-from-bigquery)
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
    
    	"google.golang.org/genai"
    )
    
    // generateBatchPredictWithBQ shows how to run a batch prediction job with BigQuery input/output.
    func generateBatchPredictWithBQ(w io.Writer, outputURI string) error {
    	// outputURI = "bq://your-project.your_dataset.your_table"
    	ctx := context.Background()
    
    	client, err := genai.NewClient(ctx, &genai.ClientConfig{
    		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create genai client: %w", err)
    	}
    
    	// BigQuery input
    	src := &genai.BatchJobSource{
    		Format:      "bigquery",
    		BigqueryURI: "bq://storage-samples.generative_ai.batch_requests_for_multimodal_input",
    	}
    
    	// BigQuery output
    	config := &genai.CreateBatchJobConfig{
    		Dest: &genai.BatchJobDestination{
    			Format:      "bigquery",
    			BigqueryURI: outputURI,
    		},
    	}
    
    	// To use a tuned model, set the model param to your tuned model using the following format:
    	//  modelName:= "projects/{PROJECT_ID}/locations/{LOCATION}/models/{MODEL_ID}
    	modelName := "gemini-2.5-flash"
    	job, err := client.Batches.Create(ctx, modelName, src, config)
    	if err != nil {
    		return fmt.Errorf("failed to create batch job: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job name: %s\n", job.Name)
    	fmt.Fprintf(w, "Job state: %s\n", job.State)
    	// Example response:
    	//  Job name: projects/{PROJECT_ID}/locations/us-central1/batchPredictionJobs/9876453210000000000
    	//  Job state: JOB_STATE_PENDING
    
    	// See the documentation: https://pkg.go.dev/google.golang.org/genai#BatchJob
    	completedStates := map[genai.JobState]bool{
    		genai.JobStateSucceeded: true,
    		genai.JobStateFailed:    true,
    		genai.JobStateCancelled: true,
    		genai.JobStatePaused:    true,
    	}
    
    	for !completedStates[job.State] {
    		time.Sleep(30 * time.Second)
    		job, err = client.Batches.Get(ctx, job.Name, nil)
    		if err != nil {
    			return fmt.Errorf("failed to get batch job: %w", err)
    		}
    		fmt.Fprintf(w, "Job state: %s\n", job.State)
    	}
    
    	// Example response:
    	//  Job state: JOB_STATE_PENDING
    	//  Job state: JOB_STATE_RUNNING
    	//  Job state: JOB_STATE_RUNNING
    	//  ...
    	//  Job state: JOB_STATE_SUCCEEDED
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import static com.google.genai.types.JobState.Known.JOB_STATE_CANCELLED;
    import static com.google.genai.types.JobState.Known.JOB_STATE_FAILED;
    import static com.google.genai.types.JobState.Known.JOB_STATE_PAUSED;
    import static com.google.genai.types.JobState.Known.JOB_STATE_SUCCEEDED;
    
    import com.google.genai.Client;
    import com.google.genai.types.BatchJob;
    import com.google.genai.types.BatchJobDestination;
    import com.google.genai.types.BatchJobSource;
    import com.google.genai.types.CreateBatchJobConfig;
    import com.google.genai.types.GetBatchJobConfig;
    import com.google.genai.types.HttpOptions;
    import com.google.genai.types.JobState;
    import java.util.EnumSet;
    import java.util.Set;
    import java.util.concurrent.TimeUnit;
    
    public class BatchPredictionWithBq {
    
      public static void main(String[] args) throws InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // To use a tuned model, set the model param to your tuned model using the following format:
        // modelId = "projects/{PROJECT_ID}/locations/{LOCATION}/models/{MODEL_ID}
        String modelId = "gemini-2.5-flash";
        String outputUri = "bq://your-project.your_dataset.your_table";
        createBatchJob(modelId, outputUri);
      }
    
      // Creates a batch prediction job with Google BigQuery.
      public static JobState createBatchJob(String modelId, String outputUri)
          throws InterruptedException {
        // Client Initialization. Once created, it can be reused for multiple requests.
        try (Client client =
            Client.builder()
                .location("us-central1")
                .vertexAI(true)
                .httpOptions(HttpOptions.builder().apiVersion("v1").build())
                .build()) {
    
          // See the documentation:
          // https://googleapis.github.io/java-genai/javadoc/com/google/genai/Batches.html
          BatchJobSource batchJobSource =
              BatchJobSource.builder()
                  .bigqueryUri("bq://storage-samples.generative_ai.batch_requests_for_multimodal_input")
                  .format("bigquery")
                  .build();
    
          CreateBatchJobConfig batchJobConfig =
              CreateBatchJobConfig.builder()
                  .displayName("your-display-name")
                  .dest(BatchJobDestination.builder().bigqueryUri(outputUri).format("bigquery").build())
                  .build();
    
          BatchJob batchJob = client.batches.create(modelId, batchJobSource, batchJobConfig);
    
          String jobName =
              batchJob.name().orElseThrow(() -> new IllegalStateException("Missing job name"));
          JobState jobState =
              batchJob.state().orElseThrow(() -> new IllegalStateException("Missing job state"));
          System.out.println("Job name: " + jobName);
          System.out.println("Job state: " + jobState);
          // Job name:
          // projects/.../locations/.../batchPredictionJobs/3189981423167602688
          // Job state: JOB_STATE_PENDING
    
          // See the documentation:
          // https://googleapis.github.io/java-genai/javadoc/com/google/genai/types/BatchJob.html
          Set<JobState.Known> completedStates =
              EnumSet.of(JOB_STATE_SUCCEEDED, JOB_STATE_FAILED, JOB_STATE_CANCELLED, JOB_STATE_PAUSED);
    
          while (!completedStates.contains(jobState.knownEnum())) {
            TimeUnit.SECONDS.sleep(30);
            batchJob = client.batches.get(jobName, GetBatchJobConfig.builder().build());
            jobState =
                batchJob
                    .state()
                    .orElseThrow(() -> new IllegalStateException("Missing job state during polling"));
            System.out.println("Job state: " + jobState);
          }
          // Example response:
          // Job state: JOB_STATE_QUEUED
          // Job state: JOB_STATE_RUNNING
          // Job state: JOB_STATE_RUNNING
          // ...
          // Job state: JOB_STATE_SUCCEEDED
          return jobState;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const {GoogleGenAI} = require('@google/genai');
    
    const GOOGLE_CLOUD_PROJECT = process.env.GOOGLE_CLOUD_PROJECT;
    const GOOGLE_CLOUD_LOCATION =
      process.env.GOOGLE_CLOUD_LOCATION || 'us-central1';
    const OUTPUT_URI = 'bq://your-project.your_dataset.your_table';
    
    async function runBatchPredictionJob(
      outputUri = OUTPUT_URI,
      projectId = GOOGLE_CLOUD_PROJECT,
      location = GOOGLE_CLOUD_LOCATION
    ) {
      const client = new GoogleGenAI({
        vertexai: true,
        project: projectId,
        location: location,
        httpOptions: {
          apiVersion: 'v1',
        },
      });
    
      // See the documentation: https://googleapis.github.io/js-genai/release_docs/classes/batches.Batches.html
      let job = await client.batches.create({
        // To use a tuned model, set the model param to your tuned model using the following format:
        // model="projects/{PROJECT_ID}/locations/{LOCATION}/models/{MODEL_ID}"
        model: 'gemini-2.5-flash',
        src: 'bq://storage-samples.generative_ai.batch_requests_for_multimodal_input',
        config: {
          dest: outputUri,
        },
      });
    
      console.log(`Job name: ${job.name}`);
      console.log(`Job state: ${job.state}`);
    
      // Example response:
      //  Job name: projects/%PROJECT_ID%/locations/us-central1/batchPredictionJobs/9876453210000000000
      //  Job state: JOB_STATE_PENDING
    
      const completedStates = new Set([
        'JOB_STATE_SUCCEEDED',
        'JOB_STATE_FAILED',
        'JOB_STATE_CANCELLED',
        'JOB_STATE_PAUSED',
      ]);
    
      while (!completedStates.has(job.state)) {
        await new Promise(resolve => setTimeout(resolve, 30000));
        job = await client.batches.get({name: job.name});
        console.log(`Job state: ${job.state}`);
      }
    
      // Example response:
      //  Job state: JOB_STATE_PENDING
      //  Job state: JOB_STATE_RUNNING
      //  Job state: JOB_STATE_RUNNING
      //  ...
      //  Job state: JOB_STATE_SUCCEEDED
    
      return job.state;
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    
    from google import genai
    from google.genai.types import CreateBatchJobConfig, HttpOptions, JobState
    
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    
    # TODO(developer): Update and un-comment below line
    # output_uri = f"bq://your-project.your_dataset.your_table"
    
    job = client.batches.create(
        # To use a tuned model, set the model param to your tuned model using the following format:
        # model="projects/{PROJECT_ID}/locations/{LOCATION}/models/{MODEL_ID}
        model="gemini-3.5-flash",
        src="bq://storage-samples.generative_ai.batch_requests_for_multimodal_input",
        config=CreateBatchJobConfig(dest=output_uri),
    )
    print(f"Job name: {job.name}")
    print(f"Job state: {job.state}")
    # Example response:
    # Job name: projects/.../locations/.../batchPredictionJobs/9876453210000000000
    # Job state: JOB_STATE_PENDING
    
    # See the documentation: https://googleapis.github.io/python-genai/genai.html#genai.types.BatchJob
    completed_states = {
        JobState.JOB_STATE_SUCCEEDED,
        JobState.JOB_STATE_FAILED,
        JobState.JOB_STATE_CANCELLED,
        JobState.JOB_STATE_PAUSED,
    }
    
    while job.state not in completed_states:
        time.sleep(30)
        job = client.batches.get(name=job.name)
        print(f"Job state: {job.state}")
    # Example response:
    # Job state: JOB_STATE_PENDING
    # Job state: JOB_STATE_RUNNING
    # Job state: JOB_STATE_RUNNING
    # ...
    # Job state: JOB_STATE_SUCCEEDED

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
