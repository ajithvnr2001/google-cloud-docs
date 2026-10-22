---
url: https://docs.cloud.google.com/apigee/docs/apihub/register-api/
title: Register an API \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:11.284945+00:00
---

# Register an API  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/register-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Register an API Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

When you register an API with API hub, you create and store an entity that represents the API. We call this entity an **API resource**. API resources stored in API hub are searchable and provide detailed operational and descriptive information about the API. Either at the time you register an API or afterwards, you can add and edit API resource attributes to build a rich description of the API. 

### Console

To register an API:

  1. In the Google Cloud console, go to the **APIs** page in **API hub**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **Register API**.
  3. Under **General details** , optionally specify a unique ID for the API. If you do not supply an ID, the system will generate one for you. If you wish to enter an ID, click **Specify Unique ID**.

**Note:** The ID must be 4-500 characters, and valid characters are `/[A-Z][a-z][0-9]-/.` The ID is the last component of the fully qualified, unique API resource name, which is in the format: `projects/PROJECT/locations/LOCATION/apis/API_ID`
  4. (Required) Provide a display name for the API resource. 
  5. Optionally add additional attributes that describe the API. You can return to the API at any time to add or change API attributes. See [Edit an API resource](https://docs.cloud.google.com/apigee/docs/apihub/manage-apis#updateapi.). 
     * **Owner information** : (Optional) The name and email address of the API owner.
     * **Additional details** : (Optional) Specify attributes to help define your API and make it more easily searchable. You can define default values for some of these attributes in Settings. For details, see [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes). 
     * **User defined attributes** : (Optional) These are attributes that you define in Settings. For details, see [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes).
  6. Click **Register**.



### REST

To register an API, use the [Create API](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis/create) REST API.
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d '{
        "display_name": "DISPLAY_NAME",            # Required attribute
        "description": "DESCRIPTION"               # description is an optional attribute
        }
        'https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis?api_id=API_ID

Replace the following:

  * HUB_PROJECT: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * API_ID: (Optional) Enter a unique ID for the API. If you do not supply this query parameter, the system will generate a unique ID for you. **Note:** The ID must be 4-500 characters, and valid characters are `/[A-Z][a-z][0-9]-/.` The ID is the last component of the fully qualified, unique API resource name, which is in the format: `projects/PROJECT/locations/LOCATION/apis/API_ID`
  * DISPLAY_NAME: (Required) The display name of the API resource. You can use any name you wish.
  * DESCRIPTION: (Optional) You can add a number of optional attributes to describe the API resource, including a description, an owner, a link to the API documentation, and more. These optional attributes are listed and described in the [API resource definition](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis).



## What's next

  * Learn how to [View API resource insights](https://docs.cloud.google.com/apigee/docs/apihub/view-api-resource-insights).
  * Learn how to [Manage API versions](https://docs.cloud.google.com/apigee/docs/apihub/manage-versions).
  * Learn about [API insights in API hub](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
