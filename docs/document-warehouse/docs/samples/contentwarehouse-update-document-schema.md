---
url: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-update-document-schema/
title: Update document schema \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:30.416604+00:00
---

# Update document schema  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-update-document-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Samples ](https://docs.cloud.google.com/document-warehouse/docs/samples)



#  Update document schema Stay organized with collections  Save and categorize content based on your preferences. 

Update a document schema

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage document schemas](https://docs.cloud.google.com/document-warehouse/docs/manage-document-schemas)



## Code sample

### Java

For more information, see the [Document AI Warehouse Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/overview). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.contentwarehouse.v1.[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema.html);
    import com.google.cloud.contentwarehouse.v1.[DocumentSchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaName.html);
    import com.google.cloud.contentwarehouse.v1.[DocumentSchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceClient.html);
    import com.google.cloud.contentwarehouse.v1.[DocumentSchemaServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceSettings.html);
    import com.google.cloud.contentwarehouse.v1.[PropertyDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.PropertyDefinition.html);
    import com.google.cloud.contentwarehouse.v1.[TextTypeOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.TextTypeOptions.html);
    import com.google.cloud.contentwarehouse.v1.[UpdateDocumentSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentSchemaRequest.html);
    import com.google.cloud.resourcemanager.v3.[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project.html);
    import com.google.cloud.resourcemanager.v3.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html);
    import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    public class UpdateDocumentSchema {
      public static void updateDocumentSchema() throws IOException, 
            InterruptedException, ExecutionException, TimeoutException { 
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String location = "your-region"; // Format is "us" or "eu".
        String documentSchemaId = "your-document-schema-id";
        /* The below method call retrieves details about the schema you are about to update.
         * It is important to note that some properties cannot be edited or removed. 
         * For more information on managing document schemas, please see the below documentation.
         * https://cloud.google.com/document-warehouse/docs/manage-document-schemas */
        GetDocumentSchema.getDocumentSchema(projectId, location, documentSchemaId);
        updateDocumentSchema(projectId, location, documentSchemaId);
      }
    
      // Updates an existing Document Schema
      public static void updateDocumentSchema(String projectId, String location, 
            String documentSchemaId) throws IOException, InterruptedException,
              ExecutionException, TimeoutException { 
        String projectNumber = getProjectNumber(projectId);
    
        String endpoint = "contentwarehouse.googleapis.com:443";
        if (!"us".equals(location)) {
          endpoint = String.format("%s-%s", location, endpoint);
        }
    
        [DocumentSchemaServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceSettings.html) documentSchemaServiceSettings = 
                 [DocumentSchemaServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceSettings.html).newBuilder().setEndpoint(endpoint).build(); 
    
        /* Create the Schema Service Client 
         * Initialize client that will be used to send requests. 
         * This client only needs to be created once, and can be reused for multiple requests. */
        try ([DocumentSchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceClient.html) documentSchemaServiceClient = 
                [DocumentSchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaServiceClient.html).create(documentSchemaServiceSettings)) {
    
          /* The full resource name of the location, e.g.: 
           projects/{project_number}/location/{location}/documentSchemas/{document_schema_id} */
          [DocumentSchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaName.html) documentSchemaName = 
              [DocumentSchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaName.html).of(projectNumber, location, documentSchemaId);
    
          // Define the new Schema Property with updated values
          [PropertyDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.PropertyDefinition.html) propertyDefinition = [PropertyDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.PropertyDefinition.html).newBuilder()
              .setName("plaintiff")
              .setDisplayName("Plaintiff")
              .[setIsSearchable](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.PropertyDefinition.Builder.html#com_google_cloud_contentwarehouse_v1_PropertyDefinition_Builder_setIsSearchable_boolean_)(true)
              .[setIsRepeatable](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.PropertyDefinition.Builder.html#com_google_cloud_contentwarehouse_v1_PropertyDefinition_Builder_setIsRepeatable_boolean_)(true)
              .[setIsRequired](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.PropertyDefinition.Builder.html#com_google_cloud_contentwarehouse_v1_PropertyDefinition_Builder_setIsRequired_boolean_)(false)
              .[setTextTypeOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.PropertyDefinition.Builder.html#com_google_cloud_contentwarehouse_v1_PropertyDefinition_Builder_setTextTypeOptions_com_google_cloud_contentwarehouse_v1_TextTypeOptions_)([TextTypeOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.TextTypeOptions.html).newBuilder()
              .build())
              .build();
    
          [DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema.html) updatedDocumentSchema = [DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema.html).newBuilder()
                        .setDisplayName("Test Doc Schema") 
                        .addPropertyDefinitions(0, propertyDefinition).build();
    
          // Create the Request to Update the Document Schema
          [UpdateDocumentSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentSchemaRequest.html) updateDocumentSchemaRequest = 
                [UpdateDocumentSchemaRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentSchemaRequest.html).newBuilder()
                .setName(documentSchemaName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchemaName.html#com_google_cloud_contentwarehouse_v1_DocumentSchemaName_toString__)())
                .setDocumentSchema(updatedDocumentSchema)
                .build();
    
          // Update Document Schema
          updatedDocumentSchema = 
            documentSchemaServiceClient.updateDocumentSchema(updateDocumentSchemaRequest);
    
          // Read the output of Updated Document Schema Name
          System.out.println(updatedDocumentSchema.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentSchema.html#com_google_cloud_contentwarehouse_v1_DocumentSchema_getName__)());
        }
      }
    
      private static String getProjectNumber(String projectId) throws IOException { 
        /* Initialize client that will be used to send requests. 
        * This client only needs to be created once, and can be reused for multiple requests. */
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html).create()) { 
          [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html).of(projectId); 
          [Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project.html) project = projectsClient.getProject(projectName);
          String projectNumber = project.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project.html#com_google_cloud_resourcemanager_v3_Project_getName__)(); // Format returned is projects/xxxxxx
          return projectNumber.substring(projectNumber.lastIndexOf("/") + 1);
        } 
      }
    }

### Python

For more information, see the [Document AI Warehouse Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import contentwarehouse
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_number = "YOUR_PROJECT_NUMBER"
    # location = "us" # Format is 'us' or 'eu'
    # document_schema_id = "YOUR_SCHEMA_ID"
    
    
    def update_document_schema(
        project_number: str, location: str, document_schema_id: str
    ) -> None:
        # Create a Schema Service client
        document_schema_client = contentwarehouse.[DocumentSchemaServiceClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceClient.html)()
    
        # The full resource name of the location, e.g.:
        # projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}
        document_schema_path = document_schema_client.[document_schema_path](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceClient.html#google_cloud_contentwarehouse_v1_services_document_schema_service_DocumentSchemaServiceClient_document_schema_path)(
            project=project_number,
            location=location,
            document_schema=document_schema_id,
        )
    
        # Define Schema Property of Text Type with updated values
        updated_property_definition = contentwarehouse.[PropertyDefinition](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.PropertyDefinition.html)(
            name="stock_symbol",  # Must be unique within a document schema (case insensitive)
            display_name="Searchable text",
            is_searchable=True,
            is_repeatable=False,
            is_required=True,
            text_type_options=contentwarehouse.[TextTypeOptions](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.TextTypeOptions.html)(),
        )
    
        # Define Update Document Schema Request
        update_document_schema_request = contentwarehouse.[UpdateDocumentSchemaRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.UpdateDocumentSchemaRequest.html)(
            name=document_schema_path,
            document_schema=contentwarehouse.[DocumentSchema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentSchema.html)(
                display_name="My Test Schema",
                property_definitions=[updated_property_definition],
            ),
        )
    
        # Update Document schema
        updated_document_schema = document_schema_client.[update_document_schema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceClient.html#google_cloud_contentwarehouse_v1_services_document_schema_service_DocumentSchemaServiceClient_update_document_schema)(
            request=update_document_schema_request
        )
    
        # Read the output
        print(f"Updated Document Schema: {updated_document_schema}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=contentwarehouse). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
