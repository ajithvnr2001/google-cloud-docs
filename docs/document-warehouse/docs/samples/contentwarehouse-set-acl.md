---
url: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-set-acl/
title: Set access control list (ACL) \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:36.926409+00:00
---

# Set access control list (ACL)  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-set-acl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Samples ](https://docs.cloud.google.com/document-warehouse/docs/samples)



#  Set access control list (ACL) Stay organized with collections  Save and categorize content based on your preferences. 

Set the access control list (ACL) for a document or a project.

## Code sample

### Node.js

For more information, see the [Document AI Warehouse Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     * project_id = 'YOUR_PROJECT_ID'
     * location = 'YOUR_PROJECT_LOCATION' // Format is 'us' or 'eu'
     * policyRole = 'YOUR_REQUESTED_ROLE',
     * policyMember = 'YOUR_REQUESTED_MEMBER',
     * user_id = 'user:YOUR_SERVICE_ACCOUNT_ID' # Format is "user:xxxx@example.com"
     * document_id = 'YOUR_DOCUMENT_ID'
     */
    
    //Import service client from google cloud
    const {DocumentServiceClient} = require('[@google-cloud/contentwarehouse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)').v1;
    
    const apiEndpoint =
      location === 'us'
        ? 'contentwarehouse.googleapis.com'
        : `${location}-contentwarehouse.googleapis.com`;
    
    // Create client
    const serviceClient = new [DocumentServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)({apiEndpoint: apiEndpoint});
    
    // Set access control policies on project or document level.
    async function setACL() {
      //Initialize request argument(s)
      const request = {};
      request.policy = {
        bindings: [
          {
            role: policyRole,
            members: [policyMember],
          },
        ],
      };
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
      const response = serviceClient.setAcl(request);
    
      // Print Response
      response.then(
        result => console.log(`Success! Response: \n${JSON.stringify(result)}`),
        error => console.log(`Failed! Response: \n${error}`)
      );
    }
    

### Python

For more information, see the [Document AI Warehouse Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from typing import Any
    
    from google.cloud import contentwarehouse
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_number = 'YOUR_PROJECT_NUMBER'
    # location = 'YOUR_PROJECT_LOCATION' # Format is 'us' or 'eu'
    # document_id = 'YOUR_DOCUMENT_ID'
    # user_id = 'user:YOUR_SERVICE_ACCOUNT_ID' # Format is "user:xxxx@example.com"
    # policy = "Policy in JSON format"
    
    
    def set_acl(
        project_number: str,
        location: str,
        policy: dict[str, list[dict[str, Any]]],
        user_id: str,
        document_id: str = "",
    ) -> None:
        """Sets access control policies on project or document level.
    
        Args:
            project_number: Google Cloud project number.
            location: Google Cloud project location.
            policy: ACL policy to set, in JSON format.
            user_id: user:YOUR_SERVICE_ACCOUNT_ID.
            document_id: Record id in Document AI Warehouse.
        """
        # Create a client
        client = contentwarehouse.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html)()
    
        # Initialize request argument(s)
        # Set document acl if document id is specified
        # else set acl on project level
        if document_id:
            request = contentwarehouse.[SetAclRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.SetAclRequest.html)(
                # The full resource name of the document, e.g.:
                # projects/{project_number}/locations/{location}/documents/{document_id}
                resource=client.[document_path](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html#google_cloud_contentwarehouse_v1_services_document_service_DocumentServiceClient_document_path)(project_number, location, document_id),
                request_metadata=contentwarehouse.[RequestMetadata](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.RequestMetadata.html)(
                    user_info=contentwarehouse.[UserInfo](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.UserInfo.html)(id=user_id)
                ),
            )
        else:
            request = contentwarehouse.[SetAclRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.SetAclRequest.html)(
                # The full resource name of the project, e.g.:
                # projects/{project_number}
                resource=client.[common_project_path](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html#google_cloud_contentwarehouse_v1_services_document_service_DocumentServiceClient_common_project_path)(project_number),
                project_owner=True,
            )
    
        request.policy = policy
    
        # Make the request
        response = client.[set_acl](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.document_service.DocumentServiceClient.html#google_cloud_contentwarehouse_v1_services_document_service_DocumentServiceClient_set_acl)(request=request)
    
        # Print response
        print(response)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=contentwarehouse). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
