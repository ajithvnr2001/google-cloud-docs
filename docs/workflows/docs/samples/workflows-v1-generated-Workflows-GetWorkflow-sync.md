---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-v1-generated-Workflows-GetWorkflow-sync/
title: Get a workflow using Python or Ruby. \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:49.970448+00:00
---

# Get a workflow using Python or Ruby.  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-v1-generated-Workflows-GetWorkflow-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Get a workflow using Python or Ruby. Stay organized with collections  Save and categorize content based on your preferences. 

Gets a workflow using Python or Ruby.

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Workflows.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.html);
    using [Google.Cloud.Workflows.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.html);
    
    public sealed partial class GeneratedWorkflowsClientSnippets
    {
        /// <summary>Snippet for GetWorkflow</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void GetWorkflowRequestObject()
        {
            // Create client
            [WorkflowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html) workflowsClient = [WorkflowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html#Google_Cloud_Workflows_V1_WorkflowsClient_Create)();
            // Initialize request argument(s)
            [GetWorkflowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.GetWorkflowRequest.html) request = new [GetWorkflowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.GetWorkflowRequest.html)
            {
                WorkflowName = [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName.html).[FromProjectLocationWorkflow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName.html#Google_Cloud_Workflows_Common_V1_WorkflowName_FromProjectLocationWorkflow_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[WORKFLOW]"),
                RevisionId = "",
            };
            // Make the request
            Workflow response = workflowsClient.[GetWorkflow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html#Google_Cloud_Workflows_V1_WorkflowsClient_GetWorkflow_Google_Cloud_Workflows_Common_V1_WorkflowName_Google_Api_Gax_Grpc_CallSettings_)(request);
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
    
    	req := &workflowspb.GetWorkflowRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workflows/apiv1/workflowspb#GetWorkflowRequest.
    	}
    	resp, err := c.GetWorkflow(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/overview). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.workflows.v1.[GetWorkflowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.GetWorkflowRequest.html);
    import com.google.cloud.workflows.v1.[Workflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.Workflow.html);
    import com.google.cloud.workflows.v1.[WorkflowName](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowName.html);
    import com.google.cloud.workflows.v1.[WorkflowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html);
    
    public class SyncGetWorkflow {
    
      public static void main(String[] args) throws Exception {
        syncGetWorkflow();
      }
    
      public static void syncGetWorkflow() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([WorkflowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html) workflowsClient = [WorkflowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html).create()) {
          [GetWorkflowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.GetWorkflowRequest.html) request =
              [GetWorkflowRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.GetWorkflowRequest.html).newBuilder()
                  .setName([WorkflowName](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowName.html).of("[PROJECT]", "[LOCATION]", "[WORKFLOW]").toString())
                  .setRevisionId("revisionId-1507445162")
                  .build();
          [Workflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.Workflow.html) response = workflowsClient.getWorkflow(request);
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
    
    
    def sample_get_workflow():
        # Create a client
        client = workflows_v1.[WorkflowsClient](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.services.workflows.WorkflowsClient.html)()
    
        # Initialize request argument(s)
        request = workflows_v1.[GetWorkflowRequest](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.types.GetWorkflowRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_workflow](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.services.workflows.WorkflowsClient.html#google_cloud_workflows_v1_services_workflows_WorkflowsClient_get_workflow)(request=request)
    
        # Handle the response
        print(response)
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows/latest). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/workflows/v1"
    
    ##
    # Snippet for the get_workflow call in the Workflows service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Workflows::V1::Workflows::Client#get_workflow.
    #
    def get_workflow
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Workflows::V1::Workflows::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Workflows::V1::GetWorkflowRequest.new
    
      # Call the get_workflow method.
      result = client.get_workflow request
    
      # The returned object is of type Google::Cloud::Workflows::V1::Workflow.
      p result
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
