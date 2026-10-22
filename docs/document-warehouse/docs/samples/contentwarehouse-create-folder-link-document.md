---
url: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-create-folder-link-document/
title: Create a folder and link a document \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:48.335910+00:00
---

# Create a folder and link a document  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-create-folder-link-document/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Samples ](https://docs.cloud.google.com/document-warehouse/docs/samples)



#  Create a folder and link a document Stay organized with collections  Save and categorize content based on your preferences. 

Create a folder and link a document

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Organize documents in folders](https://docs.cloud.google.com/document-warehouse/docs/organize-documents-in-folders)



## Code sample

### Python

For more information, see the [Document AI Warehouse Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import contentwarehouse
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_number = "YOUR_PROJECT_NUMBER"
    # location = "us" # Format is 'us' or 'eu'
    # user_id = "user:xxxx@example.com" # Format is "user:xxxx@example.com"
    
    
    def create_folder(
        project_number: str, location: str, user_id: str
    ) -> contentwarehouse.Document:
        # Create a Schema Service client
        document_schema_client = contentwarehouse.[DocumentSchemaServiceClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceClient.html)()
    
        # The full resource name of the location, e.g.:
        # projects/{project_number}/locations/{location}
        parent = document_schema_client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceClient.html#google_cloud_contentwarehouse_v1_services_document_schema_service_DocumentSchemaServiceClient_common_location_path)(
            project=project_number, location=location
        )
    
        # Define Folder Schema Request
        create_folder_schema_request = contentwarehouse.[CreateDocumentSchemaRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.CreateDocumentSchemaRequest.html)(
            parent=parent,
            document_schema=contentwarehouse.[DocumentSchema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentSchema.html)(
                display_name="Test Folder Schema ",
                document_is_folder=True,
            ),
        )
    
        # Create a Folder Schema
        folder_schema = document_schema_client.[create_document_schema](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_schema_service.DocumentSchemaServiceClient.html#google_cloud_contentwarehouse_v1_services_document_schema_service_DocumentSchemaServiceClient_create_document_schema)(
            request=create_folder_schema_request
        )
    
        # Create a Document(Folder) Service client
        folder_client = contentwarehouse.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html)()
    
        # Define Folder
        folder = contentwarehouse.[Document](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.Document.html)(
            display_name="My Test Folder",
            document_schema_name=folder_schema.name,
        )
    
        # Define Request to create Folder
        create_folder_request = contentwarehouse.[CreateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.CreateDocumentRequest.html)(
            parent=parent,
            document=folder,
            request_metadata=contentwarehouse.[RequestMetadata](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.RequestMetadata.html)(
                user_info=contentwarehouse.[UserInfo](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.UserInfo.html)(id=user_id)
            ),
        )
    
        # Create a Folder for the given schema
        folder_response = folder_client.[create_document](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html#google_cloud_contentwarehouse_v1_services_document_service_DocumentServiceClient_create_document)(request=create_folder_request)
    
        # Read the output
        print(f"Rule Engine Output: {folder_response.rule_engine_output}")
        print(f"Folder Created: {folder_response.document}")
    
        return folder_response
    
    
    def create_document(
        project_number: str, location: str, user_id: str
    ) -> contentwarehouse.Document:
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
        document_response = document_client.[create_document](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html#google_cloud_contentwarehouse_v1_services_document_service_DocumentServiceClient_create_document)(request=create_document_request)
    
        # Read the output
        print(f"Rule Engine Output: {document_response.rule_engine_output}")
        print(f"Document Created: {document_response.document}")
    
        return document_response
    
    
    def create_folder_link_document(
        project_number: str, location: str, user_id: str
    ) -> None:
        # Function call to create a folder
        folder = create_folder(project_number, location, user_id)
    
        # Function call to create a Document
        document = create_document(project_number, location, user_id)
    
        # Create a Link Service client
        link_client = contentwarehouse.[DocumentLinkServiceClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_link_service.DocumentLinkServiceClient.html)()
    
        # Initialize request argument(s)
        link = contentwarehouse.[DocumentLink](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentLink.html)(
            source_document_reference=contentwarehouse.[DocumentReference](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentReference.html)(
                document_name=folder.document.name,
            ),
            target_document_reference=contentwarehouse.[DocumentReference](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentReference.html)(
                document_name=document.document.name,
            ),
        )
    
        # Initialize document link request
        create_document_link_request = contentwarehouse.[CreateDocumentLinkRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.CreateDocumentLinkRequest.html)(
            parent=folder.document.name,
            document_link=link,
            request_metadata=contentwarehouse.[RequestMetadata](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.RequestMetadata.html)(
                user_info=contentwarehouse.[UserInfo](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.UserInfo.html)(id=user_id)
            ),
        )
    
        # Make the Document Link request
        create_link_response = link_client.[create_document_link](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_link_service.DocumentLinkServiceClient.html#google_cloud_contentwarehouse_v1_services_document_link_service_DocumentLinkServiceClient_create_document_link)(
            request=create_document_link_request
        )
    
        print(f"Link Created: {create_link_response}")
    
        # Initialize list linked targets request
        linked_targets_request = contentwarehouse.[ListLinkedTargetsRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.ListLinkedTargetsRequest.html)(
            parent=folder.document.name,
            request_metadata=contentwarehouse.[RequestMetadata](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.RequestMetadata.html)(
                user_info=contentwarehouse.[UserInfo](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.UserInfo.html)(id=user_id)
            ),
        )
    
        # Make the request
        linked_targets_response = link_client.[list_linked_targets](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_link_service.DocumentLinkServiceClient.html#google_cloud_contentwarehouse_v1_services_document_link_service_DocumentLinkServiceClient_list_linked_targets)(
            request=linked_targets_request
        )
    
        print(f"Validate Link Created: {linked_targets_response}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=contentwarehouse). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
