---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-TemplatesService-GetTemplate-async/
title: Get a template (async) \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:08.195830+00:00
---

# Get a template (async)  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-TemplatesService-GetTemplate-async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Get a template (async) Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to get metadata and runtime metadata about a template.

## Code sample

### C#

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataflow.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.html);
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedTemplatesServiceClientSnippets
    {
        /// <summary>Snippet for GetTemplateAsync</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task GetTemplateRequestObjectAsync()
        {
            // Create client
            [TemplatesServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.TemplatesServiceClient.html) templatesServiceClient = await [TemplatesServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.TemplatesServiceClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.TemplatesServiceClient.html#Google_Cloud_Dataflow_V1Beta3_TemplatesServiceClient_CreateAsync_System_Threading_CancellationToken_)();
            // Initialize request argument(s)
            [GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetTemplateRequest.html) request = new [GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetTemplateRequest.html)
            {
                ProjectId = "",
                GcsPath = "",
                View = [GetTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetTemplateRequest.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetTemplateRequest.Types.html).[TemplateView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetTemplateRequest.Types.TemplateView.html).[MetadataOnly](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetTemplateRequest.Types.TemplateView.html#Google_Cloud_Dataflow_V1Beta3_GetTemplateRequest_Types_TemplateView_MetadataOnly),
                Location = "",
            };
            // Make the request
            [GetTemplateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetTemplateResponse.html) response = await templatesServiceClient.[GetTemplateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.TemplatesServiceClient.html#Google_Cloud_Dataflow_V1Beta3_TemplatesServiceClient_GetTemplateAsync_Google_Cloud_Dataflow_V1Beta3_GetTemplateRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.dataflow.v1beta3.GetTemplateRequest;
    import com.google.dataflow.v1beta3.GetTemplateResponse;
    import com.google.dataflow.v1beta3.TemplatesServiceClient;
    
    public class AsyncGetTemplate {
    
      public static void main(String[] args) throws Exception {
        asyncGetTemplate();
      }
    
      public static void asyncGetTemplate() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (TemplatesServiceClient templatesServiceClient = TemplatesServiceClient.[create](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html#com_google_api_core_SettableApiFuture__V_create__)()) {
          GetTemplateRequest request =
              GetTemplateRequest.newBuilder()
                  .setProjectId("projectId-894832108")
                  .setLocation("location1901043637")
                  .build();
          ApiFuture<GetTemplateResponse> future =
              templatesServiceClient.getTemplateCallable().futureCall(request);
          // Do something.
          GetTemplateResponse response = future.get();
        }
      }
    }

### Node.js

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The ID of the Cloud Platform project that the job belongs to.
     */
    // const projectId = 'abc123'
    /**
     *  Required. A Cloud Storage path to the template from which to
     *  create the job.
     *  Must be valid Cloud Storage URL, beginning with 'gs://'.
     */
    // const gcsPath = 'abc123'
    /**
     *  The view to retrieve. Defaults to METADATA_ONLY.
     */
    // const view = {}
    /**
     *  The regional endpoint 
     *  (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) to
     *  which to direct the request.
     */
    // const location = 'abc123'
    
    // Imports the Dataflow library
    const {TemplatesServiceClient} = require('[@google-cloud/dataflow](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)').v1beta3;
    
    // Instantiates a client
    const dataflowClient = new [TemplatesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)();
    
    async function callGetTemplate() {
      // Construct request
      const request = {
      };
    
      // Run request
      const response = await dataflowClient.getTemplate(request);
      console.log(response);
    }
    
    callGetTemplate();

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
    
    
    async def sample_get_template():
        # Create a client
        client = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[TemplatesServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.templates_service.TemplatesServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[GetTemplateRequest](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.types.GetTemplateRequest.html)(
            gcs_path="gcs_path_value",
        )
    
        # Make the request
        response = await client.[get_template](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.templates_service.TemplatesServiceAsyncClient.html#google_cloud_dataflow_v1beta3_services_templates_service_TemplatesServiceAsyncClient_get_template)(request=request)
    
        # Handle the response
        print(response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
