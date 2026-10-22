---
url: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-quickstart/
title: Quickstart \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:28.643391+00:00
---

# Quickstart  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Samples ](https://docs.cloud.google.com/document-warehouse/docs/samples)



#  Quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Create a document schema and create a document

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Document AI Warehouse client libraries](https://docs.cloud.google.com/document-warehouse/docs/libraries)
  * [Quickstart](https://docs.cloud.google.com/document-warehouse/docs/quickstart)



## Code sample

### Java

For more information, see the [Document AI Warehouse Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/overview). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public class QuickStart {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String location = "your-region"; // Format is "us" or "eu".
        String userId = "your-user-id"; // Format is user:<user-id>
        quickStart(projectId, location, userId);
      }
    
      public static void quickStart(String projectId, String location, String userId)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        String projectNumber = getProjectNumber(projectId);
    
        String endpoint = "contentwarehouse.googleapis.com:443";
        if (!"us".equals(location)) {
          endpoint = String.format("%s-%s", location, endpoint);
        }
        DocumentSchemaServiceSettings documentSchemaServiceSettings = 
             DocumentSchemaServiceSettings.newBuilder().setEndpoint(endpoint).build(); 
    
        // Create a Schema Service client
        try (DocumentSchemaServiceClient documentSchemaServiceClient =
            DocumentSchemaServiceClient.create(documentSchemaServiceSettings)) {
          /*  The full resource name of the location, e.g.:
          projects/{project_number}/locations/{location} */
          String parent = LocationName.format(projectNumber, location);
    
          /* Create Document Schema with Text Type Property Definition
           * More detail on managing Document Schemas: 
           * https://cloud.google.com/document-warehouse/docs/manage-document-schemas */
          DocumentSchema documentSchema = DocumentSchema.newBuilder()
              .setDisplayName("My Test Schema")
              .setDescription("My Test Schema's Description")
              .addPropertyDefinitions(
                PropertyDefinition.newBuilder()
                  .setName("test_symbol")
                  .setDisplayName("Searchable text")
                  .setIsSearchable(true)
                  .setTextTypeOptions(TextTypeOptions.newBuilder().build())
                  .build()).build();
    
          // Define Document Schema request
          CreateDocumentSchemaRequest createDocumentSchemaRequest =
              CreateDocumentSchemaRequest.newBuilder()
                .setParent(parent)
                .setDocumentSchema(documentSchema).build();
    
          // Create Document Schema
          DocumentSchema documentSchemaResponse =
              documentSchemaServiceClient.createDocumentSchema(createDocumentSchemaRequest); 
    
    
          // Create Document Service Client Settings
          DocumentServiceSettings documentServiceSettings = 
              DocumentServiceSettings.newBuilder().setEndpoint(endpoint).build();
    
          // Create Document Service Client and Document with relevant properties 
          try (DocumentServiceClient documentServiceClient =
              DocumentServiceClient.create(documentServiceSettings)) {
            TextArray textArray = TextArray.newBuilder().addValues("Test").build();
            Document document = Document.newBuilder()
                  .setDisplayName("My Test Document")
                  .setDocumentSchemaName(documentSchemaResponse.getName())
                  .setPlainText("This is a sample of a document's text.")
                  .addProperties(
                    Property.newBuilder()
                      .setName(documentSchema.getPropertyDefinitions(0).getName())
                      .setTextValues(textArray)).build();
    
            // Define Request Metadata for enforcing access control
            RequestMetadata requestMetadata = RequestMetadata.newBuilder()
                .setUserInfo(
                UserInfo.newBuilder()
                  .setId(userId).build()).build();
    
            // Define Create Document Request 
            CreateDocumentRequest createDocumentRequest = CreateDocumentRequest.newBuilder()
                .setParent(parent)
                .setDocument(document)
                .setRequestMetadata(requestMetadata)
                .build();
    
            // Create Document
            CreateDocumentResponse createDocumentResponse =
                documentServiceClient.createDocument(createDocumentRequest);
    
            System.out.println(createDocumentResponse.getDocument().getName());
            System.out.println(documentSchemaResponse.getName());
          }
        }
      }
    
      private static String getProjectNumber(String projectId) throws IOException { 
        try (ProjectsClient projectsClient = ProjectsClient.create()) { 
          ProjectName projectName = ProjectName.of(projectId); 
          Project project = projectsClient.getProject(projectName);
          String projectNumber = project.getName(); // Format returned is projects/xxxxxx
          return projectNumber.substring(projectNumber.lastIndexOf("/") + 1);
        } 
      }
    }

### Node.js

For more information, see the [Document AI Warehouse Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     * const projectNumber = 'YOUR_PROJECT_NUMBER';
     * const location = 'YOUR_PROJECT_LOCATION'; // Format is 'us' or 'eu'
     * const userId = 'user:xxx@example.com'; // Format is "user:xxx@example.com"
     */
    
    // Import from google cloud
    const {DocumentSchemaServiceClient, DocumentServiceClient} =
      require('[@google-cloud/contentwarehouse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)').v1;
    
    const apiEndpoint =
      location === 'us'
        ? 'contentwarehouse.googleapis.com'
        : `${location}-contentwarehouse.googleapis.com`;
    
    // Create service client
    const schemaClient = new [DocumentSchemaServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)({
      apiEndpoint: apiEndpoint,
    });
    const serviceClient = new [DocumentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)({apiEndpoint: apiEndpoint});
    
    // Get Document Schema
    async function quickstart() {
      // The full resource name of the location, e.g.:
      // projects/{project_number}/locations/{location}
      const parent = `projects/${projectNumber}/locations/${location}`;
    
      // Initialize request argument(s)
      const schemaRequest = {
        parent: parent,
        documentSchema: {
          displayName: 'My Test Schema',
          propertyDefinitions: [
            {
              name: 'testPropertyDefinitionName', // Must be unique within a document schema (case insensitive)
              displayName: 'searchable text',
              isSearchable: true,
              textTypeOptions: {},
            },
          ],
        },
      };
    
      // Create Document Schema
      const documentSchema =
        await schemaClient.createDocumentSchema(schemaRequest);
    
      const documentRequest = {
        parent: parent,
        document: {
          displayName: 'My Test Document',
          documentSchemaName: documentSchema[0].name,
          plainText: "This is a sample of a document's text.",
          properties: [
            {
              name: 'testPropertyDefinitionName',
              textValues: {values: ['GOOG']},
            },
          ],
        },
        requestMetadata: {userInfo: {id: userId}},
      };
    
      // Make Request
      const response = serviceClient.createDocument(documentRequest);
    
      // Print out response
      response.then(
        result => console.log(`Document Created: ${JSON.stringify(result)}`),
        error => console.log(`error: ${error}`)
      );
    }
    

### Python

For more information, see the [Document AI Warehouse Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import contentwarehouse
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_number = 'YOUR_PROJECT_NUMBER'
    # location = 'YOUR_PROJECT_LOCATION' # Format is 'us' or 'eu'
    # user_id = "user:xxxx@example.com" # Format is "user:xxxx@example.com"
    
    
    def quickstart(project_number: str, location: str, user_id: str) -> None:
        # Create a Schema Service client
        document_schema_client = contentwarehouse.[DocumentSchemaServiceClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceClient.html)()
    
        # The full resource name of the location, e.g.:
        # projects/{project_number}/locations/{location}
        parent = document_schema_client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceClient.html#google_cloud_contentwarehouse_v1_services_document_schema_service_DocumentSchemaServiceClient_common_location_path)(
            project=project_number, location=location
        )
    
        # Define Schema Property of Text Type
        property_definition = contentwarehouse.[PropertyDefinition](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.PropertyDefinition.html)(
            name="stock_symbol",  # Must be unique within a document schema (case insensitive)
            display_name="Searchable text",
            is_searchable=True,
            text_type_options=contentwarehouse.[TextTypeOptions](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.TextTypeOptions.html)(),
        )
    
        # Define Document Schema Request
        create_document_schema_request = contentwarehouse.[CreateDocumentSchemaRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.CreateDocumentSchemaRequest.html)(
            parent=parent,
            document_schema=contentwarehouse.[DocumentSchema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentSchema.html)(
                display_name="My Test Schema",
                property_definitions=[property_definition],
            ),
        )
    
        # Create a Document schema
        document_schema = document_schema_client.[create_document_schema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceClient.html#google_cloud_contentwarehouse_v1_services_document_schema_service_DocumentSchemaServiceClient_create_document_schema)(
            request=create_document_schema_request
        )
    
        # Create a Document Service client
        document_client = contentwarehouse.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html)()
    
        # The full resource name of the location, e.g.:
        # projects/{project_number}/locations/{location}
        parent = document_client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html#google_cloud_contentwarehouse_v1_services_document_service_DocumentServiceClient_common_location_path)(
            project=project_number, location=location
        )
    
        # Define Document Property Value
        document_property = contentwarehouse.[Property](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.Property.html)(
            name=document_schema.property_definitions[0].name,
            text_values=contentwarehouse.[TextArray](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.TextArray.html)(values=["GOOG"]),
        )
    
        # Define Document
        document = contentwarehouse.[Document](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.Document.html)(
            display_name="My Test Document",
            document_schema_name=document_schema.name,
            plain_text="This is a sample of a document's text.",
            properties=[document_property],
        )
    
        # Define Request
        create_document_request = contentwarehouse.[CreateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.CreateDocumentRequest.html)(
            parent=parent,
            document=document,
            request_metadata=contentwarehouse.[RequestMetadata](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.RequestMetadata.html)(
                user_info=contentwarehouse.[UserInfo](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.UserInfo.html)(id=user_id)
            ),
        )
    
        # Create a Document for the given schema
        response = document_client.[create_document](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html#google_cloud_contentwarehouse_v1_services_document_service_DocumentServiceClient_create_document)(request=create_document_request)
    
        # Read the output
        print(f"Rule Engine Output: {response.rule_engine_output}")
        print(f"Document Created: {response.document}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=contentwarehouse). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
