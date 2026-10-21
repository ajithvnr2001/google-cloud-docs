---
url: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-delete-dataset-sample/
title: Delete a dataset \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:34:53.314858+00:00
---

# Delete a dataset  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-delete-dataset-sample/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/vertex-ai/docs/samples)



#  Delete a dataset Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a dataset using the delete_dataset method.

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
    )
    
    func deleteDataset(w io.Writer, projectID, location, datasetID string) error {
    	// projectID := "my-project"
    	// location := "us-central1"
    	// datasetID := "my-dataset"
    
    	apiEndpoint := fmt.Sprintf("%s-aiplatform.googleapis.com:443", location)
    	clientOption := option.WithEndpoint(apiEndpoint)
    
    	ctx := context.Background()
    	aiplatformService, err := aiplatform.[NewDatasetClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/aiplatform/latest/apiv1.html#cloud_google_com_go_aiplatform_apiv1_DatasetClient_NewDatasetClient)(ctx, clientOption)
    	if err != nil {
    		return err
    	}
    	defer aiplatformService.Close()
    
    	req := &aiplatformpb.DeleteDatasetRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/datasets/%s",
    			projectID, location, datasetID),
    	}
    
    	op, err := aiplatformService.DeleteDataset(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		return ctx.Err()
    	}
    
    	fmt.Fprintf(w, "Deleted dataset: %s\n", datasetID)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[DatasetName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetName.html);
    import com.google.cloud.aiplatform.v1.[DatasetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.html);
    import com.google.cloud.aiplatform.v1.[DatasetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteDatasetSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String datasetId = "YOUR_DATASET_ID";
        deleteDatasetSample(project, datasetId);
      }
    
      static void deleteDatasetSample(String project, String datasetId)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        [DatasetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceSettings.html) datasetServiceSettings =
            [DatasetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DatasetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.html) datasetServiceClient =
            [DatasetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.html).create(datasetServiceSettings)) {
          String location = "us-central1";
          [DatasetName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetName.html) datasetName = [DatasetName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetName.html).of(project, location, datasetId);
    
          OperationFuture<Empty, DeleteOperationMetadata> operationFuture =
              datasetServiceClient.[deleteDatasetAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceClient.html#com_google_cloud_aiplatform_v1_DatasetServiceClient_deleteDatasetAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_DatasetName_)(datasetName);
          System.out.format("Operation name: %s\n", operationFuture.getInitialFuture().get().getName());
          System.out.println("Waiting for operation to finish...");
          operationFuture.get(300, TimeUnit.SECONDS);
    
          System.out.format("Deleted Dataset.");
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
    
    // const datasetId = 'YOUR_DATASET_ID';
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    
    // Imports the Google Cloud Dataset Service Client library
    const {DatasetServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const datasetServiceClient = new [DatasetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function deleteDataset() {
      // Configure the resource
      const name = datasetServiceClient.datasetPath(project, location, datasetId);
      const request = {name};
    
      // Delete Dataset Request
      const [response] = await datasetServiceClient.deleteDataset(request);
      console.log(`Long running operation: ${response.name}`);
    
      // Wait for operation to complete
      await response.promise();
      const result = response.result;
    
      console.log('Delete dataset response:\n', result);
    }
    deleteDataset();

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import aiplatform
    
    
    def delete_dataset_sample(
        project: str,
        dataset_id: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
        timeout: int = 300,
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.[DatasetServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.dataset_service.DatasetServiceClient.html)(client_options=client_options)
        name = client.[dataset_path](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.dataset_service.DatasetServiceClient.html#google_cloud_aiplatform_v1_services_dataset_service_DatasetServiceClient_dataset_path)(project=project, location=location, dataset=dataset_id)
        response = client.[delete_dataset](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.services.dataset_service.DatasetServiceClient.html#google_cloud_aiplatform_v1_services_dataset_service_DatasetServiceClient_delete_dataset)(name=name)
        print("Long running operation:", response.operation.name)
        delete_dataset_response = response.result(timeout=timeout)
        print("delete_dataset_response:", delete_dataset_response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=aiplatform). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
