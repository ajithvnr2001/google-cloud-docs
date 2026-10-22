---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdmin-BatchCreateInstances-sync/
title: Batch create instances \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:25.805686+00:00
---

# Batch create instances  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdmin-BatchCreateInstances-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Batch create instances Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to create multiple instances within a cluster in a single request. Use this method to efficiently add multiple read replicas to a cluster at once.

## Code sample

### C#

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.AlloyDb.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedAlloyDBAdminClientSnippets
    {
        /// <summary>Snippet for BatchCreateInstances</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void BatchCreateInstancesRequestObject()
        {
            // Create client
            [AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html) alloyDBAdminClient = [AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html#Google_Cloud_AlloyDb_V1_AlloyDBAdminClient_Create)();
            // Initialize request argument(s)
            [BatchCreateInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.BatchCreateInstancesRequest.html) request = new [BatchCreateInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.BatchCreateInstancesRequest.html)
            {
                ParentAsClusterName = [ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ClusterName.html).[FromProjectLocationCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ClusterName.html#Google_Cloud_AlloyDb_V1_ClusterName_FromProjectLocationCluster_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
                Requests = new [CreateInstanceRequests](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.CreateInstanceRequests.html)(),
                RequestId = "",
            };
            // Make the request
            Operation<BatchCreateInstancesResponse, OperationMetadata> response = alloyDBAdminClient.[BatchCreateInstances](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html#Google_Cloud_AlloyDb_V1_AlloyDBAdminClient_BatchCreateInstances_Google_Cloud_AlloyDb_V1_BatchCreateInstancesRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<BatchCreateInstancesResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [BatchCreateInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.BatchCreateInstancesResponse.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<BatchCreateInstancesResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.[PollOnceBatchCreateInstances](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html#Google_Cloud_AlloyDb_V1_AlloyDBAdminClient_PollOnceBatchCreateInstances_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [BatchCreateInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.BatchCreateInstancesResponse.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	alloydb "cloud.google.com/go/alloydb/apiv1"
    	alloydbpb "cloud.google.com/go/alloydb/apiv1/alloydbpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := alloydb.NewAlloyDBAdminClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &alloydbpb.BatchCreateInstancesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/alloydb/apiv1/alloydbpb#BatchCreateInstancesRequest.
    	}
    	op, err := c.BatchCreateInstances(ctx, req)
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

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.alloydb.v1.[AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.html);
    import com.google.cloud.alloydb.v1.[BatchCreateInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BatchCreateInstancesRequest.html);
    import com.google.cloud.alloydb.v1.[BatchCreateInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BatchCreateInstancesResponse.html);
    import com.google.cloud.alloydb.v1.[ClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ClusterName.html);
    import com.google.cloud.alloydb.v1.[CreateInstanceRequests](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateInstanceRequests.html);
    
    public class SyncBatchCreateInstances {
    
      public static void main(String[] args) throws Exception {
        syncBatchCreateInstances();
      }
    
      public static void syncBatchCreateInstances() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.html) alloyDBAdminClient = [AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.html).create()) {
          [BatchCreateInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BatchCreateInstancesRequest.html) request =
              [BatchCreateInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BatchCreateInstancesRequest.html).newBuilder()
                  .setParent([ClusterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ClusterName.html).of("[PROJECT]", "[LOCATION]", "[CLUSTER]").toString())
                  .[setRequests](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BatchCreateInstancesRequest.Builder.html#com_google_cloud_alloydb_v1_BatchCreateInstancesRequest_Builder_setRequests_com_google_cloud_alloydb_v1_CreateInstanceRequests_)([CreateInstanceRequests](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.CreateInstanceRequests.html).newBuilder().build())
                  .setRequestId("requestId693933066")
                  .build();
          [BatchCreateInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BatchCreateInstancesResponse.html) response =
              alloyDBAdminClient.[batchCreateInstancesAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.AlloyDBAdminClient.html#com_google_cloud_alloydb_v1_AlloyDBAdminClient_batchCreateInstancesAsync_com_google_cloud_alloydb_v1_BatchCreateInstancesRequest_)(request).get();
        }
      }
    }

### Python

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [alloydb_v1](https://docs.cloud.google.com/python/docs/reference/alloydb/latest)
    
    
    def sample_batch_create_instances():
        # Create a client
        client = [alloydb_v1](https://docs.cloud.google.com/python/docs/reference/alloydb/latest).[AlloyDBAdminClient](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1.services.alloy_db_admin.AlloyDBAdminClient.html)()
    
        # Initialize request argument(s)
        requests = [alloydb_v1](https://docs.cloud.google.com/python/docs/reference/alloydb/latest).[CreateInstanceRequests](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1.types.CreateInstanceRequests.html)()
        requests.create_instance_requests.parent = "parent_value"
        requests.create_instance_requests.instance_id = "instance_id_value"
        requests.create_instance_requests.instance.instance_type = "SECONDARY"
    
        request = [alloydb_v1](https://docs.cloud.google.com/python/docs/reference/alloydb/latest).[BatchCreateInstancesRequest](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1.types.BatchCreateInstancesRequest.html)(
            parent="parent_value",
            requests=requests,
        )
    
        # Make the request
        operation = client.[batch_create_instances](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1.services.alloy_db_admin.AlloyDBAdminClient.html#google_cloud_alloydb_v1_services_alloy_db_admin_AlloyDBAdminClient_batch_create_instances)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### Ruby

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/alloy_db/v1"
    
    ##
    # Snippet for the batch_create_instances call in the AlloyDBAdmin service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::AlloyDB::V1::AlloyDBAdmin::Client#batch_create_instances.
    #
    def batch_create_instances
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::AlloyDB::V1::AlloyDBAdmin::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::AlloyDB::V1::BatchCreateInstancesRequest.new
    
      # Call the batch_create_instances method.
      result = client.batch_create_instances request
    
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

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
