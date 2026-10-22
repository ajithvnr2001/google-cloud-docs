---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-apis/
title: Manage API resources \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:22.754146+00:00
---

# Manage API resources  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage API resources Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

## List API resources

This section explains how to list the API resources in API hub. By adding a filter, you can limit the APIs returned in the response. 

### Console

To list API resources:

  1. In the Google Cloud console, go to the **APIs** page in **API hub**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)

A list of all APIs added to API hub are listed on the APIs home page.

  2. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.



### REST

To list all API resources in your API hub project, use the [List APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis/list) API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis"
      -X GET -H "Authorization: Bearer: $(gcloud auth print-access-token)" -H "Content-Type: application/json"
    

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.



Sample output:
    
    
    {
      "apis": [
        {
          "name": "projects/myproject/locations/us-central1/apis/a035eb3b-658e-467a-89d3-9cca2bbacd32-2",
          "displayName": "TestApi2",
          "documentation": {}
        },
        {
          "name": "projects/myproject/locations/us-central1/apis/a035eb3b-658e-467a-89d3-9cca2bbacd32-1",
          "displayName": "TestApi1",
          "documentation": {}
        },
        {
          "name": "projects/myproject/locations/us-central1/apis/foo9013cfev",
          "displayName": "sample",
          "documentation": {}
        },
        {
          "name": "projects/myproject/locations/us-central1/apis/foo90121",
          "displayName": "sample",
          "documentation": {}
        },
        ...
        ],
        "nextPageToken": "f4f4d78b-a974-46db-a214-dc139f8e9c8a"
      }

### REST example with filter

You can filter list results using the API. In this example, we filter APIs based on an system defined attribute: 
    
    
    curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      'https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis' \
      -d filter="owner.email=\"testowner3@gmail.com\"" -d page_size=10
    

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.



Sample output, filtered by owner:
    
    
    {
      "apis": [
        {
          "name": "projects/myproject/locations/us-central1/apis/theme-park-management-api",
          "displayName": "Theme Park Management API",
          "documentation": {}
        },
        {
          "name": "projects/myproject/locations/us-central1/apis/restaurant-api",
          "displayName": "Restaurant API",
          "documentation": {}
        },
        {
          "name": "projects/myproject/locations/us-central1/apis/casino-management-api",
          "displayName": "Casino Management API",
          "documentation": {}
        },
        {
          "name": "projects/myproject/locations/us-central1/apis/hotel-boooking-api",
          "displayName": "Hotel Booking API",
          "documentation": {}
        },
        {
          "name": "projects/myproject/locations/us-central1/apis/test-march-26-api3",
          "displayName": "Test Pets API",
          "documentation": {}
        },
        {
          "name": "projects/myproject/locations/us-central1/apis/test-march-26-api2",
          "displayName": "Test Pets API",
          "documentation": {}
        },
        {
          "name": "projects/myproject/locations/us-central1/apis/test-march-26-api1",
          "displayName": "Test Pets API",
          "documentation": {}
        }
      ]
    }

## Get API resource details

This section explains how to get the details about an API resource. 

### Console

To view details of an API resource:

  1. In the Google Cloud console, go to the **APIs** page in **API hub**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  3. Click an API to view its overview page.



### REST

To view details of an API resource, use the [Get API resource details](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis/get) API:
    
    
    curl "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID"
      -H "Authorization: Bearer: $(gcloud auth print-access-token)" -X GET -H "Content-Type: application/json"
    

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API resource. 



Sample output:
    
    
    {
      "name": "projects/myproject/locations/us-central1/apis/myapi",
      "displayName": "My Test API",
      "description": "This is a test API.",
      "documentation": {},
      "owner": {
        "displayName": "Test API,
        "email": "testowner@gmail.com"
      },
      "versions": [
        "projects/myproject/locations/us-central1/apis/myapi/versions/myapi-version1"
      ],
      "createTime": "2024-03-26T10:13:15.668867002Z",
      "updateTime": "2024-03-26T10:13:16.700716401Z"
    }

## View API resource insights

To get a deeper understanding of your API usage, view API resource insights in API hub: 

  1. In the Google Cloud console, go to the **APIs** page in **API hub**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click an API to view its details page.
  3. Click the **Insights** tab to view the API metrics.



For more information about the available metrics, see [View API resource insights](https://docs.cloud.google.com/apigee/docs/apihub/view-api-resource-insights).

## Delete an API resource

This section explains how to delete an API resource. 

### Console

When you delete an API in the UI, then all of the underlying versions of the API and associated API specifications (if any) are deleted.

To delete an API resource:

  1. In the Google Cloud console, go to the **APIs** page in **API hub**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API to delete.
  3. From the **Actions** menu (the right side of the row containing the API), click **Delete**.



### REST

To delete an API from API hub, use the [Delete API](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis/delete) API.

By default, an API can only be deleted if all underlying versions are deleted. If you want to delete all versions under an API in one step, set the `force` query parameter to `true` in the Delete REST API.
    
    
    curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      'https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID'

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API resource to delete.



To delete the API and all underlying versions, set the `force` query parameter to `true`. For example:
    
    
    curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      'https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID?force=true'

## Edit an API resource

This section explains how to edit an API resource. Not all API resource attributes are editable. For the list of editable attributes, see the [Patch API](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis/patch) reference document. 

### Console

To edit an API:

  1. In the Google Cloud console, go to the **APIs** page in **API hub**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API to edit.
  3. Click an API to view its details page. 
  4. Click **Edit API**. 
  5. On the **Edit API** page, make your changes. Click **Continue** to move to the next set of editable attributes. 
     * **General details** : You can edit the display name of the API. 
     * **Owner information** : The name and email address of the API owner.
     * **Additional details** : These are the system-defined attributes. You can specify custom default values for these attributes in [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes). 
     * **User defined attributes** : These are the custom, user-defined attributes. You can specify custom attributes in [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes).
  6. Click **Save**. 



### REST

To edit an API resource, use the [Patch API resource API](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis/patch).
    
    
    curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d '{
              "display_name": "Updated Test Docs API",        # Example request body with changes
              "description": "This is the updated test API.",
              "owner": {
                "display_name": "Updated Docs Owner",
                "email": "updateddocsowner@gmail.com"
                }
              }
              ' https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_ID

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: The unique ID of the API to update. 
  * **Request Body** : Use the request body to specify the attributes you wish to change. See the [API request body description](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis#Api).



## What's next

  * Learn how to [View API resource insights](https://docs.cloud.google.com/apigee/docs/apihub/view-api-resource-insights).
  * Learn how to [Manage API versions](https://docs.cloud.google.com/apigee/docs/apihub/manage-versions).
  * Learn about [API insights in API hub](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
