---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetStageExecutionDetails-async/
title: Get stage execution details (async) \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:09.394446+00:00
---

# Get stage execution details (async)  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetStageExecutionDetails-async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Get stage execution details (async) Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to get information about the workers and work items within a stage.

## Code sample

### C#

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.Dataflow.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedMetricsV1Beta3ClientSnippets
    {
        /// <summary>Snippet for GetStageExecutionDetailsAsync</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task GetStageExecutionDetailsRequestObjectAsync()
        {
            // Create client
            [MetricsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html) metricsV1Beta3Client = await [MetricsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_CreateAsync_System_Threading_CancellationToken_)();
            // Initialize request argument(s)
            [GetStageExecutionDetailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetStageExecutionDetailsRequest.html) request = new [GetStageExecutionDetailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetStageExecutionDetailsRequest.html)
            {
                ProjectId = "",
                JobId = "",
                Location = "",
                StageId = "",
                StartTime = new [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)(),
                EndTime = new [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)(),
            };
            // Make the request
            PagedAsyncEnumerable<StageExecutionDetails, WorkerDetails> response = metricsV1Beta3Client.[GetStageExecutionDetailsAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_GetStageExecutionDetailsAsync_Google_Cloud_Dataflow_V1Beta3_GetStageExecutionDetailsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Iterate over all response items, lazily performing RPCs as required
            await foreach ([WorkerDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.WorkerDetails.html) item in response)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
    
            // Or iterate over pages (of server-defined size), performing one RPC per page
            await foreach ([StageExecutionDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.StageExecutionDetails.html) page in response.AsRawResponses())
            {
                // Do something with each page of items
                Console.WriteLine("A page of results:");
                foreach ([WorkerDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.WorkerDetails.html) item in page)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
            }
    
            // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
            int pageSize = 10;
            Page<WorkerDetails> singlePage = await response.ReadPageAsync(pageSize);
            // Do something with the page of items
            Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
            foreach ([WorkerDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.WorkerDetails.html) item in singlePage)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
            // Store the pageToken, for when the next page is required.
            string nextPageToken = singlePage.NextPageToken;
        }
    }

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.dataflow.v1beta3.GetStageExecutionDetailsRequest;
    import com.google.dataflow.v1beta3.MetricsV1Beta3Client;
    import com.google.dataflow.v1beta3.WorkerDetails;
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    
    public class AsyncGetStageExecutionDetails {
    
      public static void main(String[] args) throws Exception {
        asyncGetStageExecutionDetails();
      }
    
      public static void asyncGetStageExecutionDetails() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (MetricsV1Beta3Client metricsV1Beta3Client = MetricsV1Beta3Client.[create](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html#com_google_api_core_SettableApiFuture__V_create__)()) {
          GetStageExecutionDetailsRequest request =
              GetStageExecutionDetailsRequest.newBuilder()
                  .setProjectId("projectId-894832108")
                  .setJobId("jobId101296568")
                  .setLocation("location1901043637")
                  .setStageId("stageId-1897528135")
                  .setPageSize(883849137)
                  .setPageToken("pageToken873572522")
                  .setStartTime([Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder().build())
                  .setEndTime([Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder().build())
                  .build();
          ApiFuture<WorkerDetails> future =
              metricsV1Beta3Client.getStageExecutionDetailsPagedCallable().futureCall(request);
          // Do something.
          for (WorkerDetails element : future.get().iterateAll()) {
            // doThingsWith(element);
          }
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
     *  A project id.
     */
    // const projectId = 'abc123'
    /**
     *  The job to get execution details for.
     */
    // const jobId = 'abc123'
    /**
     *  The regional endpoint 
     *  (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that
     *  contains the job specified by job_id.
     */
    // const location = 'abc123'
    /**
     *  The stage for which to fetch information.
     */
    // const stageId = 'abc123'
    /**
     *  If specified, determines the maximum number of work items to
     *  return.  If unspecified, the service may choose an appropriate
     *  default, or may return an arbitrarily large number of results.
     */
    // const pageSize = 1234
    /**
     *  If supplied, this should be the value of next_page_token returned
     *  by an earlier call. This will cause the next page of results to
     *  be returned.
     */
    // const pageToken = 'abc123'
    /**
     *  Lower time bound of work items to include, by start time.
     */
    // const startTime = {}
    /**
     *  Upper time bound of work items to include, by start time.
     */
    // const endTime = {}
    
    // Imports the Dataflow library
    const {MetricsV1Beta3Client} = require('[@google-cloud/dataflow](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)').v1beta3;
    
    // Instantiates a client
    const dataflowClient = new [MetricsV1Beta3Client](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)();
    
    async function callGetStageExecutionDetails() {
      // Construct request
      const request = {
      };
    
      // Run request
      const iterable = dataflowClient.[getStageExecutionDetailsAsync](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/v1beta3.metricsv1beta3client.html)(request);
      for await (const response of iterable) {
          console.log(response);
      }
    }
    
    callGetStageExecutionDetails();

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
    
    
    async def sample_get_stage_execution_details():
        # Create a client
        client = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[MetricsV1Beta3AsyncClient](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.metrics_v1_beta3.MetricsV1Beta3AsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[GetStageExecutionDetailsRequest](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.types.GetStageExecutionDetailsRequest.html)()
    
        # Make the request
        page_result = client.[get_stage_execution_details](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.metrics_v1_beta3.MetricsV1Beta3AsyncClient.html#google_cloud_dataflow_v1beta3_services_metrics_v1_beta3_MetricsV1Beta3AsyncClient_get_stage_execution_details)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
