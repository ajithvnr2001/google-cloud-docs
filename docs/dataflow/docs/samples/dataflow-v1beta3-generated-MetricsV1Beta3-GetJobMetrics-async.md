---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-async/
title: Get job metrics (async) \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:09.715398+00:00
---

# Get job metrics (async)  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-MetricsV1Beta3-GetJobMetrics-async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Get job metrics (async) Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to get a collection of metrics describing the detailed progress of a job.

## Code sample

### C#

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataflow.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedMetricsV1Beta3ClientSnippets
    {
        /// <summary>Snippet for GetJobMetricsAsync</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task GetJobMetricsRequestObjectAsync()
        {
            // Create client
            [MetricsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html) metricsV1Beta3Client = await [MetricsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_CreateAsync_System_Threading_CancellationToken_)();
            // Initialize request argument(s)
            [GetJobMetricsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetJobMetricsRequest.html) request = new [GetJobMetricsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetJobMetricsRequest.html)
            {
                ProjectId = "",
                JobId = "",
                StartTime = new [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)(),
                Location = "",
            };
            // Make the request
            [JobMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.JobMetrics.html) response = await metricsV1Beta3Client.[GetJobMetricsAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.MetricsV1Beta3Client.html#Google_Cloud_Dataflow_V1Beta3_MetricsV1Beta3Client_GetJobMetricsAsync_Google_Cloud_Dataflow_V1Beta3_GetJobMetricsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.dataflow.v1beta3.GetJobMetricsRequest;
    import com.google.dataflow.v1beta3.JobMetrics;
    import com.google.dataflow.v1beta3.MetricsV1Beta3Client;
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    
    public class AsyncGetJobMetrics {
    
      public static void main(String[] args) throws Exception {
        asyncGetJobMetrics();
      }
    
      public static void asyncGetJobMetrics() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (MetricsV1Beta3Client metricsV1Beta3Client = MetricsV1Beta3Client.[create](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html#com_google_api_core_SettableApiFuture__V_create__)()) {
          GetJobMetricsRequest request =
              GetJobMetricsRequest.newBuilder()
                  .setProjectId("projectId-894832108")
                  .setJobId("jobId101296568")
                  .setStartTime([Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder().build())
                  .setLocation("location1901043637")
                  .build();
          ApiFuture<JobMetrics> future =
              metricsV1Beta3Client.getJobMetricsCallable().futureCall(request);
          // Do something.
          JobMetrics response = future.get();
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
     *  The job to get metrics for.
     */
    // const jobId = 'abc123'
    /**
     *  Return only metric data that has changed since this time.
     *  Default is to return all information about all metrics for the job.
     */
    // const startTime = {}
    /**
     *  The regional endpoint 
     *  (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that
     *  contains the job specified by job_id.
     */
    // const location = 'abc123'
    
    // Imports the Dataflow library
    const {MetricsV1Beta3Client} = require('[@google-cloud/dataflow](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)').v1beta3;
    
    // Instantiates a client
    const dataflowClient = new [MetricsV1Beta3Client](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)();
    
    async function callGetJobMetrics() {
      // Construct request
      const request = {
      };
    
      // Run request
      const response = await dataflowClient.getJobMetrics(request);
      console.log(response);
    }
    
    callGetJobMetrics();

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
    
    
    async def sample_get_job_metrics():
        # Create a client
        client = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[MetricsV1Beta3AsyncClient](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.metrics_v1_beta3.MetricsV1Beta3AsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[GetJobMetricsRequest](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.types.GetJobMetricsRequest.html)()
    
        # Make the request
        response = await client.[get_job_metrics](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.metrics_v1_beta3.MetricsV1Beta3AsyncClient.html#google_cloud_dataflow_v1beta3_services_metrics_v1_beta3_MetricsV1Beta3AsyncClient_get_job_metrics)(request=request)
    
        # Handle the response
        print(response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
