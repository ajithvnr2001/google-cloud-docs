---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-v1-generated-Workflows-DeleteWorkflow-sync/
title: Delete a workflow using Python or Ruby. \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:50.492612+00:00
---

# Delete a workflow using Python or Ruby.  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-v1-generated-Workflows-DeleteWorkflow-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Delete a workflow using Python or Ruby. Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a workflow using Python or Ruby.

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Workflows.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.html);
    using [Google.Cloud.Workflows.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedWorkflowsClientSnippets
    {
        /// <summary>Snippet for DeleteWorkflow</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void DeleteWorkflowRequestObject()
        {
            // Create client
            [WorkflowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html) workflowsClient = [WorkflowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html#Google_Cloud_Workflows_V1_WorkflowsClient_Create)();
            // Initialize request argument(s)
            [DeleteWorkflowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.DeleteWorkflowRequest.html) request = new [DeleteWorkflowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.DeleteWorkflowRequest.html)
            {
                WorkflowName = [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName.html).[FromProjectLocationWorkflow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName.html#Google_Cloud_Workflows_Common_V1_WorkflowName_FromProjectLocationWorkflow_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[WORKFLOW]"),
            };
            // Make the request
            Operation<Empty, OperationMetadata> response = workflowsClient.[DeleteWorkflow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html#Google_Cloud_Workflows_V1_WorkflowsClient_DeleteWorkflow_Google_Cloud_Workflows_Common_V1_WorkflowName_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Empty, OperationMetadata> retrievedResponse = workflowsClient.[PollOnceDeleteWorkflow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html#Google_Cloud_Workflows_V1_WorkflowsClient_PollOnceDeleteWorkflow_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) retrievedResult = retrievedResponse.Result;
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
    
    	req := &workflowspb.DeleteWorkflowRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workflows/apiv1/workflowspb#DeleteWorkflowRequest.
    	}
    	op, err := c.DeleteWorkflow(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/overview). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.workflows.v1.[DeleteWorkflowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.DeleteWorkflowRequest.html);
    import com.google.cloud.workflows.v1.[WorkflowName](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowName.html);
    import com.google.cloud.workflows.v1.[WorkflowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    
    public class SyncDeleteWorkflow {
    
      public static void main(String[] args) throws Exception {
        syncDeleteWorkflow();
      }
    
      public static void syncDeleteWorkflow() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([WorkflowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html) workflowsClient = [WorkflowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html).create()) {
          [DeleteWorkflowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.DeleteWorkflowRequest.html) request =
              [DeleteWorkflowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.DeleteWorkflowRequest.html).newBuilder()
                  .setName([WorkflowName](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowName.html).of("[PROJECT]", "[LOCATION]", "[WORKFLOW]").toString())
                  .build();
          workflowsClient.[deleteWorkflowAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html#com_google_cloud_workflows_v1_WorkflowsClient_deleteWorkflowAsync__org_jspecify_annotations_Nullable_com_google_cloud_workflows_v1_WorkflowName_)(request).get();
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
    from google.cloud import [workflows](https://docs.cloud.google.com/python/docs/reference/workflows/latest)_v1
    
    
    def sample_delete_workflow():
        # Create a client
        client = workflows_v1.[WorkflowsClient](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.services.workflows.WorkflowsClient.html)()
    
        # Initialize request argument(s)
        request = workflows_v1.[DeleteWorkflowRequest](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.types.DeleteWorkflowRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_workflow](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.services.workflows.WorkflowsClient.html#google_cloud_workflows_v1_services_workflows_WorkflowsClient_delete_workflow)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows/latest). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/workflows/v1"
    
    ##
    # Snippet for the delete_workflow call in the Workflows service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Workflows::V1::Workflows::Client#delete_workflow.
    #
    def delete_workflow
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Workflows::V1::Workflows::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Workflows::V1::DeleteWorkflowRequest.new
    
      # Call the delete_workflow method.
      result = client.delete_workflow request
    
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
