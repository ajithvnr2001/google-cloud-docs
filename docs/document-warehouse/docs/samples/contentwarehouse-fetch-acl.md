---
url: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-fetch-acl/
title: Get access control list (ACL) \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:13.967698+00:00
---

# Get access control list (ACL)  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-fetch-acl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Samples ](https://docs.cloud.google.com/document-warehouse/docs/samples)



#  Get access control list (ACL) Stay organized with collections  Save and categorize content based on your preferences. 

Get the access control list (ACL) for a document or a project.

## Code sample

### Node.js

For more information, see the [Document AI Warehouse Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     * const projectId = 'YOUR_PROJECT_ID';
     * const location = 'YOUR_PROJECT_LOCATION'; // Format is 'us' or 'eu'
     * const documentId = 'YOUR_DOCUMENT_ID',
     * const userId = "user:xxxx@example.com" // Format is "user:xxxx@example.com"
     */
    
    // Import from google cloud
    const {DocumentServiceClient} = require('[@google-cloud/contentwarehouse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)').v1;
    
    const apiEndpoint =
      location === 'us'
        ? 'contentwarehouse.googleapis.com'
        : `${location}-contentwarehouse.googleapis.com`;
    
    // Create service client
    const serviceClient = new [DocumentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)({apiEndpoint: apiEndpoint});
    
    // Fetches access control policies on project or document level.
    async function fetchACL() {
      // Initialize request argument(s)
      const request = {};
      if (documentId !== 'YOUR_DOCUMENT_ID') {
        // Full document resource name, e.g.:
        // projects/{project_id}/locations/{location}/documents/{document_id}
        request.resource = `projects/${projectId}/locations/${location}/documents/${documentId}`;
        request.requestMetadata = {userInfo: {id: userId}};
      } else {
        // Full document resource name, e.g.: projects/{project_id}
        request.resource = `projects/${projectId}`;
        request.projectOwner = true;
      }
    
      // Make Request
      const response = serviceClient.fetchAcl(request);
    
      // Print out response
      response.then(
        result => console.log(`Success! Response: \n${JSON.stringify(result)}`),
        error => console.log(`Failed! Response: \n${error}`)
      );
    }
    

### Python

For more information, see the [Document AI Warehouse Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import contentwarehouse
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_number = 'YOUR_PROJECT_NUMBER'
    # location = 'YOUR_PROJECT_LOCATION' # Format is 'us' or 'eu'
    # document_id = 'YOUR_DOCUMENT_ID'
    # user_id = 'user:YOUR_SERVICE_ACCOUNT_ID' # Format is "user:xxxx@example.com"
    
    
    def fetch_acl(
        project_number: str, location: str, user_id: str, document_id: str = ""
    ) -> None:
        """Fetches access control policies on project or document level.
    
        Args:
            project_number: Google Cloud project number.
            location: Google Cloud project location.
            user_id: user:YOUR_SERVICE_ACCOUNT_ID.
            document_id: Record id in Document AI Warehouse.
        """
        # Create a client
        client = contentwarehouse.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html)()
    
        # Initialize request argument(s)
        # Fetch document acl if document id is specified
        # else fetch acl on project level
        if document_id:
            request = contentwarehouse.[FetchAclRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.FetchAclRequest.html)(
                # The full resource name of the document, e.g.:
                # projects/{project_number}/locations/{location}/documents/{document_id}
                resource=client.[document_path](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html#google_cloud_contentwarehouse_v1_services_document_service_DocumentServiceClient_document_path)(project_number, location, document_id),
                request_metadata=contentwarehouse.[RequestMetadata](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.RequestMetadata.html)(
                    user_info=contentwarehouse.[UserInfo](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.UserInfo.html)(id=user_id)
                ),
            )
        else:
            request = contentwarehouse.[FetchAclRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.FetchAclRequest.html)(
                # The full resource name of the project, e.g.:
                # projects/{project_number}
                resource=client.[common_project_path](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html#google_cloud_contentwarehouse_v1_services_document_service_DocumentServiceClient_common_project_path)(project_number),
                project_owner=True,
            )
    
        # Make Request
        response = client.[fetch_acl](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html#google_cloud_contentwarehouse_v1_services_document_service_DocumentServiceClient_fetch_acl)(request)
        print(response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=contentwarehouse). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
