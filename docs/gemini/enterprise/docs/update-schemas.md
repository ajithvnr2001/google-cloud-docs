---
url: https://docs.cloud.google.com/gemini/enterprise/docs/update-schemas/
title: Update a schema \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:13:11.373640+00:00
---

# Update a schema  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/update-schemas/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Update a schema Stay organized with collections  Save and categorize content based on your preferences. 

You can update the schema [structured data](https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores#structured-data) and [unstructured data with metadata](https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores#unstructured-data) that supports a schema.

You can update the schema in the Google Cloud console or by using the [`schemas.patch`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas/patch) API method.

To update the schema, you can add new fields, change indexable, searchable, and retrievable annotations for a field, or mark a field as a key property, such as `title`, `uri` and `description`.

**Important:** Google strongly recommends that you update your schema with key property mappings, especially for `title`. This ensures that your results are displayed correctly and helps Gemini Enterprise identify important information that allows it to generate better results.

## Update your schema

You can update your schema in the Google Cloud console or using the API.

**Note:** Editing the schema indexes your data store again. For large data stores, indexing can take several hours.

### Console

To update a schema in the Google Cloud console, follow these steps:

  1. Review the Requirements and limitations section to check that your schema update is valid.

  2. If you are updating field annotations (setting fields as indexable, retrievable, dynamic facetable, searchable, or completable), review [Configure field settings](https://docs.cloud.google.com/gemini/enterprise/docs/configure-field-settings) for the limitations and requirements of each annotation type.

  3. Check that you have completed data ingestion. Otherwise, the schema might not be available to edit yet.

  4. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  5. In the navigation menu, click **Data Stores**.

  6. In the **Name** column, click the data store with the schema that you want to update.

  7. Click the **Schema** tab to view the schema for your data.

This tab might be empty if this is the first time you're editing the fields.

  8. Click the **Edit** button.

  9. Update your schema:

     * **Map key properties:** In the **Key properties** column of your schema, select a key property to map a field to. For example, if a field called `details` always contains the description of a document, map that field to the key property **Description**.

     * **Update number of dimensions (Advanced)** : You can update this setting if you are using custom vector embeddings with Gemini Enterprise. See [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings) in the Agent Search documentation.

     * **Update field annotations:** To update annotations for a field, select or deselect a field's annotation setting. Available annotations are **Retrievable** , **Indexable** , **Dynamic Facetable** , **Searchable** , and **Completable**. Some field settings have limitations. See [Configure field settings](https://docs.cloud.google.com/gemini/enterprise/docs/configure-field-settings) for descriptions and requirements for each annotation type.

     * **Add a new field:** Adding new fields to your schema before importing new documents with those fields can shorten the time it takes Gemini Enterprise to reindex your data after import.

       1. Click **Add new fields** to expand that section.

       2. Click add_box **Add node** and specify settings for the new field.

To indicate an array, set **Array** to **Yes**. For example, to add an array of strings, set **type** to `string` and **Array** to `Yes`.

  10. Click **Save** to apply your schema changes.

Changing the schema triggers reindexing. For large data stores, reindexing can take hours.




### REST

To use the API to update your schema, follow these steps:

  1. Review the Requirements and limitations and the Limitation examples (REST only) sections to check that your schema changes are valid.

To update the schema for data stores with unstructured data with metadata, skip to Step 5 to call the `schema.patch` method.

  2. If you are updating field annotations (setting fields as indexable, retrievable, dynamic facetable, or searchable), review [Configure field settings](https://docs.cloud.google.com/gemini/enterprise/docs/configure-field-settings) for the limitations and requirements of each annotation type.

  3. If you are editing an auto-detected schema, make sure that you have completed data ingestion. Otherwise, the schema might not be available to edit yet.

  4. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gemini-enterprise/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  5. Use the [schemas.patch](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas/patch) API method to provide your new JSON schema as a JSON object.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/collections/default_collection/dataStores/DATA_STORE_ID/schemas/default_schema" \
         -d '{
           "structSchema": JSON_SCHEMA_OBJECT
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `DATA_STORE_ID`: the ID of the data store.
     * `JSON_SCHEMA_OBJECT`: your new JSON schema as a JSON object. For example:
           
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

#### Example command and result
           
           curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/dataStores/my-data-store/schemas/default_schema" -d '{
           "structSchema": {
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
           }'
           
           
           * * *
           
           
           {
           "name": "projects/123456/locations/global/collections/default_collection/dataStores/my-data-store/schemas/default_schema/operations/update-schema-10569824819404198922",
           "metadata": {
           "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.UpdateSchemaMetadata"
           }
           }
           

  6. Optional: Review the schema by following the procedure [View a schema definition](https://docs.cloud.google.com/gemini/enterprise/docs/get-schema-definition).




### C#

Before trying this sample, follow the C# setup instructions in the [Gemini Enterprise quickstart using client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries). For more information, see the [Gemini Enterprise C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest). 

To authenticate to Gemini Enterprise, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedSchemaServiceClientSnippets
    {
        /// <summary>Snippet for UpdateSchema</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void UpdateSchemaRequestObject()
        {
            // Create client
            [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html#Google_Cloud_DiscoveryEngine_V1_SchemaServiceClient_Create)();
            // Initialize request argument(s)
            [UpdateSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UpdateSchemaRequest.html) request = new [UpdateSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.UpdateSchemaRequest.html)
            {
                Schema = new [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Schema.html)(),
                AllowMissing = false,
            };
            // Make the request
            Operation<Schema, UpdateSchemaMetadata> response = schemaServiceClient.[UpdateSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html#Google_Cloud_DiscoveryEngine_V1_SchemaServiceClient_UpdateSchema_Google_Cloud_DiscoveryEngine_V1_UpdateSchemaRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<Schema, UpdateSchemaMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Schema.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Schema, UpdateSchemaMetadata> retrievedResponse = schemaServiceClient.[PollOnceUpdateSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SchemaServiceClient.html#Google_Cloud_DiscoveryEngine_V1_SchemaServiceClient_PollOnceUpdateSchema_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Schema.html) retrievedResult = retrievedResponse.Result;
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
    	c, err := discoveryengine.[NewSchemaClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/discoveryengine/latest/apiv1.html#cloud_google_com_go_discoveryengine_apiv1_SchemaClient_NewSchemaClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &discoveryenginepb.UpdateSchemaRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/discoveryengine/apiv1/discoveryenginepb#UpdateSchemaRequest.
    	}
    	op, err := c.UpdateSchema(ctx, req)
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
    
    
    import com.google.cloud.discoveryengine.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Schema.html);
    import com.google.cloud.discoveryengine.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaServiceClient.html);
    import com.google.cloud.discoveryengine.v1.[UpdateSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateSchemaRequest.html);
    
    public class SyncUpdateSchema {
    
      public static void main(String[] args) throws Exception {
        syncUpdateSchema();
      }
    
      public static void syncUpdateSchema() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaServiceClient.html) schemaServiceClient = [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaServiceClient.html).create()) {
          [UpdateSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateSchemaRequest.html) request =
              [UpdateSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateSchemaRequest.html).newBuilder()
                  .setSchema([Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Schema.html).newBuilder().build())
                  .setAllowMissing(true)
                  .build();
          [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Schema.html) response = schemaServiceClient.[updateSchemaAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SchemaServiceClient.html#com_google_cloud_discoveryengine_v1_SchemaServiceClient_updateSchemaAsync_com_google_cloud_discoveryengine_v1_UpdateSchemaRequest_)(request).get();
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Gemini Enterprise quickstart using client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries). For more information, see the [Gemini Enterprise Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Gemini Enterprise, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    
    def sample_update_schema():
        # Create a client
        client = discoveryengine_v1.[SchemaServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.schema_service.SchemaServiceClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[UpdateSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateSchemaRequest.html)()
    
        # Make the request
        operation = client.[update_schema](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.schema_service.SchemaServiceClient.html#google_cloud_discoveryengine_v1_services_schema_service_SchemaServiceClient_update_schema)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Gemini Enterprise quickstart using client libraries](https://docs.cloud.google.com/gemini/enterprise/docs/libraries). For more information, see the [Gemini Enterprise Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine/latest). 

To authenticate to Gemini Enterprise, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/discovery_engine/v1"
    
    ##
    # Snippet for the update_schema call in the SchemaService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::DiscoveryEngine::V1::SchemaService::Client#update_schema.
    #
    def update_schema
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::DiscoveryEngine::V1::SchemaService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::DiscoveryEngine::V1::UpdateSchemaRequest.new
    
      # Call the update_schema method.
      result = client.update_schema request
    
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

## Requirements and limitations

When updating a schema, be sure that the new schema is backward compatible with the schema you are updating. To update a schema with a new schema that is not backward compatible, you need to delete all the documents in the data store, delete the schema, and create a new schema.

Updating a schema triggers re-indexing of all documents. Reindexing a large data store can take hours or days.

Schema updates don't support the following:

  * **Changing a field type.** A schema update doesn't support changing the type of the field. For example, a field mapped to `integer` can't be changed to `string`.
  * **Removing a field.** After it's defined, a field can't be removed. You can continue adding new fields but you can't remove an existing field.



## Limitation examples (REST only)

This section shows examples of valid and invalid types of schema updates. These examples use the following example JSON schema:
    
    
    {
      "$schema": "https://json-schema.org/draft/2020-12/schema",
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "description": {
          "type": "string",
          "keyPropertyMapping": "description"
        },
        "categories": {
          "type": "array",
          "items": {
            "type": "string",
            "keyPropertyMapping": "category"
          }
        }
      }
    }
    

### Examples of supported updates

The following updates to the example schema are supported.

  * **Adding a field.** In this example, the field `properties.uri` has been added to the schema.
        
        {
          "$schema": "https://json-schema.org/draft/2020-12/schema",
          "type": "object",
          "properties": {
            "title": {
              "type": "string"
            },
            "description": {
              "type": "string",
              "keyPropertyMapping": "description"
            },
            "uri": { // Added field. This is supported.
              "type": "string",
              "keyPropertyMapping": "uri"
            },
            "categories": {
              "type": "array",
              "items": {
                "type": "string",
                "keyPropertyMapping": "category"
              }
            }
          }
        }
        

  * **Adding or removing key property annotations for`title`, `description` or `uri`.** In this example, `keyPropertyMapping` has been added to the `title` field.
        
        {
          "$schema": "https://json-schema.org/draft/2020-12/schema",
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "keyPropertyMapping": "title" // Added "keyPropertyMapping". This is supported.
            },
            "description": {
              "type": "string",
              "keyPropertyMapping": "description"
            },
            "categories": {
              "type": "array",
              "items": {
                "type": "string",
                "keyPropertyMapping": "category"
              }
            }
          }
        }
        




### Examples of invalid schema updates

The following updates to the example schema aren't supported.

  * **Changing a field type.** In this example, the `title` field's type has been changed from string to number. This is not supported.
        
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "properties": {
              "title": {
                "type": "number" // Changed from string. Not allowed.
              },
              "description": {
                "type": "string",
                "keyPropertyMapping": "description"
              },
              "categories": {
                "type": "array",
                "items": {
                  "type": "string",
                  "keyPropertyMapping": "category"
                }
              }
            }
          }
        

  * **Removing a field.** In this example, the `title` field has been removed. This is not supported.
        
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "properties": {
              // "title" is removed. Not allowed.
              "description": {
                "type": "string",
                "keyPropertyMapping": "description"
              },
              "uri": {
                "type": "string",
                "keyPropertyMapping": "uri"
              },
              "categories": {
                "type": "array",
                "items": {
                  "type": "string",
                  "keyPropertyMapping": "category"
                }
              }
            }
          }
        




## What's next

  * [View the schema definition for structured data](https://docs.cloud.google.com/gemini/enterprise/docs/get-schema-definition)
  * [Delete a schema for structured data](https://docs.cloud.google.com/gemini/enterprise/docs/delete-schemas)
  * [Preview search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
