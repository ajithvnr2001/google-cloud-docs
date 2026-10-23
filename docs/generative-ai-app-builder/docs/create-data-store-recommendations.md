---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-recommendations/
title: Create a custom recommendations data store \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:30.357774+00:00
---

# Create a custom recommendations data store  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-recommendations/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Create a custom recommendations data store Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [GCP Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the [Generative AI Preview terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

To create a data store and ingest data for custom recommendations, go to the section for which source you plan to use:

  * BigQuery
  * Cloud Storage
  * Upload structured JSON data with the API



## BigQuery

You can create data stores from BigQuery tables in two ways:

  * **One-time ingestion** : You import data from a BigQuery table into a data store. The data in the data store does not change unless you manually [refresh the data](https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-data).

  * **Periodic ingestion** : You import data from one or more BigQuery tables, and you set a sync frequency that determines how often the data stores are updated with the most recent data from the BigQuery dataset.




The following table compares the two ways that you can import BigQuery data into Agent Search data stores.

One-time ingestion | Periodic ingestion  
---|---  
Data must be refreshed manually. | Data updates automatically every 1, 3, or 5 days. Data cannot be manually refreshed.  
Agent Search creates a single data store from one _table_ in a BigQuery.  | Agent Search creates a _data connector_ for a BigQuery _dataset_ and a data store (called an _entity_ data store) for each table specified. For each data connector, the tables must have the same data type (for example, structured) and be in the same BigQuery dataset.   
Data from multiple tables can be combined in one data store by first ingesting data from one table and then more data from another source or BigQuery table.  | Because manual data import is not supported, the data in an entity data store can only be sourced from one BigQuery table.  
Data source access control is supported. | Data source access control is not supported. The imported data can contain access controls but these controls won't be respected.  
You can create a data store using either the Google Cloud console or the API. | You must use the console to create data connectors and their entity data stores.   
CMEK-compliant. | CMEK-compliant.  
  
### Before you begin

To import data from a source Google Cloud project that's different from the Google Cloud project with the Agent Search data store, grant the following Identity and Access Management (IAM) roles to the `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com` service account in the project that contains the Agent Search data store:

  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)

**Caution:** When you import data from BigQuery into an Agent Search data store, BigQuery permissions aren't imported with the data. After import, any user with [sufficient Agent Search permissions](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-control#roles) can view the data, even if they don't have permission to view the data in BigQuery.

### Import once from BigQuery

To ingest data from a BigQuery table, use the following steps to create a data store and ingest data using either the Google Cloud console or the API.

Before importing your data, review [Prepare data for ingesting](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data).

### Console

To use the Google Cloud console to ingest data from BigQuery, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Go to the **Data Stores** page.

  3. Click add **Create data store**.

  4. On the **Source** page, select **BigQuery**.

  5. Select the data type you are going to import from the **What kind of data are you importing** section.

  6. Select **One time** in the **Synchronization frequency** section.

  7. In the **BigQuery path** field, click **Browse** , select a table that you have [prepared for ingesting](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data), and then click **Select**. Alternatively, enter the table location directly in the **BigQuery path** field.

  8. Click **Continue**.

  9. If you are doing one-time import of structured data:

     1. Map fields to key properties.

     2. If there are important fields missing from the schema, use **Add new field** to add them.

For more information, see [About auto-detect and edit](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema#about-auto-and-edit).

     3. Click **Continue**.

  10. Choose a region for your data store.

  11. Enter a name for your data store.

  12. Click **Create**.

  13. To check the status of your ingestion, go to the **Data Stores** page and click your data store name to see details about it on its **Data** page. When the status column on the **Activity** tab changes from **In progress** to **Import completed** , the ingestion is complete.

Depending on the size of your data, ingestion can take several minutes to several hours.




### REST

To use the command line to create a data store and import data from BigQuery, follow these steps.

**Note:** If you want to specify a schema instead of letting Agent Search auto-detect the schema for you, do the steps in [Provide your own schema as a JSON object](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema#provide-your-own) and then begin the following procedure at step 2.

  1. Create a data store.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
         -d '{
           "displayName": "DATA_STORE_DISPLAY_NAME",
           "industryVertical": "GENERIC",
           "solutionTypes": ["SOLUTION_TYPE_RECOMMENDATION"]
         }'
         

**Note:** The industry vertical `GENERIC` is used to create structured, unstructured, and website data stores for custom recommendations apps. 

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store that you want to create. This ID can contain only lowercase letters, digits, underscores, and hyphens.
     * `DATA_STORE_DISPLAY_NAME`: the display name of the Agent Search data store that you want to create.
  2. Import data from BigQuery.

If you defined a schema, make sure the data conforms to that schema.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
         -d '{
           "bigquerySource": {
             "projectId": "PROJECT_ID",
             "datasetId":"DATASET_ID",
             "tableId": "TABLE_ID",
             "dataSchema": "DATA_SCHEMA",
             "aclEnabled": "BOOLEAN"
           },
           "reconciliationMode": "RECONCILIATION_MODE",
           "autoGenerateIds": "AUTO_GENERATE_IDS",
           "idField": "ID_FIELD",
           "errorConfig": {
             "gcsPrefix": "ERROR_DIRECTORY"
           }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store.
     * `DATASET_ID`: the ID of the BigQuery dataset.
     * `TABLE_ID`: the ID of the BigQuery table. 
       * If the BigQuery table is not under PROJECT_ID, you need to give the service account `service-<project number>@gcp-sa-discoveryengine.iam.gserviceaccount.com` "BigQuery Data Viewer" permission for the BigQuery table. For example, if you are importing a BigQuery table from source project "123" to destination project "456", give `service-456@gcp-sa-discoveryengine.iam.gserviceaccount.com` permissions for the BigQuery table under project "123".
     * `DATA_SCHEMA`: optional. Values are `document` and `custom`. The default is `document`. 
       * `document`: the BigQuery table that you use must conform to the default BigQuery schema provided in [Prepare data for ingesting](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#unstructured-with-metadata-bq). You can define the ID of each document yourself, while wrapping all the data in the jsonData string.
       * `custom`: Any BigQuery table schema is accepted, and Agent Search automatically generates the IDs for each document that is imported.
     * `ERROR_DIRECTORY`: optional. A Cloud Storage directory for error information about the import—for example, `gs://<your-gcs-bucket>/directory/import_errors`. Google recommends leaving this field empty to let Agent Search automatically create a temporary directory.
     * `RECONCILIATION_MODE`: optional. Values are `FULL` and `INCREMENTAL`. Default is `INCREMENTAL`. Specifying `INCREMENTAL` causes an incremental refresh of data from BigQuery to your data store. This does an upsert operation, which adds new documents and replaces existing documents with updated documents with the same ID. Specifying `FULL` causes a full rebase of the documents in your data store. In other words, new and updated documents are added to your data store, and documents that are not in BigQuery are removed from your data store. The `FULL` mode is helpful if you want to automatically delete documents that you no longer need.
     * `AUTO_GENERATE_IDS`: optional. Specifies whether to automatically generate document IDs. If set to `true`, document IDs are generated based on a hash of the payload. Note that generated document IDs might not remain consistent over multiple imports. If you auto-generate IDs over multiple imports, Google highly recommends setting `reconciliationMode` to `FULL` to maintain consistent document IDs.

Specify `autoGenerateIds` only when `bigquerySource.dataSchema` is set to `custom`. Otherwise, an `INVALID_ARGUMENT` error is returned. If you don't specify `autoGenerateIds` or set it to `false`, you must specify `idField`. Otherwise, the documents fail to import.

     * `ID_FIELD`: optional. Specifies which fields are the document IDs. For BigQuery source files, `idField` indicates the name of the column in the BigQuery table that contains the document IDs.

Specify `idField` only when: (1) `bigquerySource.dataSchema` is set to `custom`, and (2) `auto_generate_ids` is set to `false` or is unspecified. Otherwise, an `INVALID_ARGUMENT` error is returned.

The value of the BigQuery column name must be of string type, must be between 1 and 63 characters, and must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034). Otherwise, the documents fail to import. 




### C#

For more information, see the [Agent Search C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

### Create a data store
    
    
    using [Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedDataStoreServiceClientSnippets
    {
        /// <summary>Snippet for CreateDataStore</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void CreateDataStoreRequestObject()
        {
            // Create client
            [DataStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStoreServiceClient.html) dataStoreServiceClient = [DataStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStoreServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStoreServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DataStoreServiceClient_Create)();
            // Initialize request argument(s)
            [CreateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CreateDataStoreRequest.html) request = new [CreateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CreateDataStoreRequest.html)
            {
                ParentAsCollectionName = [CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CollectionName.html).[FromProjectLocationCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CollectionName.html#Google_Cloud_DiscoveryEngine_V1_CollectionName_FromProjectLocationCollection_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[COLLECTION]"),
                DataStore = new [DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStore.html)(),
                DataStoreId = "",
                CreateAdvancedSiteSearch = false,
                CmekConfigNameAsCmekConfigName = [CmekConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CmekConfigName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CmekConfigName.html#Google_Cloud_DiscoveryEngine_V1_CmekConfigName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                SkipDefaultSchemaCreation = false,
            };
            // Make the request
            Operation<DataStore, CreateDataStoreMetadata> response = dataStoreServiceClient.[CreateDataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStoreServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DataStoreServiceClient_CreateDataStore_Google_Cloud_DiscoveryEngine_V1_CollectionName_Google_Cloud_DiscoveryEngine_V1_DataStore_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<DataStore, CreateDataStoreMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStore.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<DataStore, CreateDataStoreMetadata> retrievedResponse = dataStoreServiceClient.[PollOnceCreateDataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStoreServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DataStoreServiceClient_PollOnceCreateDataStore_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStore.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Import documents
    
    
    using [Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedDocumentServiceClientSnippets
    {
        /// <summary>Snippet for ImportDocuments</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void ImportDocumentsRequestObject()
        {
            // Create client
            [DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html) documentServiceClient = [DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DocumentServiceClient_Create)();
            // Initialize request argument(s)
            [ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsRequest.html) request = new [ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsRequest.html)
            {
                ParentAsBranchName = [BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BranchName.html).[FromProjectLocationDataStoreBranch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BranchName.html#Google_Cloud_DiscoveryEngine_V1_BranchName_FromProjectLocationDataStoreBranch_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
                InlineSource = new ImportDocumentsRequest.Types.InlineSource(),
                ErrorConfig = new [ImportErrorConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportErrorConfig.html)(),
                ReconciliationMode = [ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsRequest.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsRequest.Types.html).[ReconciliationMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsRequest.Types.ReconciliationMode.html).[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsRequest.Types.ReconciliationMode.html#Google_Cloud_DiscoveryEngine_V1_ImportDocumentsRequest_Types_ReconciliationMode_Unspecified),
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
                AutoGenerateIds = false,
                IdField = "",
                ForceRefreshContent = false,
            };
            // Make the request
            Operation<ImportDocumentsResponse, ImportDocumentsMetadata> response = documentServiceClient.[ImportDocuments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DocumentServiceClient_ImportDocuments_Google_Cloud_DiscoveryEngine_V1_ImportDocumentsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<ImportDocumentsResponse, ImportDocumentsMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [ImportDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsResponse.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<ImportDocumentsResponse, ImportDocumentsMetadata> retrievedResponse = documentServiceClient.[PollOnceImportDocuments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DocumentServiceClient_PollOnceImportDocuments_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [ImportDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsResponse.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

For more information, see the [Agent Search Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

### Create a data store
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	discoveryengine "cloud.google.com/go/discoveryengine/apiv1"
    	discoveryenginepb "cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := discoveryengine.[NewDataStoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1.html#cloud_google_com_go_discoveryengine_apiv1_DataStoreClient_NewDataStoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &discoveryenginepb.CreateDataStoreRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#CreateDataStoreRequest.
    	}
    	op, err := c.CreateDataStore(ctx, req)
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
    

### Import documents
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	discoveryengine "cloud.google.com/go/discoveryengine/apiv1"
    	discoveryenginepb "cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := discoveryengine.[NewDocumentClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1.html#cloud_google_com_go_discoveryengine_apiv1_DocumentClient_NewDocumentClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &discoveryenginepb.ImportDocumentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#ImportDocumentsRequest.
    	}
    	op, err := c.ImportDocuments(ctx, req)
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

For more information, see the [Agent Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/overview). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

### Create a data store
    
    
    import com.google.cloud.discoveryengine.v1.[CollectionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CollectionName.html);
    import com.google.cloud.discoveryengine.v1.[CreateDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest.html);
    import com.google.cloud.discoveryengine.v1.[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore.html);
    import com.google.cloud.discoveryengine.v1.[DataStoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient.html);
    
    public class SyncCreateDataStore {
    
      public static void main(String[] args) throws Exception {
        syncCreateDataStore();
      }
    
      public static void syncCreateDataStore() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataStoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient.html) dataStoreServiceClient = [DataStoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient.html).create()) {
          [CreateDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest.html) request =
              [CreateDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest.html).newBuilder()
                  .setParent([CollectionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CollectionName.html).of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
                  .setDataStore([DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore.html).newBuilder().build())
                  .[setDataStoreId](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest.Builder.html#com_google_cloud_discoveryengine_v1_CreateDataStoreRequest_Builder_setDataStoreId_java_lang_String_)("dataStoreId929489618")
                  .[setCreateAdvancedSiteSearch](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest.Builder.html#com_google_cloud_discoveryengine_v1_CreateDataStoreRequest_Builder_setCreateAdvancedSiteSearch_boolean_)(true)
                  .[setSkipDefaultSchemaCreation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest.Builder.html#com_google_cloud_discoveryengine_v1_CreateDataStoreRequest_Builder_setSkipDefaultSchemaCreation_boolean_)(true)
                  .build();
          [DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore.html) response = dataStoreServiceClient.[createDataStoreAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient.html#com_google_cloud_discoveryengine_v1_DataStoreServiceClient_createDataStoreAsync__org_jspecify_annotations_Nullable_com_google_cloud_discoveryengine_v1_CollectionName_com_google_cloud_discoveryengine_v1_DataStore_java_lang_String_)(request).get();
        }
      }
    }

### Import documents
    
    
    import com.google.cloud.discoveryengine.v1.[BranchName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BranchName.html);
    import com.google.cloud.discoveryengine.v1.[DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.html);
    import com.google.cloud.discoveryengine.v1.[ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest.html);
    import com.google.cloud.discoveryengine.v1.[ImportDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsResponse.html);
    import com.google.cloud.discoveryengine.v1.[ImportErrorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportErrorConfig.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    
    public class SyncImportDocuments {
    
      public static void main(String[] args) throws Exception {
        syncImportDocuments();
      }
    
      public static void syncImportDocuments() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.html) documentServiceClient = [DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.html).create()) {
          [ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest.html) request =
              [ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest.html).newBuilder()
                  .setParent(
                      [BranchName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BranchName.html).[ofProjectLocationDataStoreBranchName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BranchName.html#com_google_cloud_discoveryengine_v1_BranchName_ofProjectLocationDataStoreBranchName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(
                              "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                          .toString())
                  .setErrorConfig([ImportErrorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportErrorConfig.html).newBuilder().build())
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().build())
                  .[setAutoGenerateIds](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest.Builder.html#com_google_cloud_discoveryengine_v1_ImportDocumentsRequest_Builder_setAutoGenerateIds_boolean_)(true)
                  .[setIdField](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest.Builder.html#com_google_cloud_discoveryengine_v1_ImportDocumentsRequest_Builder_setIdField_java_lang_String_)("idField1629396127")
                  .[setForceRefreshContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest.Builder.html#com_google_cloud_discoveryengine_v1_ImportDocumentsRequest_Builder_setForceRefreshContent_boolean_)(true)
                  .build();
          [ImportDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsResponse.html) response = documentServiceClient.[importDocumentsAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.html#com_google_cloud_discoveryengine_v1_DocumentServiceClient_importDocumentsAsync_com_google_cloud_discoveryengine_v1_ImportDocumentsRequest_)(request).get();
        }
      }
    }

### Node.js

For more information, see the [Agent Search Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

### Create a data store
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Resource name of the CmekConfig to use for protecting this DataStore.
     */
    // const cmekConfigName = 'abc123'
    /**
     *  DataStore without CMEK protections. If a default CmekConfig is set for
     *  the project, setting this field will override the default CmekConfig as
     *  well.
     */
    // const disableCmek = true
    /**
     *  Required. The parent resource name, such as
     *  `projects/{project}/locations/{location}/collections/{collection}`.
     */
    // const parent = 'abc123'
    /**
     *  Required. The DataStore google.cloud.discoveryengine.v1.DataStore  to
     *  create.
     */
    // const dataStore = {}
    /**
     *  Required. The ID to use for the
     *  DataStore google.cloud.discoveryengine.v1.DataStore, which will become
     *  the final component of the
     *  DataStore google.cloud.discoveryengine.v1.DataStore's resource name.
     *  This field must conform to RFC-1034 (https://tools.ietf.org/html/rfc1034)
     *  standard with a length limit of 63 characters. Otherwise, an
     *  INVALID_ARGUMENT error is returned.
     */
    // const dataStoreId = 'abc123'
    /**
     *  A boolean flag indicating whether user want to directly create an advanced
     *  data store for site search.
     *  If the data store is not configured as site
     *  search (GENERIC vertical and PUBLIC_WEBSITE content_config), this flag will
     *  be ignored.
     */
    // const createAdvancedSiteSearch = true
    /**
     *  A boolean flag indicating whether to skip the default schema creation for
     *  the data store. Only enable this flag if you are certain that the default
     *  schema is incompatible with your use case.
     *  If set to true, you must manually create a schema for the data store before
     *  any documents can be ingested.
     *  This flag cannot be specified if `data_store.starting_schema` is specified.
     */
    // const skipDefaultSchemaCreation = true
    
    // Imports the Discoveryengine library
    const {DataStoreServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1;
    
    // Instantiates a client
    const discoveryengineClient = new [DataStoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
    async function callCreateDataStore() {
      // Construct request
      const request = {
        parent,
        dataStore,
        dataStoreId,
      };
    
      // Run request
      const [operation] = await discoveryengineClient.createDataStore(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callCreateDataStore();

### Import documents
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  The Inline source for the input content for documents.
     */
    // const inlineSource = {}
    /**
     *  Cloud Storage location for the input content.
     */
    // const gcsSource = {}
    /**
     *  BigQuery input source.
     */
    // const bigquerySource = {}
    /**
     *  FhirStore input source.
     */
    // const fhirStoreSource = {}
    /**
     *  Spanner input source.
     */
    // const spannerSource = {}
    /**
     *  Cloud SQL input source.
     */
    // const cloudSqlSource = {}
    /**
     *  Firestore input source.
     */
    // const firestoreSource = {}
    /**
     *  AlloyDB input source.
     */
    // const alloyDbSource = {}
    /**
     *  Cloud Bigtable input source.
     */
    // const bigtableSource = {}
    /**
     *  Required. The parent branch resource name, such as
     *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.
     *  Requires create/update permission.
     */
    // const parent = 'abc123'
    /**
     *  The desired location of errors incurred during the Import.
     */
    // const errorConfig = {}
    /**
     *  The mode of reconciliation between existing documents and the documents to
     *  be imported. Defaults to
     *  ReconciliationMode.INCREMENTAL google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL.
     */
    // const reconciliationMode = {}
    /**
     *  Indicates which fields in the provided imported documents to update. If
     *  not set, the default is to update all fields.
     */
    // const updateMask = {}
    /**
     *  Whether to automatically generate IDs for the documents if absent.
     *  If set to `true`,
     *  Document.id google.cloud.discoveryengine.v1.Document.id s are
     *  automatically generated based on the hash of the payload, where IDs may not
     *  be consistent during multiple imports. In which case
     *  ReconciliationMode.FULL google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode.FULL 
     *  is highly recommended to avoid duplicate contents. If unset or set to
     *  `false`, Document.id google.cloud.discoveryengine.v1.Document.id s have
     *  to be specified using
     *  id_field google.cloud.discoveryengine.v1.ImportDocumentsRequest.id_field,
     *  otherwise, documents without IDs fail to be imported.
     *  Supported data sources:
     *  * GcsSource google.cloud.discoveryengine.v1.GcsSource.
     *  GcsSource.data_schema google.cloud.discoveryengine.v1.GcsSource.data_schema 
     *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
     *  * BigQuerySource google.cloud.discoveryengine.v1.BigQuerySource.
     *  BigQuerySource.data_schema google.cloud.discoveryengine.v1.BigQuerySource.data_schema 
     *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
     *  * SpannerSource google.cloud.discoveryengine.v1.SpannerSource.
     *  * CloudSqlSource google.cloud.discoveryengine.v1.CloudSqlSource.
     *  * FirestoreSource google.cloud.discoveryengine.v1.FirestoreSource.
     *  * BigtableSource google.cloud.discoveryengine.v1.BigtableSource.
     */
    // const autoGenerateIds = true
    /**
     *  The field indicates the ID field or column to be used as unique IDs of
     *  the documents.
     *  For GcsSource google.cloud.discoveryengine.v1.GcsSource  it is the key of
     *  the JSON field. For instance, `my_id` for JSON `{"my_id": "some_uuid"}`.
     *  For others, it may be the column name of the table where the unique ids are
     *  stored.
     *  The values of the JSON field or the table column are used as the
     *  Document.id google.cloud.discoveryengine.v1.Document.id s. The JSON field
     *  or the table column must be of string type, and the values must be set as
     *  valid strings conform to RFC-1034 (https://tools.ietf.org/html/rfc1034)
     *  with 1-63 characters. Otherwise, documents without valid IDs fail to be
     *  imported.
     *  Only set this field when
     *  auto_generate_ids google.cloud.discoveryengine.v1.ImportDocumentsRequest.auto_generate_ids 
     *  is unset or set as `false`. Otherwise, an INVALID_ARGUMENT error is thrown.
     *  If it is unset, a default value `_id` is used when importing from the
     *  allowed data sources.
     *  Supported data sources:
     *  * GcsSource google.cloud.discoveryengine.v1.GcsSource.
     *  GcsSource.data_schema google.cloud.discoveryengine.v1.GcsSource.data_schema 
     *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
     *  * BigQuerySource google.cloud.discoveryengine.v1.BigQuerySource.
     *  BigQuerySource.data_schema google.cloud.discoveryengine.v1.BigQuerySource.data_schema 
     *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
     *  * SpannerSource google.cloud.discoveryengine.v1.SpannerSource.
     *  * CloudSqlSource google.cloud.discoveryengine.v1.CloudSqlSource.
     *  * FirestoreSource google.cloud.discoveryengine.v1.FirestoreSource.
     *  * BigtableSource google.cloud.discoveryengine.v1.BigtableSource.
     */
    // const idField = 'abc123'
    /**
     *  Optional. Whether to force refresh the unstructured content of the
     *  documents.
     *  If set to `true`, the content part of the documents will be refreshed
     *  regardless of the update status of the referencing content.
     */
    // const forceRefreshContent = true
    
    // Imports the Discoveryengine library
    const {DocumentServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1;
    
    // Instantiates a client
    const discoveryengineClient = new [DocumentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
    async function callImportDocuments() {
      // Construct request
      const request = {
        parent,
      };
    
      // Run request
      const [operation] = await discoveryengineClient.importDocuments(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callImportDocuments();

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

### Create a data store
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION" # Values: "global"
    # data_store_id = "YOUR_DATA_STORE_ID"
    
    
    def create_data_store_sample(
        project_id: str,
        location: str,
        data_store_id: str,
    ) -> str:
        #  For more information, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
        client_options = (
            ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
            if location != "global"
            else None
        )
    
        # Create a client
        client = discoveryengine.[DataStoreServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceClient.html)(client_options=client_options)
    
        # The full resource name of the collection
        # e.g. projects/{project}/locations/{location}/collections/default_collection
        parent = client.[collection_path](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceClient.html#google_cloud_discoveryengine_v1_services_data_store_service_DataStoreServiceClient_collection_path)(
            project=project_id,
            location=location,
            collection="default_collection",
        )
    
        data_store = discoveryengine.[DataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore.html)(
            display_name="My Data Store",
            # Options: GENERIC, MEDIA, HEALTHCARE_FHIR
            industry_vertical=discoveryengine.[IndustryVertical](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.IndustryVertical.html).GENERIC,
            # Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
            solution_types=[discoveryengine.[SolutionType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SolutionType.html).SOLUTION_TYPE_SEARCH],
            # TODO(developer): Update content_config based on data store type.
            # Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
            content_config=discoveryengine.[DataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore.html).[ContentConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore.ContentConfig.html).CONTENT_REQUIRED,
        )
    
        request = discoveryengine.[CreateDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateDataStoreRequest.html)(
            parent=parent,
            data_store_id=data_store_id,
            data_store=data_store,
            # Optional: For Advanced Site Search Only
            # create_advanced_site_search=True,
        )
    
        # Make the request
        operation = client.[create_data_store](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceClient.html#google_cloud_discoveryengine_v1_services_data_store_service_DataStoreServiceClient_create_data_store)(request=request)
    
        print(f"Waiting for operation to complete: {operation.operation.name}")
        response = operation.result()
    
        # After the operation is complete,
        # get information from operation metadata
        metadata = discoveryengine.[CreateDataStoreMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateDataStoreMetadata.html)(operation.metadata)
    
        # Handle the response
        print(response)
        print(metadata)
    
        return operation.operation.name
    
    

### Import documents
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION" # Values: "global"
    # data_store_id = "YOUR_DATA_STORE_ID"
    # bigquery_dataset = "YOUR_BIGQUERY_DATASET"
    # bigquery_table = "YOUR_BIGQUERY_TABLE"
    
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )
    
    # Create a client
    client = discoveryengine.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html)(client_options=client_options)
    
    # The full resource name of the search engine branch.
    # e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
    parent = client.[branch_path](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_branch_path)(
        project=project_id,
        location=location,
        data_store=data_store_id,
        branch="default_branch",
    )
    
    request = discoveryengine.[ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.html)(
        parent=parent,
        bigquery_source=discoveryengine.[BigQuerySource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BigQuerySource.html)(
            project_id=project_id,
            dataset_id=bigquery_dataset,
            table_id=bigquery_table,
            data_schema="custom",
        ),
        # Options: `FULL`, `INCREMENTAL`
        reconciliation_mode=discoveryengine.[ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.html).[ReconciliationMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.ReconciliationMode.html).INCREMENTAL,
    )
    
    # Make the request
    operation = client.[import_documents](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_import_documents)(request=request)
    
    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()
    
    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.[ImportDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsMetadata.html)(operation.metadata)
    
    # Handle the response
    print(response)
    print(metadata)

### Ruby

For more information, see the [Agent Search Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

### Create a data store
    
    
    require "google/cloud/discovery_engine/v1"
    
    ##
    # Snippet for the create_data_store call in the DataStoreService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DiscoveryEngine::V1::DataStoreService::Client#create_data_store.
    #
    def create_data_store
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DiscoveryEngine::V1::DataStoreService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DiscoveryEngine::V1::CreateDataStoreRequest.new
    
      # Call the create_data_store method.
      result = client.create_data_store request
    
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

### Import documents
    
    
    require "google/cloud/discovery_engine/v1"
    
    ##
    # Snippet for the import_documents call in the DocumentService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#import_documents.
    #
    def import_documents
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DiscoveryEngine::V1::DocumentService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DiscoveryEngine::V1::ImportDocumentsRequest.new
    
      # Call the import_documents method.
      result = client.import_documents request
    
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

### Connect to BigQuery with periodic syncing

Before importing your data, review [Prepare data for ingesting](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data).

The following procedure describes how to create a data connector that associates a BigQuery dataset with an Agent Search data connector and how to specify a table on the dataset for each data store you want to create. Data stores that are children of data connectors are called _entity_ data stores.

Data from the dataset is synced periodically to the entity data stores. You can specify synchronization daily, every three days, or every five days.

### Console

To use the Google Cloud console to create a connector that periodically syncs data from a BigQuery dataset to Agent Search, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. In the navigation menu, click **Data Stores**.

  3. Click **Create data store**.

  4. On the **Source** page, select **BigQuery**.

  5. Select the kind of data that you are importing.

  6. Click **Periodic**.

  7. Select the **Sync frequency** , how often you want the Agent Search connector to sync with the BigQuery dataset. You can change the frequency later.

  8. In the **BigQuery dataset path** field, click **Browse** , select the dataset that contains the tables that you have [prepared for ingesting](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data). Alternatively, enter the table location directly in the **BigQuery path** field. The format for the path is `projectname.datasetname`.

  9. In the **Tables to sync** field, click **Browse** , and then select a table that contains the data that you want for your data store.

**Note:** Make sure that the data in the tables matches the kind of data that you selected in step 5.  
If there is a mismatch you won't know until one of the following happens: 
     * You get errors when the connector tries to import data.
     * You see unexpected results. This happens if the selected type was structured but should have been unstructured or structured with metadata. The data is imported but the content URL or metadata is not recognized and is treated as a string.
  10. If there are additional tables in the dataset that that you want to use for data stores, click **Add table** and specify those tables too.

  11. Click **Continue**.

  12. Choose a region for your data store, enter a name for your data connector, and click **Create**.

You have now created a data connector, which will periodically sync data with the BigQuery dataset. And, you have created one or more entity data stores. The data stores have the same names as the BigQuery tables.

  13. To check the status of your ingestion, go to the **Data Stores** page and click your data connector name to see details about it on its **Data** page > **Data ingestion activity** tab. When the status column on the **Activity** tab changes from **In progress** to **succeeded** , the first ingestion is complete.

Depending on the size of your data, ingestion can take several minutes to several hours.




After you set up your data source and import data the first time, the data store syncs data from that source at a frequency that you select during setup. About an hour after the data connector is created, the first sync occurs. The next sync then occurs around 24 hours, 72 hours, or 120 hours later.

### Next steps

  * To attach your data store to an app, create an app and select your data store following the steps in [Create a custom recommendations app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-generic-recommendations-app).

  * To preview or get recommendations after your app and data store are set up, see [Get recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations).




## Cloud Storage

You can create data stores from Cloud Storage tables in two ways:

  * **One-time ingestion** : You import data from a Cloud Storage folder or file into a data store. The data in the data store doesn't change unless you manually [refresh the data](https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-data).

  * **Periodic ingestion** : You import data from a Cloud Storage folder or file, and you set a sync frequency that determines how often the data store is updated with the most recent data from that Cloud Storage location.




The following table compares the two ways that you can import Cloud Storage data into Agent Search data stores.

One-time ingestion | Periodic ingestion  
---|---  
Data must be refreshed manually. | Data updates automatically every one, three, or five days. Data cannot be manually refreshed.  
Agent Search creates a single data store from one folder or file in Cloud Storage.  | Agent Search creates a _data connector_ , and associates a data store (called an _entity_ data store) with it for the file or folder that is specified. Each Cloud Storage data connector can have a single entity data store.  
Data from multiple files, folders, and buckets can be combined in one data store by first ingesting data from one Cloud Storage location and then more data from another location.  | Because manual data import is not supported, the data in an entity data store can only be sourced from one Cloud Storage file or folder.  
Data source access control is supported. For more information, see [Data source access control](https://docs.cloud.google.com/generative-ai-app-builder/docs/data-source-access-control). | Data source access control is not supported. The imported data can contain access controls but these controls won't be respected.  
You can create a data store using either the Google Cloud console or the API. | You must use the console to create data connectors and their entity data stores.   
CMEK-compliant. | CMEK-compliant.  
  
### Before you begin

To import data from a source Google Cloud project that's different from the Google Cloud project with the Agent Search data store, grant the following Identity and Access Management (IAM) roles to the `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com` service account in the project that contains the Agent Search data store:

  * [Storage Object Admin (`roles/storage.objectAdmin`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)
  * [Storage Object Viewer (`roles/storage.objectViewer`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)

**Caution:** When you import data from Cloud Storage into an Agent Search data store, Cloud Storage permissions aren't imported with the data. After import, any user with [sufficient Agent Search permissions](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-control#roles) can view the data, even if they don't have permission to view the data in Cloud Storage.

### Import once from Cloud Storage

To ingest data from Cloud Storage, use the following steps to create a data store and ingest data using either the Google Cloud console or the API.

Before importing your data, review [Prepare data for ingesting](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#unstructured).

**Note:** Data import is recursive. That is, if there are folders within the bucket or folder that you specify, files within those folders are imported.

### Console

To use the console to ingest data from a Cloud Storage bucket, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Go to the **Data Stores** page.

  3. Click add **Create data store**.

  4. On the **Source** page, select **Cloud Storage**.

  5. In the **Select a folder or file you want to import** section, select **Folder** or **File**.

  6. Click **Browse** and choose the data you have [prepared for ingesting](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data), and then click **Select**. Alternatively, enter the location directly in the **`gs://`** field.

  7. Select what kind of data you are importing.

  8. Click **Continue**.

  9. If you are doing one-time import of structured data:

     1. Map fields to key properties.

     2. If there are important fields missing from the schema, use **Add new field** to add them.

For more information, see [About auto-detect and edit](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema#about-auto-and-edit).

     3. Click **Continue**.

  10. Choose a region for your data store.

  11. Enter a name for your data store.

  12. Optional: If you selected unstructured documents, you can select parsing and chunking options for your documents. To compare parsers, see [Parse documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#parsing). For information about chunking see [Chunk documents for RAG](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#parse-chunk-rag).

The [OCR parser](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#parsing-pdfs) and [layout parser](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#layout-parsing) can incur additional costs. See [Document AI feature pricing](https://docs.cloud.google.com/generative-ai-app-builder/pricing#document_ai_feature_pricing).

To select a parser, expand **Document processing options** and specify the parser options that you want to use.

  13. Click **Create**.

  14. To check the status of your ingestion, go to the **Data Stores** page and click your data store name to see details about it on its **Data** page. When the status column on the **Activity** tab changes from **In progress** to **Import completed** , the ingestion is complete.

Depending on the size of your data, ingestion can take several minutes or several hours.




### REST

To use the command line to create a data store and ingest data from Cloud Storage, follow these steps.

**Note:** If you are importing structured data and want to specify a schema instead of letting Agent Search auto-detect the schema for you, do the steps in [Provide your own schema as a JSON object](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema#provide-your-own) and then begin the following procedure at step 2.

  1. Create a data store.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
         -d '{
           "displayName": "DATA_STORE_DISPLAY_NAME",
           "industryVertical": "GENERIC",
           "solutionTypes": ["SOLUTION_TYPE_RECOMMENDATION"]
         }'
         

**Note:** The industry vertical `GENERIC` is used to create structured, unstructured, and website data stores for custom recommendations apps. 

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store that you want to create. This ID can contain only lowercase letters, digits, underscores, and hyphens.
     * `DATA_STORE_DISPLAY_NAME`: the display name of the Agent Search data store that you want to create.
  2. Import data from Cloud Storage.
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:import" \
           -d '{
             "gcsSource": {
               "inputUris": ["INPUT_FILE_PATTERN_1", "INPUT_FILE_PATTERN_2"],
               "dataSchema": "DATA_SCHEMA",
             },
             "reconciliationMode": "RECONCILIATION_MODE",
             "autoGenerateIds": "AUTO_GENERATE_IDS",
             "idField": "ID_FIELD",
             "errorConfig": {
               "gcsPrefix": "ERROR_DIRECTORY"
             }
           }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the Agent Search data store.
     * `INPUT_FILE_PATTERN`: a file pattern in Cloud Storage containing your documents.

For structured data or for unstructured data with metadata, an example of the input file pattern is `gs://<your-gcs-bucket>/directory/object.json`and an example of pattern matching one or more files is `gs://<your-gcs-bucket>/directory/*.json`.

For unstructured documents, an example is `gs://<your-gcs-bucket>/directory/*.pdf`. Each file that is matched by the pattern becomes a document.

If `<your-gcs-bucket>` is not under PROJECT_ID, you need to give the service account `service-<project number>@gcp-sa-discoveryengine.iam.gserviceaccount.com` "Storage Object Viewer" permissions for the Cloud Storage bucket. For example, if you are importing a Cloud Storage bucket from source project "123" to destination project "456", give `service-456@gcp-sa-discoveryengine.iam.gserviceaccount.com` permissions on the Cloud Storage bucket under project "123".

     * `DATA_SCHEMA`: optional. Values are `document`, `custom`, `csv`, and `content`. The default is `document`.

       * `document`: Upload unstructured data with metadata for unstructured documents. Each line of the file has to follow one of the following formats. You can define the ID of each document:

         * `{ "id": "<your-id>", "jsonData": "<JSON string>", "content": { "mimeType": "<application/pdf or text/html>", "uri": "gs://<your-gcs-bucket>/directory/filename.pdf" } }`
         * `{ "id": "<your-id>", "structData": <JSON object>, "content": { "mimeType": "<application/pdf or text/html>", "uri": "gs://<your-gcs-bucket>/directory/filename.pdf" } }`
       * `custom`: Upload JSON for structured documents. The data is organized according to a schema. You can specify the schema; otherwise it is auto-detected. You can put the JSON string of the document in a consistent format directly in each line, and Agent Search automatically generates the IDs for each document imported.

       * `content`: Upload unstructured documents (PDF, HTML, DOC, TXT, PPTX). The ID of each document is automatically generated as the first 128 bits of SHA256(GCS_URI) encoded as a hex string. You can specify multiple input file patterns as long as the matched files don't exceed the 100K files limit.

       * `csv`: Include a header row in your CSV file, with each header mapped to a document field. Specify the path to the CSV file using the `inputUris` field.

     * `ERROR_DIRECTORY`: optional. A Cloud Storage directory for error information about the import—for example, `gs://<your-gcs-bucket>/directory/import_errors`. Google recommends leaving this field empty to let Agent Search automatically create a temporary directory.

     * `RECONCILIATION_MODE`: optional. Values are `FULL` and `INCREMENTAL`. Default is `INCREMENTAL`. Specifying `INCREMENTAL` causes an incremental refresh of data from Cloud Storage to your data store. This does an upsert operation, which adds new documents and replaces existing documents with updated documents with the same ID. Specifying `FULL` causes a full rebase of the documents in your data store. In other words, new and updated documents are added to your data store, and documents that are not in Cloud Storage are removed from your data store. The `FULL` mode is helpful if you want to automatically delete documents that you no longer need.

     * `AUTO_GENERATE_IDS`: optional. Specifies whether to automatically generate document IDs. If set to `true`, document IDs are generated based on a hash of the payload. Note that generated document IDs might not remain consistent over multiple imports. If you auto-generate IDs over multiple imports, Google highly recommends setting `reconciliationMode` to `FULL` to maintain consistent document IDs.

Specify `autoGenerateIds` only when `gcsSource.dataSchema` is set to `custom` or `csv`. Otherwise, an `INVALID_ARGUMENT` error is returned. If you don't specify `autoGenerateIds` or set it to `false`, you must specify `idField`. Otherwise, the documents fail to import.

     * `ID_FIELD`: optional. Specifies which fields are the document IDs. For Cloud Storage source documents, `idField` specifies the name in the JSON fields that are document IDs. For example, if `{"my_id":"some_uuid"}` is the document ID field in one of your documents, specify `"idField":"my_id"`. This identifies all JSON fields with the name `"my_id"` as document IDs.

Specify this field only when: (1) `gcsSource.dataSchema` is set to `custom` or `csv`, and (2) `auto_generate_ids` is set to `false` or is unspecified. Otherwise, an `INVALID_ARGUMENT` error is returned.

Note that the value of the Cloud Storage JSON field must be of string type, must be between 1-63 characters, and must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034). Otherwise, the documents fail to import.

Note that the JSON field name specified by `id_field` must be of string type, must be between 1 and 63 characters, and must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034). Otherwise, the documents fail to import.




### C#

For more information, see the [Agent Search C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

### Create a data store
    
    
    using [Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedDataStoreServiceClientSnippets
    {
        /// <summary>Snippet for CreateDataStore</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void CreateDataStoreRequestObject()
        {
            // Create client
            [DataStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStoreServiceClient.html) dataStoreServiceClient = [DataStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStoreServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStoreServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DataStoreServiceClient_Create)();
            // Initialize request argument(s)
            [CreateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CreateDataStoreRequest.html) request = new [CreateDataStoreRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CreateDataStoreRequest.html)
            {
                ParentAsCollectionName = [CollectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CollectionName.html).[FromProjectLocationCollection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CollectionName.html#Google_Cloud_DiscoveryEngine_V1_CollectionName_FromProjectLocationCollection_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[COLLECTION]"),
                DataStore = new [DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStore.html)(),
                DataStoreId = "",
                CreateAdvancedSiteSearch = false,
                CmekConfigNameAsCmekConfigName = [CmekConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CmekConfigName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.CmekConfigName.html#Google_Cloud_DiscoveryEngine_V1_CmekConfigName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                SkipDefaultSchemaCreation = false,
            };
            // Make the request
            Operation<DataStore, CreateDataStoreMetadata> response = dataStoreServiceClient.[CreateDataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStoreServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DataStoreServiceClient_CreateDataStore_Google_Cloud_DiscoveryEngine_V1_CollectionName_Google_Cloud_DiscoveryEngine_V1_DataStore_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<DataStore, CreateDataStoreMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStore.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<DataStore, CreateDataStoreMetadata> retrievedResponse = dataStoreServiceClient.[PollOnceCreateDataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStoreServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DataStoreServiceClient_PollOnceCreateDataStore_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DataStore.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Import documents
    
    
    using [Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedDocumentServiceClientSnippets
    {
        /// <summary>Snippet for ImportDocuments</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void ImportDocumentsRequestObject()
        {
            // Create client
            [DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html) documentServiceClient = [DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DocumentServiceClient_Create)();
            // Initialize request argument(s)
            [ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsRequest.html) request = new [ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsRequest.html)
            {
                ParentAsBranchName = [BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BranchName.html).[FromProjectLocationDataStoreBranch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BranchName.html#Google_Cloud_DiscoveryEngine_V1_BranchName_FromProjectLocationDataStoreBranch_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
                InlineSource = new ImportDocumentsRequest.Types.InlineSource(),
                ErrorConfig = new [ImportErrorConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportErrorConfig.html)(),
                ReconciliationMode = [ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsRequest.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsRequest.Types.html).[ReconciliationMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsRequest.Types.ReconciliationMode.html).[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsRequest.Types.ReconciliationMode.html#Google_Cloud_DiscoveryEngine_V1_ImportDocumentsRequest_Types_ReconciliationMode_Unspecified),
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
                AutoGenerateIds = false,
                IdField = "",
                ForceRefreshContent = false,
            };
            // Make the request
            Operation<ImportDocumentsResponse, ImportDocumentsMetadata> response = documentServiceClient.[ImportDocuments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DocumentServiceClient_ImportDocuments_Google_Cloud_DiscoveryEngine_V1_ImportDocumentsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<ImportDocumentsResponse, ImportDocumentsMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [ImportDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsResponse.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<ImportDocumentsResponse, ImportDocumentsMetadata> retrievedResponse = documentServiceClient.[PollOnceImportDocuments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DocumentServiceClient_PollOnceImportDocuments_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [ImportDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ImportDocumentsResponse.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

For more information, see the [Agent Search Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

### Create a data store
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	discoveryengine "cloud.google.com/go/discoveryengine/apiv1"
    	discoveryenginepb "cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := discoveryengine.[NewDataStoreClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1.html#cloud_google_com_go_discoveryengine_apiv1_DataStoreClient_NewDataStoreClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &discoveryenginepb.CreateDataStoreRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#CreateDataStoreRequest.
    	}
    	op, err := c.CreateDataStore(ctx, req)
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
    

### Import documents
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	discoveryengine "cloud.google.com/go/discoveryengine/apiv1"
    	discoveryenginepb "cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := discoveryengine.[NewDocumentClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1.html#cloud_google_com_go_discoveryengine_apiv1_DocumentClient_NewDocumentClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &discoveryenginepb.ImportDocumentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#ImportDocumentsRequest.
    	}
    	op, err := c.ImportDocuments(ctx, req)
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

For more information, see the [Agent Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/overview). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

### Create a data store
    
    
    import com.google.cloud.discoveryengine.v1.[CollectionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CollectionName.html);
    import com.google.cloud.discoveryengine.v1.[CreateDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest.html);
    import com.google.cloud.discoveryengine.v1.[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore.html);
    import com.google.cloud.discoveryengine.v1.[DataStoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient.html);
    
    public class SyncCreateDataStore {
    
      public static void main(String[] args) throws Exception {
        syncCreateDataStore();
      }
    
      public static void syncCreateDataStore() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataStoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient.html) dataStoreServiceClient = [DataStoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient.html).create()) {
          [CreateDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest.html) request =
              [CreateDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest.html).newBuilder()
                  .setParent([CollectionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CollectionName.html).of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
                  .setDataStore([DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore.html).newBuilder().build())
                  .[setDataStoreId](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest.Builder.html#com_google_cloud_discoveryengine_v1_CreateDataStoreRequest_Builder_setDataStoreId_java_lang_String_)("dataStoreId929489618")
                  .[setCreateAdvancedSiteSearch](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest.Builder.html#com_google_cloud_discoveryengine_v1_CreateDataStoreRequest_Builder_setCreateAdvancedSiteSearch_boolean_)(true)
                  .[setSkipDefaultSchemaCreation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest.Builder.html#com_google_cloud_discoveryengine_v1_CreateDataStoreRequest_Builder_setSkipDefaultSchemaCreation_boolean_)(true)
                  .build();
          [DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore.html) response = dataStoreServiceClient.[createDataStoreAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient.html#com_google_cloud_discoveryengine_v1_DataStoreServiceClient_createDataStoreAsync__org_jspecify_annotations_Nullable_com_google_cloud_discoveryengine_v1_CollectionName_com_google_cloud_discoveryengine_v1_DataStore_java_lang_String_)(request).get();
        }
      }
    }

### Import documents
    
    
    import com.google.cloud.discoveryengine.v1.[BranchName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BranchName.html);
    import com.google.cloud.discoveryengine.v1.[DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.html);
    import com.google.cloud.discoveryengine.v1.[ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest.html);
    import com.google.cloud.discoveryengine.v1.[ImportDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsResponse.html);
    import com.google.cloud.discoveryengine.v1.[ImportErrorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportErrorConfig.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    
    public class SyncImportDocuments {
    
      public static void main(String[] args) throws Exception {
        syncImportDocuments();
      }
    
      public static void syncImportDocuments() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.html) documentServiceClient = [DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.html).create()) {
          [ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest.html) request =
              [ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest.html).newBuilder()
                  .setParent(
                      [BranchName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BranchName.html).[ofProjectLocationDataStoreBranchName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BranchName.html#com_google_cloud_discoveryengine_v1_BranchName_ofProjectLocationDataStoreBranchName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(
                              "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                          .toString())
                  .setErrorConfig([ImportErrorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportErrorConfig.html).newBuilder().build())
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().build())
                  .[setAutoGenerateIds](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest.Builder.html#com_google_cloud_discoveryengine_v1_ImportDocumentsRequest_Builder_setAutoGenerateIds_boolean_)(true)
                  .[setIdField](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest.Builder.html#com_google_cloud_discoveryengine_v1_ImportDocumentsRequest_Builder_setIdField_java_lang_String_)("idField1629396127")
                  .[setForceRefreshContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsRequest.Builder.html#com_google_cloud_discoveryengine_v1_ImportDocumentsRequest_Builder_setForceRefreshContent_boolean_)(true)
                  .build();
          [ImportDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportDocumentsResponse.html) response = documentServiceClient.[importDocumentsAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.html#com_google_cloud_discoveryengine_v1_DocumentServiceClient_importDocumentsAsync_com_google_cloud_discoveryengine_v1_ImportDocumentsRequest_)(request).get();
        }
      }
    }

### Node.js

For more information, see the [Agent Search Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

### Create a data store
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Resource name of the CmekConfig to use for protecting this DataStore.
     */
    // const cmekConfigName = 'abc123'
    /**
     *  DataStore without CMEK protections. If a default CmekConfig is set for
     *  the project, setting this field will override the default CmekConfig as
     *  well.
     */
    // const disableCmek = true
    /**
     *  Required. The parent resource name, such as
     *  `projects/{project}/locations/{location}/collections/{collection}`.
     */
    // const parent = 'abc123'
    /**
     *  Required. The DataStore google.cloud.discoveryengine.v1.DataStore  to
     *  create.
     */
    // const dataStore = {}
    /**
     *  Required. The ID to use for the
     *  DataStore google.cloud.discoveryengine.v1.DataStore, which will become
     *  the final component of the
     *  DataStore google.cloud.discoveryengine.v1.DataStore's resource name.
     *  This field must conform to RFC-1034 (https://tools.ietf.org/html/rfc1034)
     *  standard with a length limit of 63 characters. Otherwise, an
     *  INVALID_ARGUMENT error is returned.
     */
    // const dataStoreId = 'abc123'
    /**
     *  A boolean flag indicating whether user want to directly create an advanced
     *  data store for site search.
     *  If the data store is not configured as site
     *  search (GENERIC vertical and PUBLIC_WEBSITE content_config), this flag will
     *  be ignored.
     */
    // const createAdvancedSiteSearch = true
    /**
     *  A boolean flag indicating whether to skip the default schema creation for
     *  the data store. Only enable this flag if you are certain that the default
     *  schema is incompatible with your use case.
     *  If set to true, you must manually create a schema for the data store before
     *  any documents can be ingested.
     *  This flag cannot be specified if `data_store.starting_schema` is specified.
     */
    // const skipDefaultSchemaCreation = true
    
    // Imports the Discoveryengine library
    const {DataStoreServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1;
    
    // Instantiates a client
    const discoveryengineClient = new [DataStoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
    async function callCreateDataStore() {
      // Construct request
      const request = {
        parent,
        dataStore,
        dataStoreId,
      };
    
      // Run request
      const [operation] = await discoveryengineClient.createDataStore(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callCreateDataStore();

### Import documents
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  The Inline source for the input content for documents.
     */
    // const inlineSource = {}
    /**
     *  Cloud Storage location for the input content.
     */
    // const gcsSource = {}
    /**
     *  BigQuery input source.
     */
    // const bigquerySource = {}
    /**
     *  FhirStore input source.
     */
    // const fhirStoreSource = {}
    /**
     *  Spanner input source.
     */
    // const spannerSource = {}
    /**
     *  Cloud SQL input source.
     */
    // const cloudSqlSource = {}
    /**
     *  Firestore input source.
     */
    // const firestoreSource = {}
    /**
     *  AlloyDB input source.
     */
    // const alloyDbSource = {}
    /**
     *  Cloud Bigtable input source.
     */
    // const bigtableSource = {}
    /**
     *  Required. The parent branch resource name, such as
     *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.
     *  Requires create/update permission.
     */
    // const parent = 'abc123'
    /**
     *  The desired location of errors incurred during the Import.
     */
    // const errorConfig = {}
    /**
     *  The mode of reconciliation between existing documents and the documents to
     *  be imported. Defaults to
     *  ReconciliationMode.INCREMENTAL google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode.INCREMENTAL.
     */
    // const reconciliationMode = {}
    /**
     *  Indicates which fields in the provided imported documents to update. If
     *  not set, the default is to update all fields.
     */
    // const updateMask = {}
    /**
     *  Whether to automatically generate IDs for the documents if absent.
     *  If set to `true`,
     *  Document.id google.cloud.discoveryengine.v1.Document.id s are
     *  automatically generated based on the hash of the payload, where IDs may not
     *  be consistent during multiple imports. In which case
     *  ReconciliationMode.FULL google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode.FULL 
     *  is highly recommended to avoid duplicate contents. If unset or set to
     *  `false`, Document.id google.cloud.discoveryengine.v1.Document.id s have
     *  to be specified using
     *  id_field google.cloud.discoveryengine.v1.ImportDocumentsRequest.id_field,
     *  otherwise, documents without IDs fail to be imported.
     *  Supported data sources:
     *  * GcsSource google.cloud.discoveryengine.v1.GcsSource.
     *  GcsSource.data_schema google.cloud.discoveryengine.v1.GcsSource.data_schema 
     *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
     *  * BigQuerySource google.cloud.discoveryengine.v1.BigQuerySource.
     *  BigQuerySource.data_schema google.cloud.discoveryengine.v1.BigQuerySource.data_schema 
     *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
     *  * SpannerSource google.cloud.discoveryengine.v1.SpannerSource.
     *  * CloudSqlSource google.cloud.discoveryengine.v1.CloudSqlSource.
     *  * FirestoreSource google.cloud.discoveryengine.v1.FirestoreSource.
     *  * BigtableSource google.cloud.discoveryengine.v1.BigtableSource.
     */
    // const autoGenerateIds = true
    /**
     *  The field indicates the ID field or column to be used as unique IDs of
     *  the documents.
     *  For GcsSource google.cloud.discoveryengine.v1.GcsSource  it is the key of
     *  the JSON field. For instance, `my_id` for JSON `{"my_id": "some_uuid"}`.
     *  For others, it may be the column name of the table where the unique ids are
     *  stored.
     *  The values of the JSON field or the table column are used as the
     *  Document.id google.cloud.discoveryengine.v1.Document.id s. The JSON field
     *  or the table column must be of string type, and the values must be set as
     *  valid strings conform to RFC-1034 (https://tools.ietf.org/html/rfc1034)
     *  with 1-63 characters. Otherwise, documents without valid IDs fail to be
     *  imported.
     *  Only set this field when
     *  auto_generate_ids google.cloud.discoveryengine.v1.ImportDocumentsRequest.auto_generate_ids 
     *  is unset or set as `false`. Otherwise, an INVALID_ARGUMENT error is thrown.
     *  If it is unset, a default value `_id` is used when importing from the
     *  allowed data sources.
     *  Supported data sources:
     *  * GcsSource google.cloud.discoveryengine.v1.GcsSource.
     *  GcsSource.data_schema google.cloud.discoveryengine.v1.GcsSource.data_schema 
     *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
     *  * BigQuerySource google.cloud.discoveryengine.v1.BigQuerySource.
     *  BigQuerySource.data_schema google.cloud.discoveryengine.v1.BigQuerySource.data_schema 
     *  must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
     *  * SpannerSource google.cloud.discoveryengine.v1.SpannerSource.
     *  * CloudSqlSource google.cloud.discoveryengine.v1.CloudSqlSource.
     *  * FirestoreSource google.cloud.discoveryengine.v1.FirestoreSource.
     *  * BigtableSource google.cloud.discoveryengine.v1.BigtableSource.
     */
    // const idField = 'abc123'
    /**
     *  Optional. Whether to force refresh the unstructured content of the
     *  documents.
     *  If set to `true`, the content part of the documents will be refreshed
     *  regardless of the update status of the referencing content.
     */
    // const forceRefreshContent = true
    
    // Imports the Discoveryengine library
    const {DocumentServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1;
    
    // Instantiates a client
    const discoveryengineClient = new [DocumentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
    async function callImportDocuments() {
      // Construct request
      const request = {
        parent,
      };
    
      // Run request
      const [operation] = await discoveryengineClient.importDocuments(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callImportDocuments();

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

### Create a data store
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION" # Values: "global"
    # data_store_id = "YOUR_DATA_STORE_ID"
    
    
    def create_data_store_sample(
        project_id: str,
        location: str,
        data_store_id: str,
    ) -> str:
        #  For more information, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
        client_options = (
            ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
            if location != "global"
            else None
        )
    
        # Create a client
        client = discoveryengine.[DataStoreServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceClient.html)(client_options=client_options)
    
        # The full resource name of the collection
        # e.g. projects/{project}/locations/{location}/collections/default_collection
        parent = client.[collection_path](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceClient.html#google_cloud_discoveryengine_v1_services_data_store_service_DataStoreServiceClient_collection_path)(
            project=project_id,
            location=location,
            collection="default_collection",
        )
    
        data_store = discoveryengine.[DataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore.html)(
            display_name="My Data Store",
            # Options: GENERIC, MEDIA, HEALTHCARE_FHIR
            industry_vertical=discoveryengine.[IndustryVertical](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.IndustryVertical.html).GENERIC,
            # Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
            solution_types=[discoveryengine.[SolutionType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SolutionType.html).SOLUTION_TYPE_SEARCH],
            # TODO(developer): Update content_config based on data store type.
            # Options: NO_CONTENT, CONTENT_REQUIRED, PUBLIC_WEBSITE
            content_config=discoveryengine.[DataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore.html).[ContentConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore.ContentConfig.html).CONTENT_REQUIRED,
        )
    
        request = discoveryengine.[CreateDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateDataStoreRequest.html)(
            parent=parent,
            data_store_id=data_store_id,
            data_store=data_store,
            # Optional: For Advanced Site Search Only
            # create_advanced_site_search=True,
        )
    
        # Make the request
        operation = client.[create_data_store](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceClient.html#google_cloud_discoveryengine_v1_services_data_store_service_DataStoreServiceClient_create_data_store)(request=request)
    
        print(f"Waiting for operation to complete: {operation.operation.name}")
        response = operation.result()
    
        # After the operation is complete,
        # get information from operation metadata
        metadata = discoveryengine.[CreateDataStoreMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateDataStoreMetadata.html)(operation.metadata)
    
        # Handle the response
        print(response)
        print(metadata)
    
        return operation.operation.name
    
    

### Import documents
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION" # Values: "global"
    # data_store_id = "YOUR_DATA_STORE_ID"
    
    # Examples:
    # - Unstructured documents
    #   - `gs://bucket/directory/file.pdf`
    #   - `gs://bucket/directory/*.pdf`
    # - Unstructured documents with JSONL Metadata
    #   - `gs://bucket/directory/file.json`
    # - Unstructured documents with CSV Metadata
    #   - `gs://bucket/directory/file.csv`
    # gcs_uri = "YOUR_GCS_PATH"
    
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )
    
    # Create a client
    client = discoveryengine.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html)(client_options=client_options)
    
    # The full resource name of the search engine branch.
    # e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
    parent = client.[branch_path](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_branch_path)(
        project=project_id,
        location=location,
        data_store=data_store_id,
        branch="default_branch",
    )
    
    request = discoveryengine.[ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.html)(
        parent=parent,
        gcs_source=discoveryengine.[GcsSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GcsSource.html)(
            # Multiple URIs are supported
            input_uris=[gcs_uri],
            # Options:
            # - `content` - Unstructured documents (PDF, HTML, DOC, TXT, PPTX)
            # - `custom` - Unstructured documents with custom JSONL metadata
            # - `document` - Structured documents in the discoveryengine.Document format.
            # - `csv` - Unstructured documents with CSV metadata
            data_schema="content",
        ),
        # Options: `FULL`, `INCREMENTAL`
        reconciliation_mode=discoveryengine.[ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.html).[ReconciliationMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.ReconciliationMode.html).INCREMENTAL,
    )
    
    # Make the request
    operation = client.[import_documents](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_import_documents)(request=request)
    
    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()
    
    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.[ImportDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsMetadata.html)(operation.metadata)
    
    # Handle the response
    print(response)
    print(metadata)

### Ruby

For more information, see the [Agent Search Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

### Create a data store
    
    
    require "google/cloud/discovery_engine/v1"
    
    ##
    # Snippet for the create_data_store call in the DataStoreService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DiscoveryEngine::V1::DataStoreService::Client#create_data_store.
    #
    def create_data_store
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DiscoveryEngine::V1::DataStoreService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DiscoveryEngine::V1::CreateDataStoreRequest.new
    
      # Call the create_data_store method.
      result = client.create_data_store request
    
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

### Import documents
    
    
    require "google/cloud/discovery_engine/v1"
    
    ##
    # Snippet for the import_documents call in the DocumentService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#import_documents.
    #
    def import_documents
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DiscoveryEngine::V1::DocumentService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DiscoveryEngine::V1::ImportDocumentsRequest.new
    
      # Call the import_documents method.
      result = client.import_documents request
    
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

### Connect to Cloud Storage with periodic syncing

Before importing your data, review [Prepare data for ingesting](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data).

The following procedure describes how to create a data connector that associates a Cloud Storage location with an Agent Search data connector and how to specify a folder or file in that location for the data store that you want to create. Data stores that are children of data connectors are called _entity_ data stores.

Data is synced periodically to the entity data store. You can specify synchronization daily, every three days, or every five days.

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Go to the **Data Stores** page.

  3. Click **Create data store**.

  4. On the **Source** page, select **Cloud Storage**.

  5. Select what kind of data you are importing.

  6. Click **Periodic**.

  7. Select the **Synchronization frequency** , how often you want the Agent Search connector to sync with the Cloud Storage location. You can change the frequency later.

  8. In the **Select a folder or file you want to import** section, select **Folder** or **File**.

  9. Click **Browse** and choose the data you have [prepared for ingesting](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data), and then click **Select**. Alternatively, enter the location directly in the **`gs://`** field.

  10. Click **Continue**.

  11. Choose a region for your data connector.

  12. Enter a name for your data connector.

  13. Optional: If you selected unstructured documents, you can select parsing and chunking options for your documents. To compare parsers, see [Parse documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#parsing). For information about chunking see [Chunk documents for RAG](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#parse-chunk-rag).

To select a parser, expand **Document processing options** and specify the parser options that you want to use.

The [OCR parser](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#parsing-pdfs) and [layout parser](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#layout-parsing) can incur additional costs. See [Document AI feature pricing](https://docs.cloud.google.com/generative-ai-app-builder/pricing#document_ai_feature_pricing).

  14. Click **Create**.

You have now created a data connector, which will periodically sync data with the Cloud Storage location. You have also created an entity data store, which is named `gcs_store`.

  15. To check the status of your ingestion, go to the **Data Stores** page and click your data connector name to see details about it on its **Data** page

> **Data ingestion activity** tab. When the status column on the **Data ingestion activity** tab changes from **In progress** to **succeeded** , the first ingestion is complete.

Depending on the size of your data, ingestion can take several minutes to several hours.




After you set up your data source and import data the first time, data is synced from that source at a frequency that you select during setup. About an hour after the data connector is created, the first sync occurs. The next sync then occurs around 24 hours, 72 hours, or 120 hours later.

### Next steps

  * To attach your data store to an app, create an app and select your data store following the steps in [Create a custom recommendations app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-generic-recommendations-app).

  * To preview or get recommendations after your app and data store are set up, see [Get recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations).




## Upload structured JSON data with the API

To directly upload a JSON document or object using the API, follow these steps.

Before importing your data, [Prepare data for ingesting](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data).

### REST

To use the command line to create a data store and import structured JSON data, follow these steps:

  1. Create a data store.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID" \
         -d '{
           "displayName": "DATA_STORE_DISPLAY_NAME",
           "industryVertical": "GENERIC",
           "solutionTypes": ["SOLUTION_TYPE_RECOMMENDATION"]
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the recommendations data store that you want to create. This ID can contain only lowercase letters, digits, underscores, and hyphens.
     * `DATA_STORE_DISPLAY_NAME`: the display name of the recommendations data store that you want to create.
**Note:** The industry vertical `GENERIC` is used to create structured, unstructured, and website data stores for custom recommendations apps. 
  2. Optional: Provide your own schema. When you provide a schema, you typically get better results. For more information, see [Provide or auto-detect a schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema).
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/schemas/default_schema" \
         -d '{
           "structSchema": JSON_SCHEMA_OBJECT
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `DATA_STORE_ID`: the ID of the recommendations data store.
     * `JSON_SCHEMA_OBJECT`: your JSON schema as a JSON object—for example:
           
           {
             "$schema": "https://json-schema.org/draft/2020-12/schema",
             "type": "object",
             "properties": {
               "title": {
                 "type": "string",
                 "keyPropertyMapping": "title"
               },
               "categories": {
                 "type": "array",
                 "items": {
                   "type": "string",
                   "keyPropertyMapping": "category"
                 }
               },
               "uri": {
                 "type": "string",
                 "keyPropertyMapping": "uri"
               }
             }
           }
           

  3. Import structured data that conforms to the defined schema.

There are a few approaches that you can use to upload data, including:

     * Upload a JSON document.
           
           curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents?documentId=DOCUMENT_ID" \
           -d '{
             "jsonData": "JSON_DOCUMENT_STRING"
           }'
           

Replace `JSON_DOCUMENT_STRING` with the JSON document as a single string. This must conform to the JSON schema that you provided in the previous step—for example:
           
           ```none
           { \"title\": \"test title\", \"categories\": [\"cat_1\", \"cat_2\"], \"uri\": \"test uri\"}
           ```
           

     * Upload a JSON object.
           
           curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents?documentId=DOCUMENT_ID" \
           -d '{
             "structData": JSON_DOCUMENT_OBJECT
           }'
           

Replace `JSON_DOCUMENT_OBJECT` with the JSON document as a JSON object. This must conform to the JSON schema that you provided in the previous step—for example:
           
           ```json
           {
             "title": "test title",
             "categories": [
               "cat_1",
               "cat_2"
             ],
             "uri": "test uri"
           }
           ```
           

     * Update with a JSON document.
           
           curl -X PATCH \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents/DOCUMENT_ID" \
           -d '{
             "jsonData": "JSON_DOCUMENT_STRING"
           }'
           

     * Update with a JSON object.
           
           curl -X PATCH \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents/DOCUMENT_ID" \
           -d '{
             "structData": JSON_DOCUMENT_OBJECT
           }'
           




### Next steps

  * To attach your data store to an app, create an app and select your data store following the steps in [Create a custom recommendations app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-generic-recommendations-app).

  * To preview how your recommendations appear after your app and data store are set up, see [Get recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations).




## Create a data store using Terraform

You can use Terraform to create an empty data store. After the empty data store is created, you can ingest data into the data store using the Google Cloud console or API commands.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To create an empty data store using Terraform, see [` google_discovery_engine_data_store`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_engine_data_store).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
