---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-batch-predict-gemini-createjob/
title: Batch text prediction with Gemini model \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:53.329001+00:00
---

# Batch text prediction with Gemini model  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-batch-predict-gemini-createjob/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Batch text prediction with Gemini model Stay organized with collections  Save and categorize content based on your preferences. 

Perform batch text prediction using Gemini model and returns the output location.

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
    
    // batchPredictGCS submits a batch prediction job using GCS data source as its input
    func batchPredictGCS(w io.Writer, projectID, location string, inputURIs []string, outputURI string) error {
    	// location := "us-central1"
    	// inputURIs := []string{"gs://cloud-samples-data/batch/prompt_for_batch_gemini_predict.jsonl"}
    	// outputURI := "gs://<cloud-bucket-name>/<prefix-name>"
    	modelName := "gemini-2.5-flash"
    	jobName := "batch-predict-gcs-test-001"
    
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
    				Source: &aiplatformpb.BatchPredictionJob_InputConfig_GcsSource{
    					GcsSource: &aiplatformpb.GcsSource{
    						Uris: inputURIs,
    					},
    				},
    				InstancesFormat: "jsonl",
    			},
    			OutputConfig: &aiplatformpb.BatchPredictionJob_OutputConfig{
    				Destination: &aiplatformpb.BatchPredictionJob_OutputConfig_GcsDestination{
    					GcsDestination: &aiplatformpb.GcsDestination{
    						OutputUriPrefix: outputURI,
    					},
    				},
    				PredictionsFormat: "jsonl",
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
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
