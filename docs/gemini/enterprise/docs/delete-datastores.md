---
url: https://docs.cloud.google.com/gemini/enterprise/docs/delete-datastores/
title: Purge data from a first-party data store \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:17:41.621181+00:00
---

# Purge data from a first-party data store  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/delete-datastores/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Purge data from a first-party data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to purge all of the data in a structured or unstructured data store.

You purge the data in a data store if you want to completely delete the contents of the data store before re-importing fresh data. Purging a data store deletes only the data in the data store, leaving your app, schema, and configurations intact.

For how to delete a data store, see [Delete a datastore](https://docs.cloud.google.com/gemini/enterprise/docs/delete-a-data-store).

## Purge data

To purge data from a data store, do the following:

### Console

To use the Google Cloud console to purge the data from a branch of a structured or unstructured, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/apps)

  2. In the navigation menu, click **Data Stores**.

  3. In the **Name** column, click the data store that you want to purge.

  4. In the **Documents** tab, click delete **Purge data**.

  5. Read the warning in the **Confirm purge data** dialog. If you want to continue, enter the name of your data store, and then click **Confirm**. Purging data is a long-running operation. For more information, see [Monitor long-running operations](https://docs.cloud.google.com/gemini/enterprise/docs/long-running-operations).

  6. Click the **Activity** tab to monitor the progress of the purge operation. 




### REST

To use the command line to purge the data from a branch of a structured or unstructured data store, follow these steps:

  1. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gemini-enterprise/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  2. Call the [`documents.purge`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.branches.documents/purge) method.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/branches/0/documents:purge" \
         -d '{
           "filter": "*",
           "force": FORCE
         }'
         

Replace the following:

     * `PROJECT_ID`: Google Cloud project
     * `DATA_STORE_ID`: the ID of the data store.
     * `FORCE`: a boolean value that specifies whether to delete data from the branch of the data store. 
       * If `true`, deletes all data from the branch
       * If `false`, deletes no data and returns a list of documents in the branch.
       * If `force` is omitted, the default is `false`.
  3. Optional: Make note of the `name` value returned by the `documents.purge` method and follow the instructions in [Get details about a long-running operation](https://docs.cloud.google.com/gemini/enterprise/docs/long-running-operations#get-details) to see when the purge operation is complete.




### C#

Before trying this sample, follow the C# setup instructions in the [Gemini Enterprise quickstart using client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries). For more information, see the [Gemini Enterprise C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest). 

To authenticate to Gemini Enterprise, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedDocumentServiceClientSnippets
    {
        /// <summary>Snippet for PurgeDocuments</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void PurgeDocumentsRequestObject()
        {
            // Create client
            [DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html) documentServiceClient = [DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DocumentServiceClient_Create)();
            // Initialize request argument(s)
            [PurgeDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.PurgeDocumentsRequest.html) request = new [PurgeDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.PurgeDocumentsRequest.html)
            {
                ParentAsBranchName = [BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BranchName.html).[FromProjectLocationDataStoreBranch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.BranchName.html#Google_Cloud_DiscoveryEngine_V1_BranchName_FromProjectLocationDataStoreBranch_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
                Filter = "",
                Force = false,
                GcsSource = new [GcsSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.GcsSource.html)(),
                ErrorConfig = new [PurgeErrorConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.PurgeErrorConfig.html)(),
            };
            // Make the request
            Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> response = documentServiceClient.[PurgeDocuments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DocumentServiceClient_PurgeDocuments_Google_Cloud_DiscoveryEngine_V1_PurgeDocumentsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [PurgeDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.PurgeDocumentsResponse.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> retrievedResponse = documentServiceClient.[PollOncePurgeDocuments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentServiceClient.html#Google_Cloud_DiscoveryEngine_V1_DocumentServiceClient_PollOncePurgeDocuments_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [PurgeDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.PurgeDocumentsResponse.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Gemini Enterprise quickstart using client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries). For more information, see the [Gemini Enterprise Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1). 

To authenticate to Gemini Enterprise, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    	req := &discoveryenginepb.PurgeDocumentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#PurgeDocumentsRequest.
    	}
    	op, err := c.PurgeDocuments(ctx, req)
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

Before trying this sample, follow the Java setup instructions in the [Gemini Enterprise quickstart using client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries). For more information, see the [Gemini Enterprise Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/overview). 

To authenticate to Gemini Enterprise, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.discoveryengine.v1.[BranchName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BranchName.html);
    import com.google.cloud.discoveryengine.v1.[DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.html);
    import com.google.cloud.discoveryengine.v1.[PurgeDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeDocumentsRequest.html);
    import com.google.cloud.discoveryengine.v1.[PurgeDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeDocumentsResponse.html);
    import com.google.cloud.discoveryengine.v1.[PurgeErrorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeErrorConfig.html);
    
    public class SyncPurgeDocuments {
    
      public static void main(String[] args) throws Exception {
        syncPurgeDocuments();
      }
    
      public static void syncPurgeDocuments() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.html) documentServiceClient = [DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.html).create()) {
          [PurgeDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeDocumentsRequest.html) request =
              [PurgeDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeDocumentsRequest.html).newBuilder()
                  .setParent(
                      [BranchName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BranchName.html).[ofProjectLocationDataStoreBranchName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BranchName.html#com_google_cloud_discoveryengine_v1_BranchName_ofProjectLocationDataStoreBranchName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(
                              "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]")
                          .toString())
                  .setFilter("filter-1274492040")
                  .setErrorConfig([PurgeErrorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeErrorConfig.html).newBuilder().build())
                  .setForce(true)
                  .build();
          [PurgeDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeDocumentsResponse.html) response = documentServiceClient.[purgeDocumentsAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DocumentServiceClient.html#com_google_cloud_discoveryengine_v1_DocumentServiceClient_purgeDocumentsAsync_com_google_cloud_discoveryengine_v1_PurgeDocumentsRequest_)(request).get();
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Gemini Enterprise quickstart using client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries). For more information, see the [Gemini Enterprise Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest). 

To authenticate to Gemini Enterprise, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Cloud Storage location for the input content.
     *  Supported `data_schema`:
     *  * `document_id`: One valid
     *  Document.id google.cloud.discoveryengine.v1.Document.id  per line.
     */
    // const gcsSource = {}
    /**
     *  Inline source for the input content for purge.
     */
    // const inlineSource = {}
    /**
     *  Required. The parent resource name, such as
     *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.
     */
    // const parent = 'abc123'
    /**
     *  Required. Filter matching documents to purge. Only currently supported
     *  value is
     *  `*` (all items).
     */
    // const filter = 'abc123'
    /**
     *  The desired location of errors incurred during the purge.
     */
    // const errorConfig = {}
    /**
     *  Actually performs the purge. If `force` is set to false, return the
     *  expected purge count without deleting any documents.
     */
    // const force = true
    
    // Imports the Discoveryengine library
    const {DocumentServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1;
    
    // Instantiates a client
    const discoveryengineClient = new [DocumentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
    async function callPurgeDocuments() {
      // Construct request
      const request = {
        parent,
        filter,
      };
    
      // Run request
      const [operation] = await discoveryengineClient.purgeDocuments(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callPurgeDocuments();

### Python

Before trying this sample, follow the Python setup instructions in the [Gemini Enterprise quickstart using client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries). For more information, see the [Gemini Enterprise Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Gemini Enterprise, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION"            # Values: "global", "us", "eu"
    # data_store_id = "YOUR_DATA_STORE_ID"
    
    
    def purge_documents_sample(
        project_id: str, location: str, data_store_id: str
    ) -> discoveryengine.PurgeDocumentsMetadata:
        #  For more information, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
        client_options = (
            ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
            if location != "global"
            else None
        )
    
        # Create a client
        client = discoveryengine.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html)(client_options=client_options)
    
        operation = client.[purge_documents](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_purge_documents)(
            request=discoveryengine.[PurgeDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeDocumentsRequest.html)(
                # The full resource name of the search engine branch.
                # e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
                parent=client.[branch_path](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_branch_path)(
                    project=project_id,
                    location=location,
                    data_store=data_store_id,
                    branch="default_branch",
                ),
                filter="*",
                # If force is set to `False`, return the expected purge count without deleting any documents.
                force=True,
            )
        )
    
        print(f"Waiting for operation to complete: {operation.operation.name}")
        response = operation.result()
    
        # After the operation is complete,
        # get information from operation metadata
        metadata = discoveryengine.[PurgeDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeDocumentsMetadata.html)(operation.metadata)
    
        # Handle the response
        print(response)
        print(metadata)
    
        return metadata
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Gemini Enterprise quickstart using client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries). For more information, see the [Gemini Enterprise Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine/latest). 

To authenticate to Gemini Enterprise, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/discovery_engine/v1"
    
    ##
    # Snippet for the purge_documents call in the DocumentService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DiscoveryEngine::V1::DocumentService::Client#purge_documents.
    #
    def purge_documents
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DiscoveryEngine::V1::DocumentService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DiscoveryEngine::V1::PurgeDocumentsRequest.new
    
      # Call the purge_documents method.
      result = client.purge_documents request
    
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
