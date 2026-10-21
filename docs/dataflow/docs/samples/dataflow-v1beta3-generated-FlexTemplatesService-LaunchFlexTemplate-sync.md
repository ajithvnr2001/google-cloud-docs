---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-FlexTemplatesService-LaunchFlexTemplate-sync/
title: Launch a Flex Template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:10.287933+00:00
---

# Launch a Flex Template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-FlexTemplatesService-LaunchFlexTemplate-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Launch a Flex Template Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to launch a Flex Template.

## Code sample

### C#

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataflow.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.html);
    
    public sealed partial class GeneratedFlexTemplatesServiceClientSnippets
    {
        /// <summary>Snippet for LaunchFlexTemplate</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void LaunchFlexTemplateRequestObject()
        {
            // Create client
            [FlexTemplatesServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.FlexTemplatesServiceClient.html) flexTemplatesServiceClient = [FlexTemplatesServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.FlexTemplatesServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.FlexTemplatesServiceClient.html#Google_Cloud_Dataflow_V1Beta3_FlexTemplatesServiceClient_Create)();
            // Initialize request argument(s)
            [LaunchFlexTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.LaunchFlexTemplateRequest.html) request = new [LaunchFlexTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.LaunchFlexTemplateRequest.html)
            {
                ProjectId = "",
                LaunchParameter = new [LaunchFlexTemplateParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.LaunchFlexTemplateParameter.html)(),
                Location = "",
                ValidateOnly = false,
            };
            // Make the request
            [LaunchFlexTemplateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.LaunchFlexTemplateResponse.html) response = flexTemplatesServiceClient.[LaunchFlexTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.FlexTemplatesServiceClient.html#Google_Cloud_Dataflow_V1Beta3_FlexTemplatesServiceClient_LaunchFlexTemplate_Google_Cloud_Dataflow_V1Beta3_LaunchFlexTemplateRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataflow "cloud.google.com/go/dataflow/apiv1beta3"
    	dataflowpb "cloud.google.com/go/dataflow/apiv1beta3/dataflowpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataflow.[NewFlexTemplatesClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataflow/latest/apiv1beta3.html#cloud_google_com_go_dataflow_apiv1beta3_FlexTemplatesClient_NewFlexTemplatesClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataflowpb.LaunchFlexTemplateRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataflow/apiv1beta3/dataflowpb#LaunchFlexTemplateRequest.
    	}
    	resp, err := c.LaunchFlexTemplate(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.dataflow.v1beta3.FlexTemplatesServiceClient;
    import com.google.dataflow.v1beta3.LaunchFlexTemplateParameter;
    import com.google.dataflow.v1beta3.LaunchFlexTemplateRequest;
    import com.google.dataflow.v1beta3.LaunchFlexTemplateResponse;
    
    public class SyncLaunchFlexTemplate {
    
      public static void main(String[] args) throws Exception {
        syncLaunchFlexTemplate();
      }
    
      public static void syncLaunchFlexTemplate() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (FlexTemplatesServiceClient flexTemplatesServiceClient =
            FlexTemplatesServiceClient.create()) {
          LaunchFlexTemplateRequest request =
              LaunchFlexTemplateRequest.newBuilder()
                  .setProjectId("projectId-894832108")
                  .setLaunchParameter(LaunchFlexTemplateParameter.newBuilder().build())
                  .setLocation("location1901043637")
                  .setValidateOnly(true)
                  .build();
          LaunchFlexTemplateResponse response = flexTemplatesServiceClient.launchFlexTemplate(request);
        }
      }
    }

### Python

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest)
    
    
    def sample_launch_flex_template():
        # Create a client
        client = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[FlexTemplatesServiceClient](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.flex_templates_service.FlexTemplatesServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[LaunchFlexTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.types.LaunchFlexTemplateRequest.html)()
    
        # Make the request
        response = client.[launch_flex_template](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.flex_templates_service.FlexTemplatesServiceClient.html#google_cloud_dataflow_v1beta3_services_flex_templates_service_FlexTemplatesServiceClient_launch_flex_template)(request=request)
    
        # Handle the response
        print(response)
    
    

### Ruby

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataflow/v1beta3"
    
    ##
    # Snippet for the launch_flex_template call in the FlexTemplatesService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client#launch_flex_template.
    #
    def launch_flex_template
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataflow::V1beta3::FlexTemplatesService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateRequest.new
    
      # Call the launch_flex_template method.
      result = client.launch_flex_template request
    
      # The returned object is of type Google::Cloud::Dataflow::V1beta3::LaunchFlexTemplateResponse.
      p result
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
