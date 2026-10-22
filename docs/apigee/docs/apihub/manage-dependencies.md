---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-dependencies/
title: Manage API supply chain dependencies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:14.544661+00:00
---

# Manage API supply chain dependencies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage API supply chain dependencies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page explains how to manage API supply chain dependencies in API hub. For an overview of API supply chain in API hub, see [API supply chain](https://docs.cloud.google.com/apigee/docs/apihub/api-supply-chain).

## List dependencies

You can view or list all the dependencies in your API ecosystem using Google Cloud console or the [List dependencies](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.dependencies/list) API.

### Console

To list all the dependencies in your API ecosystem from API hub, do the following:

  1. In the Google Cloud console, go to **API hub > ****API supply chain**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/dependencies)

The **API supply chain** page appears displaying all the dependencies in your API ecosystem in [list view](https://docs.cloud.google.com/apigee/docs/apihub/api-supply-chain#api-supply-chain-list-view).

  2. In the **Filter** field, if needed, specify supplier and/or consumer operations to return relevant dependencies. The filter feature lets you find all dependencies linked with specified operations.
  3. To view the dependencies in [graph view](https://docs.cloud.google.com/apigee/docs/apihub/api-supply-chain#api-supply-chain-graph-view), click lan **(Open graph view)** beside the consumer or supplier name in the list.



### REST

To list all the dependencies using the [List dependencies](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.dependencies/list) API, use the following command: 
    
    
      curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/dependencies"
          -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X GET -H "Content-Type: application/json"

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.



Sample output:
    
    
    {
      "dependencies": [
          {
              "name": "projects/myproject/locations/us-central1/dependencies/user-to-pet",
              "consumer": {
                  "displayName": "POST - /v2/user",
                  "operationResourceName": "projects/myproject/locations/us-central1/apis/payments-api/versions/version1/operations/createuser"
              },
              "supplier": {
                  "displayName": "POST - /v2/pet",
                  "operationResourceName": "projects/myproject/locations/us-central1/apis/payments-api/versions/version1/operations/addpet"
              }
          }
      ]
     }

## View dependency details

You can view the dependency details between API operations using Google Cloud console or the [Get dependency details](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.dependencies/get) API.

### Console

To view the details of a dependency from the Google Cloud console, do the following:

  1. In the Google Cloud console, go to **API hub > ****API supply chain**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/dependencies)

The **API supply chain** page appears displaying all the dependencies in your API ecosystem in [list view](https://docs.cloud.google.com/apigee/docs/apihub/api-supply-chain#api-supply-chain-list-view).

  2. In the **Filter** field, if needed, specify supplier and/or consumer operations to return relevant dependencies. The filter feature lets you find all dependencies linked with specified operations.
  3. Locate the desired dependency and click **See Details**. 

The **Dependency** pane appears displaying detailed information about the dependency such as the consumer and supplier details, dependency details, and the user defined attributes.




Alternatively, you can also use the API supply chain graph view to view the dependency details. For more information, see [API supply chain graph edge](https://docs.cloud.google.com/apigee/docs/apihub/api-supply-chain#edges).

### REST

To view details of a dependency using the [Get dependency details](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.dependencies/get) API, use the following command:
    
    
      curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/dependencies/DEPENDENCY_ID"
      -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X GET -H "Content-Type: application/json"

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * DEPENDENCY_ID: The unique ID of the dependency. 



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
      "createTime": "2024-04-17T19:33:31.215978712Z",
      "updateTime": "2024-04-17T19:33:31.737505297Z"
    }

Here's a sample response, where the error condition indicates the supplier operation was removed (a broken dependency):
    
    
    {
      "name": "projects/common-dev-15/locations/us-central1/dependencies/user-to-pet",
      "consumer": {
          "displayName": "POST - /v2/user",
          "operationResourceName": "projects/common-dev-15/locations/us-central1/apis/payments-api/versions/2ff89c88-e8b6-48c4-a1c2-bdbb2a929bde/operations/createuser"
      },
      "supplier": {
          "displayName": "POST - /v2/pet",
          "operationResourceName": "projects/common-dev-15/locations/us-central1/apis/payments-api/versions/2ff89c88-e8b6-48c4-a1c2-bdbb2a929bde/operations/addpet"
      },
      "state": "VALIDATED",
      "description": "Dependency from user to pet API",
      "discoveryMode": "MANUAL",
      "createTime": "2024-04-17T19:33:31.215978712Z",
      "updateTime": "2024-04-17T19:33:31.737505297Z",
      {
        "error": "SUPPLIER_NOT_FOUND",
        "errorTime": 2024-05-18T20:23:42.465324Z
      }
    }

## Edit a dependency

You can edit a dependency using Google Cloud console or the [Patch dependency](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.dependencies/patch) API.

**Note:** The only editable attribute is the dependency description. 

### Console

To edit an API dependency from API hub, do the following: 

  1. In the Google Cloud console, go to **API hub > ****API supply chain**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/dependencies)

The **API supply chain** page appears displaying all the dependencies in your API ecosystem in [list view](https://docs.cloud.google.com/apigee/docs/apihub/api-supply-chain#api-supply-chain-list-view).

  2. Locate the dependency that you want to edit and click **See Details**. 

The **Dependency** pane appears.

  3. Edit the description of the dependency under **Dependency details**.
  4. Click **Save**.



### REST

To edit a dependency using the [Patch dependencies](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.dependencies/patch) API, use the following command:
    
    
      curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/dependencies/DEPENDENCY_ID"
        -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X PATCH -H "Content-Type: application/json"
        '{
          'description': DESCRIPTION
        }'
      

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * DEPENDENCY_ID: The ID of the dependency to edit.
  * DESCRIPTION: The description of the dependency.



## Delete a dependency

You can delete a dependency using Google Cloud console or the [Delete dependency](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.dependencies/delete) API.

### Console

To delete a dependency from API hub, do the following: 

  1. In the Google Cloud console, go to **API hub > ****API supply chain**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/dependencies)

The **API supply chain** page appears displaying all the dependencies in your API ecosystem in [list view](https://docs.cloud.google.com/apigee/docs/apihub/api-supply-chain#api-supply-chain-list-view).

  2. In the **Filter** field, if needed, specify supplier and/or consumer operations to return relevant dependencies. The filter feature lets you find all dependencies linked with specified operations.
  3. Locate a dependency of interest and click delete **(Delete dependency)** to delete the dependency.



### REST

To delete a dependency using the [Delete dependency](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.dependencies/delete) API, use the following command:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/dependencies/DEPENDENCY_ID"
      -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X DELETE -H "Content-Type: application/json"

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * DEPENDENCY_ID: The ID of the dependency to delete. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
