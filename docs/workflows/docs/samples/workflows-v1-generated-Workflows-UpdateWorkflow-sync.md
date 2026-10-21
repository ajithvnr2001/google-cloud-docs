---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-v1-generated-Workflows-UpdateWorkflow-sync/
title: Update a workflow using Python or Ruby \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:09.981961+00:00
---

# Update a workflow using Python or Ruby  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-v1-generated-Workflows-UpdateWorkflow-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Update a workflow using Python or Ruby Stay organized with collections  Save and categorize content based on your preferences. 

Updates a workflow using Python or Ruby.

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Workflows.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedWorkflowsClientSnippets
    {
        /// <summary>Snippet for UpdateWorkflow</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void UpdateWorkflowRequestObject()
        {
            // Create client
            [WorkflowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html) workflowsClient = [WorkflowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html#Google_Cloud_Workflows_V1_WorkflowsClient_Create)();
            // Initialize request argument(s)
            [UpdateWorkflowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.UpdateWorkflowRequest.html) request = new [UpdateWorkflowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.UpdateWorkflowRequest.html)
            {
                Workflow = new Workflow(),
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
            };
            // Make the request
            Operation<Workflow, OperationMetadata> response = workflowsClient.[UpdateWorkflow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html#Google_Cloud_Workflows_V1_WorkflowsClient_UpdateWorkflow_Google_Cloud_Workflows_V1_UpdateWorkflowRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<Workflow, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            Workflow result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Workflow, OperationMetadata> retrievedResponse = workflowsClient.[PollOnceUpdateWorkflow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html#Google_Cloud_Workflows_V1_WorkflowsClient_PollOnceUpdateWorkflow_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                Workflow retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Go API reference documentation](https://godoc.org/cloud.google.com/go/workflows/apiv1beta). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	workflows "cloud.google.com/go/workflows/apiv1"
    	workflowspb "cloud.google.com/go/workflows/apiv1/workflowspb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := workflows.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workflows/latest/apiv1.html#cloud_google_com_go_workflows_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/workflows/latest/apiv1.html#cloud_google_com_go_workflows_apiv1_Client_Close)()
    
    	req := &workflowspb.UpdateWorkflowRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workflows/apiv1/workflowspb#UpdateWorkflowRequest.
    	}
    	op, err := c.UpdateWorkflow(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/overview). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.workflows.v1.[UpdateWorkflowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.UpdateWorkflowRequest.html);
    import com.google.cloud.workflows.v1.[Workflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.Workflow.html);
    import com.google.cloud.workflows.v1.[WorkflowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    
    public class SyncUpdateWorkflow {
    
      public static void main(String[] args) throws Exception {
        syncUpdateWorkflow();
      }
    
      public static void syncUpdateWorkflow() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([WorkflowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html) workflowsClient = [WorkflowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html).create()) {
          [UpdateWorkflowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.UpdateWorkflowRequest.html) request =
              [UpdateWorkflowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.UpdateWorkflowRequest.html).newBuilder()
                  .setWorkflow([Workflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.Workflow.html).newBuilder().build())
                  .[setUpdateMask](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.UpdateWorkflowRequest.Builder.html#com_google_cloud_workflows_v1_UpdateWorkflowRequest_Builder_setUpdateMask_com_google_protobuf_FieldMask_)([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().build())
                  .build();
          [Workflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.Workflow.html) response = workflowsClient.[updateWorkflowAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html#com_google_cloud_workflows_v1_WorkflowsClient_updateWorkflowAsync_com_google_cloud_workflows_v1_UpdateWorkflowRequest_)(request).get();
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/workflows/latest). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [workflows](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.services.workflows.html)_v1
    
    
    def sample_update_workflow():
        # Create a client
        client = workflows_v1.[WorkflowsClient](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.services.workflows.WorkflowsClient.html)()
    
        # Initialize request argument(s)
        workflow = workflows_v1.[Workflow](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.types.Workflow.html)()
        workflow.source_contents = "source_contents_value"
    
        request = workflows_v1.[UpdateWorkflowRequest](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.types.UpdateWorkflowRequest.html)(
            workflow=workflow,
        )
    
        # Make the request
        operation = client.[update_workflow](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.services.workflows.WorkflowsClient.html#google_cloud_workflows_v1_services_workflows_WorkflowsClient_update_workflow)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows/latest). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/workflows/v1"
    
    ##
    # Snippet for the update_workflow call in the Workflows service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Workflows::V1::Workflows::Client#update_workflow.
    #
    def update_workflow
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Workflows::V1::Workflows::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Workflows::V1::UpdateWorkflowRequest.new
    
      # Call the update_workflow method.
      result = client.update_workflow request
    
      # The returned object is of type Gapic::Operation. You can use it to
      # check the status of an operation, cancel it, or wait for results.
      # Here is how to wait for a response.
      result.wait_until_done! timeout: 60
      if result.response?
        p result.response
      else
        puts "No response received."
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
