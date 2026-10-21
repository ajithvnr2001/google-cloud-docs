---
url: https://docs.cloud.google.com/apigee/docs/apihub/register-mcp-apis/
title: Register MCP APIs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:03:13.809949+00:00
---

# Register MCP APIs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/register-mcp-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Register MCP APIs Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

API hub supports the Model Context Protocol (MCP) as a first-class API style, alongside REST, gRPC, and others. You can import, register, and manage MCP APIs and their associated tools directly within API hub, creating a centralized registry for your agentic APIs and services. 

For information about MCP in Apigee, see [MCP in Apigee overview](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview). 

## Import Apigee MCP proxies

API hub automatically imports all MCP proxies created in your associated Apigee organization. These proxies are registered with the **MCP** API style, and their specification files are parsed to extract MCP tools. 

If you have additional runtime projects that are not currently attached to your API hub instance, you can attach them manually from the **API hub > Settings** page. For more information, see [Attach a runtime project](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#attach-a-runtime-project). 

**Important:**

  * When Apigee MCP proxies are imported, API hub identifies the associated OpenAPI Specification (OAS) files as MCP specs and parses them to extract MCP tools. While the specification type is updated to **MCP** , the underlying OAS file is not currently converted to the MCP specification schema. This is a known issue.
  * For Apigee MCP proxies with multiple deployment revisions, API hub only parses MCP tools from the latest deployed revision. Tools from earlier revisions are not available or supported.



## Register an MCP API

You can register MCP APIs using the Google Cloud console or the API hub API. 

### Console

To register a MCP API, do the following:

  1. In the Google Cloud console, go to the **API hub > APIs** page. 

[ Go to APIs](https://console.cloud.google.com/apigee/api-hub/apis)

  2. Provide the required API details.
  3. Under **System attributes** , set the **API style** to **MCP**.
  4. Click **Register**.

The MCP API is registered. You can edit the API details and attach a specification file at a later time. 




### REST

To register a MCP API, use the [Create API](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis/create) REST API.
    
    
    curl -X POST -H "Content-Type: application/json" 
    -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/apis?api_id=API_ID 
    -d '{
      "display_name": "DISPLAY_NAME",
      "description": "DESCRIPTION",
      "owner": {
        "display_name": "OWNER_DISPLAY_NAME",
        "email": "OWNER_EMAIL"
      },
      "api_style": {
        "enum_values": {
          "values": [
            {
              "id": "mcp-api"
            }
          ]
        }
      },
      "attributes": {
        "projects/HUB_PROJECT/locations/HUB_LOCATION/custom-attribute-1": {
          "attribute": "projects/HUB_PROJECT/locations/HUB_LOCATION/custom-attribute-1",
          "enum_values": {
            "values": [
              {
                "id": "ATTRIBUTE_VALUE"
              }
            ]
          }
        }
      }
    }'
      

Replace the following:

  * HUB_PROJECT: The project ID of the API hub instance.
  * HUB_LOCATION: The location of the API hub instance.
  * API_ID: The ID of the API resource.
  * DISPLAY_NAME: The display name of the API resource. You can use any name you wish.
  * DESCRIPTION: A description of the API resource.
  * OWNER_DISPLAY_NAME: The display name of the API owner.
  * OWNER_EMAIL: The email address of the API owner.
  * ATTRIBUTE_VALUE: The value of a custom user-defined attribute. This is optional. **Caution:** Avoid adding sensitive data to user-defined attributes. 



## View MCP APIs

The API list view in API hub allows you to filter APIs by style to find specific resources. To view only registered MCP APIs, select the **MCP** filter tag at the top of the list. 

[ Go to API list view](https://console.cloud.google.com/apigee/api-hub/apis)

The following image shows the API list view in API hub, with the top filter tags highlighted:

![API list view with MCP filter tags highlighted](https://docs.cloud.google.com/static/apigee/docs/apihub/images/mcp-apis.png)

## What's next

  * Learn how to [Manage MCP tools](https://docs.cloud.google.com/apigee/docs/apihub/manage-mcp-tools).
  * Learn how to [Manage API resources](https://docs.cloud.google.com/apigee/docs/apihub/manage-apis).
  * Learn how to [Manage MCP proxies](https://docs.cloud.google.com/apigee/docs/apihub/manage-mcp-proxies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
