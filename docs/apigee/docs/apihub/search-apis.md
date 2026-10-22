---
url: https://docs.cloud.google.com/apigee/docs/apihub/search-apis/
title: Search API resources using semantic search \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:08.560030+00:00
---

# Search API resources using semantic search  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/search-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Search API resources using semantic search Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

The **Semantic search** add-on helps you quickly find and view the details of your API resources registered in API hub. With its AI-powered search engine, Semantic search can go beyond term "matching" and return results containing terms found anywhere in the detailed API resource entries that are semantically similar to the free text search queries entered.

Free-text search returns the following categories of results: 

  * **APIs** : A list of APIs that match the search. For each API, the following details are provided: 
    * The name of the API with a link to the API details page.
    * A brief description of the resource.
    * The name and email address of the resource owner.
  * **Versions** : A list of API versions that match the search. For each version, the following details are provided: 
    * The names of the APIs associated with the version, with a link that takes you to the API details page.
    * The name of the API version, with a link that takes you to the version details page.
    * The description of the version and related metadata.
  * **Specifications** : A list of API specifications that match the search. For each specification, the following details are provided: 
    * The names of the API associated with the specification, with a link that takes you to the API details page.
    * The name of the API specification, with a link that takes you to the version details page associated with the specification.
    * The description of the specification.
    * A link to the specification document.
    * The type of specification, such as OpenAPI spec.
  * **Operations** : A list of API operations that match the search. For each operation, the following details are provided: 
    * The names of the API associated with the operation, with a link that takes you to the API details page.
    * The name of the operation, with a link that takes you to the version details page associated with the operation.
    * The description of the specification.
    * A link to the specification document that defines the operation.
    * A link to the version that includes the operation.
  * **Deployments** : A list of deployments that match the search. For each deployment, the following details are provided: 
    * The name of the deployment.
    * The description of the deployment.
    * The deployment type. For example, Apigee hybrid. 
    * A link to the version that includes the deployment.

**Note:** The **Semantic search** add-on is enabled by default during the [API hub provisioning process](https://docs.cloud.google.com/apigee/docs/apihub/provision#step-hosting). You can however disable and enable the add-on at any time. See Disable semantic search.

## Search API hub using Semantic search

### Console

To search for APIs containing a specific term: 

  1. In the Google Cloud console, go to the API hub **Semantic search** page.

[Go to API hub](https://console.cloud.google.com//apigee/api-hub/search)

  2. Type a search query in the search box.

For example, you could enter "Order management APIs" or "Spec file for wireless carrier settings".

You can refine your search by using [system attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#system-attributes) within your search query prompt. If you created [user attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#user-attributes) when registering your APIs in API hub, you can also incorporate these attributes in your search query prompts. 

  3. The **Search results** are categorized under the following tabs: APIs, Versions, Specifications, Operations, and Deployments. Click one of the tabs to see results for a category. The results display API resources that contain terms semantically similar to the search query you entered.
  4. Click the API resource name to view the detail page for the resource.
  5. To clear the current query, click **Clear results**.



### API

To search your API hub resources using the API hub API, use the `searchResources` method:
    
    
          curl -X POST https://apihub.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:searchResources \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" \
          -d '{
            "query":"QUERY",
            "filter":"resource_type = RESOURCE_TYPE"
           }'
        

Where: 

  * **PROJECT_ID** is the ID of the host project for your API hub instance.
  * **LOCATION** is the location where your API hub instance is hosted.
  * **QUERY** is the free text query to be used in the search. The query can contain keywords related to any detail of the API hub resource, including display names, descriptions, or other metadata..
  * **RESOURCE_TYPE** is the optional filter specified for your search. You can specify one of the following API hub resource types as a filter: 
    * `Api`
    * `ApiOperation`
    * `Deployment`
    * `Definition`
    * `Spec`
    * `Version`



For example: 
    
    
          curl -X POST https://apihub.googleapis.com/v1/projects/{project-id}/locations/{location}:searchResources \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" \
          -d '{
            "query":"dog status in the store",
            "filter":"resource_type = SPEC"
            }'

This call returns a paginated list of API hub resources, with resource-specific metadata. 

For more information on free-text search with the API hub API, see the API reference documentation for [ `Method:project.locations.searchResources`](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations/searchResources).

## Disable semantic search

To disable the semantic search add-on, do the following: 

**Caution:** Disabling semantic search for a selected region can take up to **5 minutes**. You won't be able to perform any new operations in API hub until the process is complete. 

  1. In the Google Cloud console, go to the **API hub > Add-on management** page. 

[Go to Add-on management](https://console.cloud.google.com/apigee/api-hub/add-on-management)

  2. Locate the **Semantic search** card and click **Manage**. 

The **Semantic search** pane appears. 

To disable the add-on, click **Disable semantic search** , and then click **Disable** in the confirmation dialog.

  3. Click **Save**.



To re-enable the semantic search add-on, go to the **API hub > Add-on management** page, locate the **Semantic search** card, and click **Enable add-on**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
