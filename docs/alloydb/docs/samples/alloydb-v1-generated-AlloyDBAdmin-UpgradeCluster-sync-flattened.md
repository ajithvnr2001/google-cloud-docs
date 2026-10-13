---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdmin-UpgradeCluster-sync-flattened/
title: Upgrade a cluster \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:06.424517+00:00
---

# Upgrade a cluster  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdmin-UpgradeCluster-sync-flattened/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Upgrade a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This snippet shows how to perform an in-place upgrade of a cluster to a newer database version. Users would do this to take advantage of new features, performance improvements, and security fixes available in the target version.

## Code sample

### C#

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.AlloyDb.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedAlloyDBAdminClientSnippets
    {
        /// <summary>Snippet for UpgradeCluster</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void UpgradeCluster()
        {
            // Create client
            [AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html) alloyDBAdminClient = [AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html#Google_Cloud_AlloyDb_V1_AlloyDBAdminClient_Create)();
            // Initialize request argument(s)
            string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
            [DatabaseVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.DatabaseVersion.html) version = [DatabaseVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.DatabaseVersion.html).[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.DatabaseVersion.html#Google_Cloud_AlloyDb_V1_DatabaseVersion_Unspecified);
            // Make the request
            Operation<UpgradeClusterResponse, OperationMetadata> response = alloyDBAdminClient.[UpgradeCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html#Google_Cloud_AlloyDb_V1_AlloyDBAdminClient_UpgradeCluster_Google_Cloud_AlloyDb_V1_ClusterName_Google_Cloud_AlloyDb_V1_DatabaseVersion_Google_Api_Gax_Grpc_CallSettings_)(name, version);
    
            // Poll until the returned long-running operation is complete
            Operation<UpgradeClusterResponse, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.UpgradeClusterResponse.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<UpgradeClusterResponse, OperationMetadata> retrievedResponse = alloyDBAdminClient.[PollOnceUpgradeCluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html#Google_Cloud_AlloyDb_V1_AlloyDBAdminClient_PollOnceUpgradeCluster_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [UpgradeClusterResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.UpgradeClusterResponse.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
