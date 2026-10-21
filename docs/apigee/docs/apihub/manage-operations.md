---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-operations/
title: Manage operations \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:07:31.774864+00:00
---

# Manage operations  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage operations Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes how to create and manage API operations in API hub. To learn more about operations, see [Introduction to API operations](https://docs.cloud.google.com/apigee/docs/apihub/operations-intro).

## Add an operation to an API version

You can add an API operation to an existing [API version](https://docs.cloud.google.com/apigee/docs/apihub/versions-intro) in the console or with the REST API.

### Console

To add a new API operation to an API version, do the following:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API you wish to add an operation to. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click the API to view its details. 
  5. Click the **Versions** tab and select the version you wish to add from the **Select a version** drop-down list.
  6. Go to the **Operations** section, click **Add operation**.
  7. Specify operation details in the **Add operation** form. 
     * **Operation ID** : Click **Specify Unique ID** to optionally provide a unique ID for the operation. If you omit the ID, API hub creates one for you. **Note:** The ID must be 4-500 characters long and can contain only uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), and hyphens (-). The ID forms the last part of the API resource name: `projects/PROJECT/locations/LOCATION/apis/API_ID/versions/VERSION_ID/operations/OPERATION_ID`. The full resource name is limited to 700 characters.
     * **Documentation** : Enter the URL to documentation for the API operation.
     * **Description** : Add a description of the operation.
     * **Operation type** : This field is automatically set as `HTTP`.
     * **Deprecated** : Select if the operation is deprecated.
     * **Path** : Enter the path of the operation.
     * **Path description** : Enter the description of the path of the operation.
     * **Method** : Enter the method of the operation.
     * **Additional attributes** : Add user-defined attributes based on your organizational or team needs. See [User attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#user-attributes).
  8. Click **Create**.



### REST

To add a new API operation using the [Create operations](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations/create) API, use the following command:
    
    
      curl --location --request POST 
      'https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions/VERSION_ID/operations?api_operation_id=OPERATION_ID' \
    --header 'Authorization: Bearer $(gcloud auth print-access-token)' \
    --header 'Content-Type: application/json' \
    --data '{
        "details":{
             "description":"DESCRIPTION",
             "deprecated":false,
            "documentation":{
                    "external_uri":"EXTERNAL_URI"
                },
            "http_operation":{
                "method":"METHOD",
                "path":{
                    "path":"PATH",
                    "description":"DESCRIPTION"
                }
            }
        }
    }'
    
    

Replace the following:

  * HUB_PROJECT: The project ID of the API hub project.
  * HUB_LOCATION: The location of the API hub project.
  * API_ID: The ID of the API.
  * VERSION_ID: The ID of the API version.
  * OPERATION_ID: The ID of the API operation.
  * DESCRIPTION: The description of the API operation.
  * EXTERNAL_URI: The external URI of the API operation.
  * METHOD: The method of the API operation.
  * PATH: The path of the API operation.



Example:
    
    
      curl --location --request POST 
      'https://apihub.googleapis.com/v1/projects/test-project/locations/us-central1/apis/test-api/versions/version-id/operations?api_operation_id=test-operation' \
      --header 'Authorization: Bearer $(gcloud auth print-access-token)' \
      --header 'Content-Type: application/json' \
      --data '{
          "details":{
               "description":"api to create root level entity api in apihub",
               "deprecated":false,
              "documentation":{
                      "external_uri":"https://google.com"
                  },
              "http_operation":{
                  "method":"POST",
                  "path":{
                      "path":"/apis",
                      "description":"It is ccfe managed resource"
                  }
              }
          }
      }'
      
    

## Edit an API operation

You can edit an API operation of an API version in the console or with the REST API. 

### Console

To edit an API operation, do the following:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API with the version that contains the operation you wish to edit. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click the API to view its details.
  5. Click the **Versions** tab and select the version that contains the operation you wish to edit.
  6. Go to the **Operations** section and locate the operation you wish to edit.
  7. Select **Edit** from the **Actions** menu in the row of the operation you wish to edit.
  8. In the **Edit operation** form, make the required changes to the operation details.
  9. Click **Save**.



### REST

To edit or update an API operation using the [Patch operations](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations/patch) API, use the following command:
    
    
      curl --location --request PATCH 'https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions/VERSION_ID/operations/OPERATION_ID?update_mask=UPDATE_MASK' \
      --header 'Authorization: Bearer $(gcloud auth print-access-token)' \
      --data '{
          "details":{
               "description":"DESCRIPTION",
               "deprecated":false,
              "documentation":{
                      "external_uri":"EXTERNAL_URI"
                  },
              "http_operation":{
                  "method":"METHOD",
                  "path":{
                      "path":"PATH",
                      "description":"DESCRIPTION"
                  }
              }
          }
      }'
      
    

Replace the following:

  * HUB_PROJECT: The project ID of the API hub project. 
  * HUB_LOCATION: The location of the API hub project. 
  * API_ID: The ID of the API. 
  * VERSION_ID: The ID of the API version. 
  * OPERATION_ID: The ID of the API operation. 
  * UPDATE_MASK: The update mask of the API operation. 
  * DESCRIPTION: The description of the API operation. 
  * EXTERNAL_URI: The external URI of the API operation. 
  * PATH: The path of the API operation. 



Example:
    
    
      curl --location --request PATCH 
      'https://apihub.googleapis.com/v1/projects/test-project/locations/us-central1/apis/test-api/versions/version-id/operations/test-operation?update_mask=details.http_operation.path' \
    --header 'Authorization: Bearer $(gcloud auth print-access-token)' \
    --data '{
        "details":{
             "description":"api to create root level entity api in apihub update",
             "deprecated":false,
            "documentation":{
                    "external_uri":"https://google.com"
                },
            "http_operation":{
                "method":"POST",
                "path":{
                    "path":"/apiss",
                    "description":"It is ccfe managed api"
                }
            }
        }
    }'
    

## Delete an API operation

You can delete an API operation in the console or with the REST API. 

### Console

To delete an API operation, do the following:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API with the version that contains the operation you wish to delete. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click the API to view its details.
  5. Click the **Versions** tab and select the version that contains the operation you wish to delete.
  6. Go to the **Operations** section and locate the operation you wish to delete.
  7. Select **Delete** from the **Actions** menu in the row of the operation you wish to delete.
  8. Click **Delete** in the confirmation dialog.



### REST

To delete an API operation using the [Delete operations](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations/delete) API, use the following command:
    
    
      curl --location --request DELETE 'https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions/VERSION_ID/operations/OPERATION_ID' \
      --header 'Authorization: Bearer $(gcloud auth print-access-token)'
    

Replace the following:

  * HUB_PROJECT: The project ID of the API hub project.
  * HUB_LOCATION: The location of the API hub project.
  * API_ID: The ID of the API.
  * VERSION_ID: The ID of the API version.
  * OPERATION_ID: The ID of the API operation.



Example:
    
    
      curl --location --request DELETE 'https://apihub.googleapis.com/v1/projects/test-project/locations/us-central1/apis/test-api/versions/version-id/operations/test-operation' \
      --header 'Authorization: Bearer $(gcloud auth print-access-token)'
    

## List API operations

You can list or view the API operations of an API version using the API hub console UI or using the [List operations](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations/list) API.

### Console

To view the API operations of an API version, do the following:

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Locate the API you wish to inspect. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Select an API.
  5. Go to the **Versions** tables in the **API details** page.
  6. Select an API version.
  7. The API operations for the selected API version are listed in the **Operations** table on the page.



### REST

To list the API operations of an API version, use the following command:
    
    
      curl -H "Authorization: Bearer $(gcloud auth print-access-token)"  -X GET  
      https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions/VERSION_ID/operations
    

Replace the following:

  * HUB_PROJECT: The project ID of the API hub project.
  * HUB_LOCATION: The location of the API hub project.
  * API_ID: The ID of the API.
  * VERSION_ID: The ID of the API version.



Example:
    
    
      curl -H "Authorization: Bearer $(gcloud auth print-access-token)"  -X GET  
      https://apihub.googleapis.com/v1/projects/test-project/locations/us-central1/apis/test-api/versions/version-id/operations
    

## Get API operation

You can get the details of an API operation using the [Get operations](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations/get) API. These details include the name, specification, description, create time, update time, and user-defined attributes. 

### REST

To get the details of an API operation, use the following command:
    
    
      curl -H "Authorization: Bearer $(gcloud auth print-access-token)"  -X GET  https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID/versions/VERSION_ID/operations/OPERATION_ID
    

Replace the following:

  * HUB_PROJECT: The project ID of the API hub project.
  * HUB_LOCATION: The location of the API hub project.
  * API_ID: The ID of the API.
  * VERSION_ID: The ID of the API version.
  * OPERATION_ID: The ID of the API operation.



Example:
    
    
      curl -H "Authorization: Bearer $(gcloud auth print-access-token)"  -X GET  https://apihub.googleapis.com/v1/projects/test-project/locations/us-central1/apis/test-api/versions/version-id/operations/test-operation
    

## Considerations

  * For API versions with a [valid OpenAPI specification](https://docs.cloud.google.com/apigee/docs/apihub/validate-spec) and parsed operations, the [Operations](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations) API can't be used to add, modify, or delete operations. 
  * When a valid OpenAPI specification is added to an API version containing existing operations, the operations defined in the specification will take precedence and replace the current ones. 
  * While specifications from multiple revisions can be stored for API proxies in Apigee and Apigee hybrid organizations, only the OpenAPI specification from the latest deployed revision is used to generate the API operations list in API hub. Changes made to an specification file in a newer, undeployed revision will not appear in API hub until that revision is deployed to an environment. 



## What's next

  * See the API reference documentation for the [Operations](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis.versions.operations) API.
  * Learn more about [API specifications](https://docs.cloud.google.com/apigee/docs/apihub/spec-intro).
  * Learn more about [API operations](https://docs.cloud.google.com/apigee/docs/apihub/operations-intro).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
