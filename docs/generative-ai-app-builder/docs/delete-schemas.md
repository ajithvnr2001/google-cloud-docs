---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-schemas/
title: Delete a schema for structured data \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:08.593956+00:00
---

# Delete a schema for structured data  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-schemas/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Delete a schema for structured data Stay organized with collections  Save and categorize content based on your preferences. 

You can only delete a schema if all of the documents associated with the schema are deleted. Otherwise, the attempt fails. After you delete a schema, you can call the `schemas.create` method to create a new one.

To delete a schema for structured data, follow these steps:

### REST

  1. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  2. Delete your schema.
         
         curl -X DELETE \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/schemas/default_schema"
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `DATA_STORE_ID`: the ID of your data store.



### C#

For more information, see the [Agent Search C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedSchemaServiceClientSnippets
    {
        /// <summary>Snippet for DeleteSchema</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void DeleteSchemaRequestObject()
        {
            // Create client
            [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html#Google_Cloud_DiscoveryEngine_V1_SchemaServiceClient_Create)();
            // Initialize request argument(s)
            [DeleteSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteSchemaRequest.html) request = new [DeleteSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DeleteSchemaRequest.html)
            {
                SchemaName = [SchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaName.html).[FromProjectLocationDataStoreSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaName.html#Google_Cloud_DiscoveryEngine_V1_SchemaName_FromProjectLocationDataStoreSchema_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SCHEMA]"),
            };
            // Make the request
            Operation<Empty, DeleteSchemaMetadata> response = schemaServiceClient.[DeleteSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html#Google_Cloud_DiscoveryEngine_V1_SchemaServiceClient_DeleteSchema_Google_Cloud_DiscoveryEngine_V1_DeleteSchemaRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<Empty, DeleteSchemaMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Empty, DeleteSchemaMetadata> retrievedResponse = schemaServiceClient.[PollOnceDeleteSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html#Google_Cloud_DiscoveryEngine_V1_SchemaServiceClient_PollOnceDeleteSchema_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

For more information, see the [Agent Search Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    	c, err := discoveryengine.[NewSchemaClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1.html#cloud_google_com_go_discoveryengine_apiv1_SchemaClient_NewSchemaClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &discoveryenginepb.DeleteSchemaRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#DeleteSchemaRequest.
    	}
    	op, err := c.DeleteSchema(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### Java

For more information, see the [Agent Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/overview). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.discoveryengine.v1.[DeleteSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSchemaRequest.html);
    import com.google.cloud.discoveryengine.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaName.html);
    import com.google.cloud.discoveryengine.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaServiceClient.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    
    public class SyncDeleteSchema {
    
      public static void main(String[] args) throws Exception {
        syncDeleteSchema();
      }
    
      public static void syncDeleteSchema() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaServiceClient.html).create()) {
          [DeleteSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSchemaRequest.html) request =
              [DeleteSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSchemaRequest.html).newBuilder()
                  .setName(
                      [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaName.html).[ofProjectLocationDataStoreSchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaName.html#com_google_cloud_discoveryengine_v1_SchemaName_ofProjectLocationDataStoreSchemaName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(
                              "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SCHEMA]")
                          .toString())
                  .build();
          schemaServiceClient.[deleteSchemaAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaServiceClient.html#com_google_cloud_discoveryengine_v1_SchemaServiceClient_deleteSchemaAsync__org_jspecify_annotations_Nullable_com_google_cloud_discoveryengine_v1_SchemaName_)(request).get();
        }
      }
    }

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    
    def sample_delete_schema():
        # Create a client
        client = discoveryengine_v1.[SchemaServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.schema_service.SchemaServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[DeleteSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteSchemaRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_schema](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.schema_service.SchemaServiceClient.html#google_cloud_discoveryengine_v1_services_schema_service_SchemaServiceClient_delete_schema)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### Ruby

For more information, see the [Agent Search Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/discovery_engine/v1"
    
    ##
    # Snippet for the delete_schema call in the SchemaService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DiscoveryEngine::V1::SchemaService::Client#delete_schema.
    #
    def delete_schema
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DiscoveryEngine::V1::SchemaService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DiscoveryEngine::V1::DeleteSchemaRequest.new
    
      # Call the delete_schema method.
      result = client.delete_schema request
    
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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
