---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-JobsV1Beta3-SnapshotJob-async/
title: Snapshot the state of a streaming job (async) \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:35.390806+00:00
---

# Snapshot the state of a streaming job (async)  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-JobsV1Beta3-SnapshotJob-async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Snapshot the state of a streaming job (async) Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to snapshot the state of a streaming job asynchronously.

## Code sample

### C#

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataflow.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System.Threading.Tasks;
    
    public sealed partial class GeneratedJobsV1Beta3ClientSnippets
    {
        /// <summary>Snippet for SnapshotJobAsync</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public async Task SnapshotJobRequestObjectAsync()
        {
            // Create client
            [JobsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.JobsV1Beta3Client.html) jobsV1Beta3Client = await [JobsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.JobsV1Beta3Client.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.JobsV1Beta3Client.html#Google_Cloud_Dataflow_V1Beta3_JobsV1Beta3Client_CreateAsync_System_Threading_CancellationToken_)();
            // Initialize request argument(s)
            [SnapshotJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.SnapshotJobRequest.html) request = new [SnapshotJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.SnapshotJobRequest.html)
            {
                ProjectId = "",
                JobId = "",
                Ttl = new [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)(),
                Location = "",
                SnapshotSources = false,
                Description = "",
            };
            // Make the request
            [Snapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.Snapshot.html) response = await jobsV1Beta3Client.[SnapshotJobAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.JobsV1Beta3Client.html#Google_Cloud_Dataflow_V1Beta3_JobsV1Beta3Client_SnapshotJobAsync_Google_Cloud_Dataflow_V1Beta3_SnapshotJobRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.dataflow.v1beta3.JobsV1Beta3Client;
    import com.google.dataflow.v1beta3.Snapshot;
    import com.google.dataflow.v1beta3.SnapshotJobRequest;
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    
    public class AsyncSnapshotJob {
    
      public static void main(String[] args) throws Exception {
        asyncSnapshotJob();
      }
    
      public static void asyncSnapshotJob() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (JobsV1Beta3Client jobsV1Beta3Client = JobsV1Beta3Client.[create](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.SettableApiFuture.html#com_google_api_core_SettableApiFuture__V_create__)()) {
          SnapshotJobRequest request =
              SnapshotJobRequest.newBuilder()
                  .setProjectId("projectId-894832108")
                  .setJobId("jobId101296568")
                  .setTtl([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().build())
                  .setLocation("location1901043637")
                  .setSnapshotSources(true)
                  .setDescription("description-1724546052")
                  .build();
          ApiFuture<Snapshot> future = jobsV1Beta3Client.snapshotJobCallable().futureCall(request);
          // Do something.
          Snapshot response = future.get();
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
     *  The project which owns the job to be snapshotted.
     */
    // const projectId = 'abc123'
    /**
     *  The job to be snapshotted.
     */
    // const jobId = 'abc123'
    /**
     *  TTL for the snapshot.
     */
    // const ttl = {}
    /**
     *  The location that contains this job.
     */
    // const location = 'abc123'
    /**
     *  If true, perform snapshots for sources which support this.
     */
    // const snapshotSources = true
    /**
     *  User specified description of the snapshot. Maybe empty.
     */
    // const description = 'abc123'
    
    // Imports the Dataflow library
    const {JobsV1Beta3Client} = require('[@google-cloud/dataflow](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)').v1beta3;
    
    // Instantiates a client
    const dataflowClient = new [JobsV1Beta3Client](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)();
    
    async function callSnapshotJob() {
      // Construct request
      const request = {
      };
    
      // Run request
      const response = await dataflowClient.snapshotJob(request);
      console.log(response);
    }
    
    callSnapshotJob();

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
    
    
    async def sample_snapshot_job():
        # Create a client
        client = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[JobsV1Beta3AsyncClient](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.jobs_v1_beta3.JobsV1Beta3AsyncClient.html)()
    
        # Initialize request argument(s)
        request = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[SnapshotJobRequest](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.types.SnapshotJobRequest.html)()
    
        # Make the request
        response = await client.[snapshot_job](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.jobs_v1_beta3.JobsV1Beta3AsyncClient.html#google_cloud_dataflow_v1beta3_services_jobs_v1_beta3_JobsV1Beta3AsyncClient_snapshot_job)(request=request)
    
        # Handle the response
        print(response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
