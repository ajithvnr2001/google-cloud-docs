---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdmin-ExportCluster-sync-flattened/
title: Export a cluster \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:38.704140+00:00
---

# Export a cluster  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdmin-ExportCluster-sync-flattened/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Export a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This snippet shows how to export data from a cluster to a Google Cloud Storage bucket. Use this to create backups or to migrate data to other services.

## Code sample

### C#

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.AlloyDb.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedAlloyDBAdminClientSnippets
    {
        /// <summary>Snippet for ExportCluster</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void ExportCluster()
        {
            // Create client
            [AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html) alloyDBAdminClient = [AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html#Google_Cloud_AlloyDb_V1_AlloyDBAdminClient_Create)();
            // Initialize request argument(s)
            string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
            [GcsDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.GcsDestination.html) gcsDestination = new [GcsDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.GcsDestination.html)();
            string database = "";
            ExportClusterRequest.Types.CsvExportOptions csvExportOptions = new ExportClusterRequest.Types.CsvExportOptions();
            ExportClusterRequest.Types.SqlExportOptions sqlExportOptions = new ExportClusterRequest.Types.SqlExportOptions();
            // Make the request
            Operation<ExportClusterResponse, OperationMetadata> response = alloyDBAdminClient.[ExportCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html#Google_Cloud_AlloyDb_V1_AlloyDBAdminClient_ExportCluster_Google_Cloud_AlloyDb_V1_ClusterName_Google_Cloud_AlloyDb_V1_GcsDestination_System_String_Google_Cloud_AlloyDb_V1_ExportClusterRequest_Types_CsvExportOptions_Google_Cloud_AlloyDb_V1_ExportClusterRequest_Types_SqlExportOptions_Google_Api_Gax_Grpc_CallSettings_)(name, gcsDestination, database, csvExportOptions, sqlExportOptions);
    
            // Poll until the returned long-running operation is complete
            Operation<ExportClusterResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ExportClusterResponse.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<ExportClusterResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.[PollOnceExportCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html#Google_Cloud_AlloyDb_V1_AlloyDBAdminClient_PollOnceExportCluster_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [ExportClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ExportClusterResponse.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
