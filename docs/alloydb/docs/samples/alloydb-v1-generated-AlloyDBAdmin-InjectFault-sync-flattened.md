---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdmin-InjectFault-sync-flattened/
title: Inject an instance fault \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:11.004788+00:00
---

# Inject an instance fault  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-v1-generated-AlloyDBAdmin-InjectFault-sync-flattened/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Inject an instance fault Stay organized with collections  Save and categorize content based on your preferences. 

Inject a fault into a specific instance to test how your application handles database failures. This is useful for verifying your application's failover and recovery procedures.

## Code sample

### C#

To authenticate to AlloyDB, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.AlloyDb.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedAlloyDBAdminClientSnippets
    {
        /// <summary>Snippet for InjectFault</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void InjectFault()
        {
            // Create client
            [AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html) alloyDBAdminClient = [AlloyDBAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html#Google_Cloud_AlloyDb_V1_AlloyDBAdminClient_Create)();
            // Initialize request argument(s)
            InjectFaultRequest.Types.FaultType faultType = [InjectFaultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.InjectFaultRequest.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.InjectFaultRequest.Types.html).[FaultType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.InjectFaultRequest.Types.FaultType.html).[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.InjectFaultRequest.Types.FaultType.html#Google_Cloud_AlloyDb_V1_InjectFaultRequest_Types_FaultType_Unspecified);
            string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/instances/[INSTANCE]";
            // Make the request
            Operation<Instance, OperationMetadata> response = alloyDBAdminClient.[InjectFault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html#Google_Cloud_AlloyDb_V1_AlloyDBAdminClient_InjectFault_Google_Cloud_AlloyDb_V1_InjectFaultRequest_Google_Api_Gax_Grpc_CallSettings_)(faultType, name);
    
            // Poll until the returned long-running operation is complete
            Operation<Instance, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Instance, OperationMetadata> retrievedResponse = alloyDBAdminClient.[PollOnceInjectFault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.AlloyDBAdminClient.html#Google_Cloud_AlloyDb_V1_AlloyDBAdminClient_PollOnceInjectFault_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.Instance.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
