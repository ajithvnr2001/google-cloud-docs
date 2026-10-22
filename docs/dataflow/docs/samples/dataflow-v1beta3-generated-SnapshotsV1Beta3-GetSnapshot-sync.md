---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-SnapshotsV1Beta3-GetSnapshot-sync/
title: Get a snapshot \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:32.575048+00:00
---

# Get a snapshot  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-v1beta3-generated-SnapshotsV1Beta3-GetSnapshot-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Get a snapshot Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to get a snapshot.

## Code sample

### C#

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataflow.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.html);
    
    public sealed partial class GeneratedSnapshotsV1Beta3ClientSnippets
    {
        /// <summary>Snippet for GetSnapshot</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void GetSnapshotRequestObject()
        {
            // Create client
            [SnapshotsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.SnapshotsV1Beta3Client.html) snapshotsV1Beta3Client = [SnapshotsV1Beta3Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.SnapshotsV1Beta3Client.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.SnapshotsV1Beta3Client.html#Google_Cloud_Dataflow_V1Beta3_SnapshotsV1Beta3Client_Create)();
            // Initialize request argument(s)
            [GetSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetSnapshotRequest.html) request = new [GetSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.GetSnapshotRequest.html)
            {
                ProjectId = "",
                SnapshotId = "",
                Location = "",
            };
            // Make the request
            [Snapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.Snapshot.html) response = snapshotsV1Beta3Client.[GetSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.SnapshotsV1Beta3Client.html#Google_Cloud_Dataflow_V1Beta3_SnapshotsV1Beta3Client_GetSnapshot_Google_Cloud_Dataflow_V1Beta3_GetSnapshotRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
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
    	c, err := dataflow.NewSnapshotsV1Beta3Client(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataflowpb.GetSnapshotRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataflow/apiv1beta3/dataflowpb#GetSnapshotRequest.
    	}
    	resp, err := c.GetSnapshot(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.dataflow.v1beta3.GetSnapshotRequest;
    import com.google.dataflow.v1beta3.Snapshot;
    import com.google.dataflow.v1beta3.SnapshotsV1Beta3Client;
    
    public class SyncGetSnapshot {
    
      public static void main(String[] args) throws Exception {
        syncGetSnapshot();
      }
    
      public static void syncGetSnapshot() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (SnapshotsV1Beta3Client snapshotsV1Beta3Client = SnapshotsV1Beta3Client.create()) {
          GetSnapshotRequest request =
              GetSnapshotRequest.newBuilder()
                  .setProjectId("projectId-894832108")
                  .setSnapshotId("snapshotId-1113817601")
                  .setLocation("location1901043637")
                  .build();
          Snapshot response = snapshotsV1Beta3Client.getSnapshot(request);
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
    
    
    def sample_get_snapshot():
        # Create a client
        client = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[SnapshotsV1Beta3Client](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.snapshots_v1_beta3.SnapshotsV1Beta3Client.html)()
    
        # Initialize request argument(s)
        request = [dataflow_v1beta3](https://docs.cloud.google.com/python/docs/reference/dataflow/latest).[GetSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.types.GetSnapshotRequest.html)()
    
        # Make the request
        response = client.[get_snapshot](https://docs.cloud.google.com/python/docs/reference/dataflow/latest/google.cloud.dataflow_v1beta3.services.snapshots_v1_beta3.SnapshotsV1Beta3Client.html#google_cloud_dataflow_v1beta3_services_snapshots_v1_beta3_SnapshotsV1Beta3Client_get_snapshot)(request=request)
    
        # Handle the response
        print(response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
