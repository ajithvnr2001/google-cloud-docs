---
url: https://docs.cloud.google.com/apigee/docs/apihub/create-dependency/
title: Create API supply chain dependencies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:43.980508+00:00
---

# Create API supply chain dependencies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/create-dependency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Create API supply chain dependencies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

You can create a dependency between APIs, API versions, and API operations in API hub. The high-level process to create a dependency is as follows:

  1. Find two APIs that may have operations that may be dependent. The operations may be in [registered APIs](https://docs.cloud.google.com/apigee/docs/apihub/manage-apis#register-an-api) or [external APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.externalApis). 
  2. Determine which API is the supplier and which is the consumer. As discussed previously, the consumer invokes the supplier.
  3. Use the Google Cloud console or the [Create dependency API](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.dependencies/create) to create the dependency between the supplier and consumer. 

**Note:** API hub doesn't support creating dependencies between Model Context Protocol (MCP) tools.

## Create a dependency

You can create a dependency in the console or with the REST API.

### Console

To create a dependency using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **API supply chain** page in **API hub**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/dependencies)
  2. Click **Create dependency** and provide the following inputs in the **Create a new dependency** page.
  3. Under **General details** , do the following: 
     1. **Specify unique ID** : (Optional) The identifier of the dependency. If not provided, a system-generated ID will be used. **Note:** Dependency ID must be 4-500 characters long and can contain only uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), and hyphens (-). The ID forms the last part of the API resource name: `projects/PROJECT/locations/LOCATION/dependencies/DEPENDENCY_ID`.
     2. **Description** : (Optional) A brief description of the dependency.
     3. Click **Continue**.
  4. Under **Select supplier resource** , do the following: 
     1. **Resource type:** Select **Operation** as the supplier resource type.
     2. **Supplier API:** Select the API that supplies the operation.
     3. **Version:** Select the API version of the supplier API that provides the operation.
     4. **Operation:** Select the operation that is supplied to the consumer. For example: `GET-/items`.
     5. Click **Continue**.
**Note:** To use external APIs to create dependencies, you must use the [Dependencies API](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.dependencies/create). For more information, see the **REST API** tab. 
  5. Under **Select consumer resource** , do the following: 
     1. **Resource type:** Select **Operation** as the consumer resource type.
     2. **Consumer API:** Select the API that consumes the operation.
     3. **Version:** Select the API version of the consumer API that consumes the operation.
     4. **Operation:** Select the operation that is consumed by the supplier. For example: `GET-/categories`.
     5. Click **Continue**.
  6. Optionally, provide values for any user-defined attributes that were defined in Settings.
  7. Click **Create**. The new dependency appears in the **API supply chain** page.



### REST API

To create a new dependency using the [Create a dependency](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.dependencies/create) API, use the following command:
    
    
      curl -X POST 'https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/dependencies?dependency_id=DEPENDENCY_ID' \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H 'Content-Type: application/json' \
      --d '{
          "description": "DESCRIPTION",
          "supplier": {
              // Specify one of the following:
              "operation_resource_name": RESOURCE_NAME
              // OR
              "external_api_resource_name: RESOURCE_NAME"
          },
          "consumer": {
            // Specify one of the following:
            "operation_resource_name": RESOURCE_NAME
            // OR
            "external_api_resource_name: RESOURCE_NAME"
          }
      }'
    

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * DEPENDENCY_ID: (Optional) The identifier of the dependency. If not provided, a system-generated ID will be used. **Note:** The ID must be 4-500 characters, and valid characters are `/[A-Z][a-z][0-9]-/.` The ID is the last component of the fully qualified, unique API resource name, which is in the format: `projects/PROJECT/locations/LOCATION/dependencies/DEPENDENCY_ID`
  * DESCRIPTION: (Optional) A brief description of the dependency. 
  * RESOURCE_NAME: (Required) Either the resource name of an operation in API hub or an external API, depending on which attribute you specify.

Operation resource names follow this format: `projects/PROJECT/locations/LOCATION/apis/API/versions/VERSION/operations/OPERATION`

Operation resource example: `"projects/myproject/locations/us-central1/apis/payments-api/versions/locationv1/operations/getlocation"`.

External API resource names follow this format: `projects/PROJECT/locations/LOCATION/externalApis/EXTERNAL_API`

External API resource example: `"projects/myproject/locations/us-central1/externalApis/petstore"`.




Example:
    
    
      curl -X POST 'https://apihub.googleapis.com/v1/projects/myproject/locations/us-central1/dependencies?dependency_id=user-to-pet' \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H 'Content-Type: application/json' \
      --d '{
          "description": "Dependency from user to pet API",
          "consumer": {
              "operation_resource_name": "projects/myproject/locations/us-central1/apis/payments-api/versions/paymentv1/operations/createuser"
          },
          "supplier": {
              "operation_resource_name": "projects/myproject/locations/us-central1/apis/pet-api/versions/petstorev1/operations/addpet"
          }
      }'
    

Sample response:
    
    
    {
      "name": "projects/myproject/locations/us-central1/dependencies/user-to-pet",
      "consumer": {
          "displayName": "POST - /v2/user",
          "operationResourceName": "projects/myproject/locations/us-central1/apis/payments-api/versions/version1/operations/createuser"
      },
      "supplier": {
          "displayName": "POST - /v2/pet",
          "operationResourceName": "projects/myproject/locations/us-central1/apis/payments-api/versions/version1/operations/addpet"
      },
      "state": "VALIDATED",
      "description": "Dependency from user to pet API",
      "discoveryMode": "MANUAL",
      "createTime": "2024-04-17T19:33:31.664226Z",
      "updateTime": "2024-04-17T19:33:31.664226Z"
     }

## What's next?

  * Learn about how to [manage dependencies](https://docs.cloud.google.com/apigee/docs/apihub/manage-dependencies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
