---
url: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-search-documents/
title: Search documents \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:54.058058+00:00
---

# Search documents  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-search-documents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Samples ](https://docs.cloud.google.com/document-warehouse/docs/samples)



#  Search documents Stay organized with collections  Save and categorize content based on your preferences. 

Search documents in Document AI Warehouse

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Search documents](https://docs.cloud.google.com/document-warehouse/docs/basic-search)



## Code sample

### Java

For more information, see the [Document AI Warehouse Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/overview). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.contentwarehouse.v1.[DocumentQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentQuery.html);
    import com.google.cloud.contentwarehouse.v1.[DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient.html);
    import com.google.cloud.contentwarehouse.v1.[DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient.html).[SearchDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient.SearchDocumentsPagedResponse.html);
    import com.google.cloud.contentwarehouse.v1.[DocumentServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceSettings.html);
    import com.google.cloud.contentwarehouse.v1.[FileTypeFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FileTypeFilter.html);
    import com.google.cloud.contentwarehouse.v1.[FileTypeFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FileTypeFilter.html).[FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FileTypeFilter.FileType.html);
    import com.google.cloud.contentwarehouse.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.LocationName.html);
    import com.google.cloud.contentwarehouse.v1.[RequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RequestMetadata.html);
    import com.google.cloud.contentwarehouse.v1.[SearchDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsRequest.html);
    import com.google.cloud.contentwarehouse.v1.[SearchDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsResponse.html).[MatchingDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsResponse.MatchingDocument.html);
    import com.google.cloud.contentwarehouse.v1.[UserInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UserInfo.html);
    import com.google.cloud.resourcemanager.v3.[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project.html);
    import com.google.cloud.resourcemanager.v3.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html);
    import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    public class SearchDocuments {
      public static void main(String[] args) throws IOException, 
            InterruptedException, ExecutionException, TimeoutException { 
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String location = "your-region"; // Format is "us" or "eu".
        String documentQuery = "your-document-query";
        String userId = "your-user-id"; // Format is user:<user-id>
    
        searchDocuments(projectId, location, documentQuery, userId);
      }
    
      // Searches all documents for a given Document Query
      public static void searchDocuments(String projectId, String location,
            String documentQuery, String userId) throws IOException, InterruptedException,
              ExecutionException, TimeoutException { 
        String projectNumber = getProjectNumber(projectId);
    
        String endpoint = "contentwarehouse.googleapis.com:443";
        if (!"us".equals(location)) {
          endpoint = String.format("%s-%s", location, endpoint);
        }
    
        [DocumentServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceSettings.html) documentServiceSettings = 
                 [DocumentServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceSettings.html).newBuilder().setEndpoint(endpoint)
                 .build(); 
    
        /*
         * Create the Document Service Client 
         * Initialize client that will be used to send requests. 
         * This client only needs to be created once, and can be reused for multiple requests. 
         */
        try ([DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient.html) documentServiceClient = 
                [DocumentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient.html).create(documentServiceSettings)) {  
    
          /*
           * The full resource name of the location, e.g.:
           * projects/{project_number}/locations/{location} 
           */
          String parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.LocationName.html).format(projectNumber, location);
    
          // Define RequestMetadata object for context of the user making the API call
          [RequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RequestMetadata.html) requestMetadata = [RequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RequestMetadata.html).newBuilder()
              .setUserInfo(
              [UserInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UserInfo.html).newBuilder()
                .[setId](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UserInfo.Builder.html#com_google_cloud_contentwarehouse_v1_UserInfo_Builder_setId_java_lang_String_)(userId)
                .build())
                .build();
    
          // Set file type for filter to 'DOCUMENT'
          [FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FileTypeFilter.FileType.html) documentFileType = [FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FileTypeFilter.FileType.html).DOCUMENT;
    
          // Create a file type filter for documents 
          [FileTypeFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FileTypeFilter.html) fileTypeFilter = [FileTypeFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FileTypeFilter.html).newBuilder()
              .[setFileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FileTypeFilter.Builder.html#com_google_cloud_contentwarehouse_v1_FileTypeFilter_Builder_setFileType_com_google_cloud_contentwarehouse_v1_FileTypeFilter_FileType_)(documentFileType)
              .build();
    
          // Create document query to search all documents for text given at input
          [DocumentQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentQuery.html) query = [DocumentQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentQuery.html).newBuilder()
              .setQuery(documentQuery)
              .[setFileTypeFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentQuery.Builder.html#com_google_cloud_contentwarehouse_v1_DocumentQuery_Builder_setFileTypeFilter_com_google_cloud_contentwarehouse_v1_FileTypeFilter_)(fileTypeFilter)
              .build();
    
          /*
           * Create the request to search all documents for specified query. 
           * Please note the offset in this request is to only return the specified number of results 
           * to avoid hitting the API quota. 
           */
          [SearchDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsRequest.html) searchDocumentsRequest = [SearchDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsRequest.html).newBuilder()
              .setParent(parent)
              .setRequestMetadata(requestMetadata)
              .[setOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsRequest.Builder.html#com_google_cloud_contentwarehouse_v1_SearchDocumentsRequest_Builder_setOffset_int_)(5)
              .[setDocumentQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsRequest.Builder.html#com_google_cloud_contentwarehouse_v1_SearchDocumentsRequest_Builder_setDocumentQuery_com_google_cloud_contentwarehouse_v1_DocumentQuery_)(query)
              .build();
    
          // Make the call to search documents with document service client and store the response
          [SearchDocumentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceClient.SearchDocumentsPagedResponse.html) searchDocumentsPagedResponse = 
              documentServiceClient.searchDocuments(searchDocumentsRequest);
    
          // Iterate through response and print search results for documents matching the search query
          for ([MatchingDocument](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsResponse.MatchingDocument.html) matchingDocument :
              searchDocumentsPagedResponse.iterateAll()) {
            System.out.println(
                "Display Name: " + matchingDocument.getDocument().getDisplayName()
                + "Document Name: " + matchingDocument.getDocument().getName()
                + "Document Creation Time: " + matchingDocument.getDocument().getCreateTime().toString()
                + "Search Text Snippet: " + matchingDocument.getSearchTextSnippet());
          }
        }
      }
    
      private static String getProjectNumber(String projectId) throws IOException { 
        /*
         * Initialize client that will be used to send requests. 
         * This client only needs to be created once, and can be reused for multiple requests.
         */
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html).create()) { 
          [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html).of(projectId); 
          [Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project.html) project = projectsClient.getProject(projectName);
          String projectNumber = project.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project.html#com_google_cloud_resourcemanager_v3_Project_getName__)(); // Format returned is projects/xxxxxx
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
     * const documentQueryText = 'YOUR_DOCUMENT_QUERY'
     */
    
    // Import from google cloud
    const {DocumentServiceClient} = require('[@google-cloud/contentwarehouse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)').v1;
    
    const apiEndpoint =
      location === 'us'
        ? 'contentwarehouse.googleapis.com'
        : `${location}-contentwarehouse.googleapis.com`;
    
    // Create service client
    const serviceClient = new [DocumentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)({apiEndpoint: apiEndpoint});
    
    // Get Document Schema
    async function searchDocuments() {
      // Initialize request argument(s)
      const searchRequest = {
        // The full resource name of the location, e.g.:
        // projects/{project_number}/locations/{location}
        parent: `projects/${projectNumber}/locations/${location}`,
    
        // Document Text Query
        documentQuery: {
          query: documentQueryText,
          // File Type Filter
          fileTypeFilter: {
            fileType: '[DOCUMENT](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.filetypefilter.filetype.html)',
          },
        },
    
        // Histogram Query
        histogramQueries: [
          {
            histogramQuery: 'count("DocumentSchemaId")',
          },
        ],
        requestMetadata: {userInfo: {id: userId}},
      };
    
      // Make Request
      const response = serviceClient.searchDocuments(searchRequest);
    
      // Print out response
      response.then(
        result => console.log(`Document Found: ${JSON.stringify(result)}`),
        error => console.log(`${error}`)
      );
    }
    

### Python

For more information, see the [Document AI Warehouse Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import contentwarehouse
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_number = 'YOUR_PROJECT_NUMBER'
    # location = 'YOUR_PROJECT_LOCATION' # Format is 'us' or 'eu'
    # document_query_text = 'YOUR_DOCUMENT_QUERY'
    # user_id = 'user:YOUR_SERVICE_ACCOUNT_ID' # Format is "user:xxxx@example.com"
    
    
    def search_documents_sample(
        project_number: str, location: str, document_query_text: str, user_id: str
    ) -> None:
        # Create a client
        client = contentwarehouse.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html)()
    
        # The full resource name of the location, e.g.:
        # projects/{project_number}/locations/{location}
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html#google_cloud_contentwarehouse_v1_services_document_service_DocumentServiceClient_common_location_path)(project=project_number, location=location)
    
        # File Type Filter
        # Options: DOCUMENT, FOLDER
        file_type_filter = contentwarehouse.[FileTypeFilter](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.FileTypeFilter.html)(
            file_type=contentwarehouse.[FileTypeFilter](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.FileTypeFilter.html).[FileType](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.FileTypeFilter.FileType.html).DOCUMENT
        )
    
        # Document Text Query
        document_query = contentwarehouse.[DocumentQuery](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DocumentQuery.html)(
            query=document_query_text,
            file_type_filter=file_type_filter,
        )
    
        # Histogram Query
        histogram_query = contentwarehouse.[HistogramQuery](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.HistogramQuery.html)(
            histogram_query='count("DocumentSchemaId")'
        )
    
        request_metadata = contentwarehouse.[RequestMetadata](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.RequestMetadata.html)(
            user_info=contentwarehouse.[UserInfo](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.UserInfo.html)(id=user_id)
        )
    
        # Define request
        request = contentwarehouse.[SearchDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.SearchDocumentsRequest.html)(
            parent=parent,
            request_metadata=request_metadata,
            document_query=document_query,
            histogram_queries=[histogram_query],
        )
    
        # Make the request
        response = client.[search_documents](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html#google_cloud_contentwarehouse_v1_services_document_service_DocumentServiceClient_search_documents)(request=request)
    
        # Print search results
        for matching_document in response.matching_documents:
            document = matching_document.document
            # Display name - schema display name.
            # Name.
            # Create date.
            # Snippet - keywords are highlighted with <b> & </b>.
            print(
                f"{document.display_name} - {document.document_schema_name}\n"
                f"{document.name}\n"
                f"{document.create_time}\n"
                f"{matching_document.search_text_snippet}\n"
            )
    
        # Print histogram
        for histogram_query_result in response.histogram_query_results:
            print(
                f"Histogram Query: {histogram_query_result.histogram_query}\n"
                f"| {'Schema':<70} | {'Count':<15} |"
            )
            for key, value in histogram_query_result.histogram.items():
                print(f"| {key:<70} | {value:<15} |")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=contentwarehouse). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
