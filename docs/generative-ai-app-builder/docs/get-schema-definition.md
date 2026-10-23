---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/get-schema-definition/
title: View a schema definition \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:37.206633+00:00
---

# View a schema definition  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/get-schema-definition/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  View a schema definition Stay organized with collections  Save and categorize content based on your preferences. 

You can view the schema for any data store containing data that supports a schema, such as [structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#structured-data), [website data with structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata), or [unstructured data with structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#unstructured-data).

You can view the schema in the Google Cloud console or by using the [`dataStores.schemas.get`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas/get) API method. Viewing the schema for a website is supported only over the REST API.

### Console

To view a schema in the Google Cloud console, follow these steps.

  1. If you are viewing an auto-generated schema, make sure that you have completed data ingestion. Otherwise, the schema might not be available yet.

  2. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  3. In the navigation menu, click **Data Stores**.

  4. In the **Name** column, click the data store with the schema that you want to view.

  5. Click the **Schema** tab to view the schema for your data.




### REST

To use the API to get the definition for your schema, follow these steps:

  1. If you are viewing an auto-generated schema, make sure that you have completed data ingestion. Otherwise, the schema might not be available yet.

To view the schema for data stores with websites or unstructured data with metadata, skip to Step 3 to call the `schema.get` method.

  2. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  3. Use the [`schemas.get`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas/get) API method to get your schema definition.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/schemas/default_schema"
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `DATA_STORE_ID`: the ID of your data store.



### C#

For more information, see the [Agent Search C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.html);
    
    public sealed partial class GeneratedSchemaServiceClientSnippets
    {
        /// <summary>Snippet for GetSchema</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void GetSchemaRequestObject()
        {
            // Create client
            [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html#Google_Cloud_DiscoveryEngine_V1_SchemaServiceClient_Create)();
            // Initialize request argument(s)
            [GetSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.GetSchemaRequest.html) request = new [GetSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.GetSchemaRequest.html)
            {
                SchemaName = [SchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaName.html).[FromProjectLocationDataStoreSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaName.html#Google_Cloud_DiscoveryEngine_V1_SchemaName_FromProjectLocationDataStoreSchema_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SCHEMA]"),
            };
            // Make the request
            [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Schema.html) response = schemaServiceClient.[GetSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html#Google_Cloud_DiscoveryEngine_V1_SchemaServiceClient_GetSchema_Google_Cloud_DiscoveryEngine_V1_GetSchemaRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
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
    
    	req := &discoveryenginepb.GetSchemaRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#GetSchemaRequest.
    	}
    	resp, err := c.GetSchema(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

For more information, see the [Agent Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/overview). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.discoveryengine.v1.[GetSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetSchemaRequest.html);
    import com.google.cloud.discoveryengine.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Schema.html);
    import com.google.cloud.discoveryengine.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaName.html);
    import com.google.cloud.discoveryengine.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaServiceClient.html);
    
    public class SyncGetSchema {
    
      public static void main(String[] args) throws Exception {
        syncGetSchema();
      }
    
      public static void syncGetSchema() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaServiceClient.html).create()) {
          [GetSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetSchemaRequest.html) request =
              [GetSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetSchemaRequest.html).newBuilder()
                  .setName(
                      [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaName.html).[ofProjectLocationDataStoreSchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaName.html#com_google_cloud_discoveryengine_v1_SchemaName_ofProjectLocationDataStoreSchemaName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(
                              "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SCHEMA]")
                          .toString())
                  .build();
          [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Schema.html) response = schemaServiceClient.getSchema(request);
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
    from google.cloud import [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest)
    
    
    def sample_get_schema():
        # Create a client
        client = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[SchemaServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.schema_service.SchemaServiceClient.html)()
    
        # Initialize request argument(s)
        request = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[GetSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetSchemaRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_schema](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.schema_service.SchemaServiceClient.html#google_cloud_discoveryengine_v1_services_schema_service_SchemaServiceClient_get_schema)(request=request)
    
        # Handle the response
        print(response)
    
    

### Ruby

For more information, see the [Agent Search Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/discovery_engine/v1"
    
    ##
    # Snippet for the get_schema call in the SchemaService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DiscoveryEngine::V1::SchemaService::Client#get_schema.
    #
    def get_schema
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DiscoveryEngine::V1::SchemaService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DiscoveryEngine::V1::GetSchemaRequest.new
    
      # Call the get_schema method.
      result = client.get_schema request
    
      # The returned object is of type Google::Cloud::DiscoveryEngine::V1::Schema.
      p result
    end

## What's next

  * [Provide or auto-detect a schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema)
  * [Update a schema for structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas)
  * [Delete a schema for structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-schemas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
