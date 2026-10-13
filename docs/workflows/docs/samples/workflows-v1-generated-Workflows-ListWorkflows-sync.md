---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-v1-generated-Workflows-ListWorkflows-sync/
title: List workflows using Python or Ruby \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:39.795152+00:00
---

# List workflows using Python or Ruby  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-v1-generated-Workflows-ListWorkflows-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  List workflows using Python or Ruby Stay organized with collections  Save and categorize content based on your preferences. 

Lists workflows using Python or Ruby.

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Workflows.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.html);
    using System;
    
    public sealed partial class GeneratedWorkflowsClientSnippets
    {
        /// <summary>Snippet for ListWorkflows</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void ListWorkflowsRequestObject()
        {
            // Create client
            [WorkflowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html) workflowsClient = [WorkflowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html#Google_Cloud_Workflows_V1_WorkflowsClient_Create)();
            // Initialize request argument(s)
            [ListWorkflowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.ListWorkflowsRequest.html) request = new [ListWorkflowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.ListWorkflowsRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                Filter = "",
                OrderBy = "",
            };
            // Make the request
            PagedEnumerable<ListWorkflowsResponse, Workflow> response = workflowsClient.[ListWorkflows](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.WorkflowsClient.html#Google_Cloud_Workflows_V1_WorkflowsClient_ListWorkflows_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Iterate over all response items, lazily performing RPCs as required
            foreach (Workflow item in response)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
    
            // Or iterate over pages (of server-defined size), performing one RPC per page
            foreach ([ListWorkflowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.V1/latest/Google.Cloud.Workflows.V1.ListWorkflowsResponse.html) page in response.AsRawResponses())
            {
                // Do something with each page of items
                Console.WriteLine("A page of results:");
                foreach (Workflow item in page)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
            }
    
            // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
            int pageSize = 10;
            Page<Workflow> singlePage = response.ReadPage(pageSize);
            // Do something with the page of items
            Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
            foreach (Workflow item in singlePage)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
            // Store the pageToken, for when the next page is required.
            string nextPageToken = singlePage.NextPageToken;
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
    	"google.golang.org/api/iterator"
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
    
    	req := &workflowspb.ListWorkflowsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/workflows/apiv1/workflowspb#ListWorkflowsRequest.
    	}
    	it := c.ListWorkflows(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*workflowspb.ListWorkflowsResponse)
    	}
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/overview). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.workflows.v1.[ListWorkflowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.ListWorkflowsRequest.html);
    import com.google.cloud.workflows.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.LocationName.html);
    import com.google.cloud.workflows.v1.[Workflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.Workflow.html);
    import com.google.cloud.workflows.v1.[WorkflowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html);
    
    public class SyncListWorkflows {
    
      public static void main(String[] args) throws Exception {
        syncListWorkflows();
      }
    
      public static void syncListWorkflows() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([WorkflowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html) workflowsClient = [WorkflowsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.WorkflowsClient.html).create()) {
          [ListWorkflowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.ListWorkflowsRequest.html) request =
              [ListWorkflowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.ListWorkflowsRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .setPageSize(883849137)
                  .setPageToken("pageToken873572522")
                  .[setFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.ListWorkflowsRequest.Builder.html#com_google_cloud_workflows_v1_ListWorkflowsRequest_Builder_setFilter_java_lang_String_)("filter-1274492040")
                  .[setOrderBy](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.ListWorkflowsRequest.Builder.html#com_google_cloud_workflows_v1_ListWorkflowsRequest_Builder_setOrderBy_java_lang_String_)("orderBy-1207110587")
                  .build();
          for ([Workflow](https://docs.cloud.google.com/java/docs/reference/google-cloud-workflows/latest/com.google.cloud.workflows.v1.Workflow.html) element : workflowsClient.listWorkflows(request).iterateAll()) {
            // doThingsWith(element);
          }
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
    
    
    def sample_list_workflows():
        # Create a client
        client = workflows_v1.[WorkflowsClient](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.services.workflows.WorkflowsClient.html)()
    
        # Initialize request argument(s)
        request = workflows_v1.[ListWorkflowsRequest](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.types.ListWorkflowsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_workflows](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows_v1.services.workflows.WorkflowsClient.html#google_cloud_workflows_v1_services_workflows_WorkflowsClient_list_workflows)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Workflows quickstart using client libraries](https://docs.cloud.google.com/workflows/docs/quickstart-client-libraries). For more information, see the [Workflows Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows/latest). 

To authenticate to Workflows, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/workflows/v1"
    
    ##
    # Snippet for the list_workflows call in the Workflows service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Workflows::V1::Workflows::Client#list_workflows.
    #
    def list_workflows
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Workflows::V1::Workflows::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Workflows::V1::ListWorkflowsRequest.new
    
      # Call the list_workflows method.
      result = client.list_workflows request
    
      # The returned object is of type Gapic::PagedEnumerable. You can iterate
      # over elements, and API calls will be issued to fetch pages as needed.
      result.each do |item|
        # Each element is of type ::Google::Cloud::Workflows::V1::Workflow.
        p item
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
