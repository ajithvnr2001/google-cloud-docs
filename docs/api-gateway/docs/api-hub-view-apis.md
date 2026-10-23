---
url: https://docs.cloud.google.com/api-gateway/docs/api-hub-view-apis/
title: View API Gateway APIs in API hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:54.631450+00:00
---

# View API Gateway APIs in API hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/api-hub-view-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View API Gateway APIs in API hub

This page describes how to view your API Gateway APIs in API hub using the Google Cloud console or API. For more information, see [List API resources](https://docs.cloud.google.com/apigee/docs/apihub/manage-apis#listapidetails). **Note:** Only APIs and API configurations with at least one **active** and **deployed** API Gateway are available in API hub. API Gateway continuously monitors for changes in your API Gateway APIs and **removes** API metadata for gateways that are no longer active or deployed. 

View API Gateway APIs in API hub as described below. 

### Google Cloud console

To view your API Gateway APIs in API hub, do the following:

  1. In the Google Cloud console, go to the **APIs** page in **API hub**. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)

  2. Select **Gateway: API Gateway** in the **Filter** drop-down to display all API Gateway APIs.

The main API Catalog page opens showing all available APIs. 

  3. Click an API to view more details.



The following table describes the API hub fields and maps them to the API Gateway equivalents. See also [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes) in the API hub documentation for information about the other system and user-defined attributes.

API hub field | API Gateway field | Description  
---|---|---  
Overview> Name | Details> Name | Name of the API.  
Overview> API ID | N/A | ID of the API in API hub.  
Overview> Last modified | Details> Updated | Timestamp when the API was last modified.  
Versions> Name | Configs> Configuration ID | ID of the API configuration.  
Versions> Version ID | N/A | ID of the API configuration version in API hub.  
Versions> Last modified | Configs> Updated | Timestamp when the API configuration was last modified.  
Versions> Operations | `paths` in OpenAPI Spec file | Operations defined in the specification file. API Gateway details ingested include: 

  * Path
  * Specification file
  * Method
  * Deprecated flag
  * Last modified timestamp

  
Versions> Specification file | Configs> Full resource location | Specification file associated with the API configuration. API Gateway details ingested include: 

  * Name
  * Spec type
  * Lint results
  * Last modified timestamp

**Note:** Only OpenAPI specification files are ingested by API hub at this time.  
Deployments> Deployment name | Gateways> Gateway ID | API Gateway deployment in the following format:   
`LOCATION/GATEWAY_ID`  
Deployments> Deployment type | N/A | Deployment type. Set to **API Gateway**.  
Deployments> Last modified | Gateways> Updated | Timestamp when the API Gateway was last modified.  
Deployments> Resources URI | Gateways> Full resource name | Resources URI for the API Gateway in the following format:   
`projects/RUNTIME_PROJECT_ID/locations/LOCATION/gateways/GATEWAY_ID`  
Deployments> Management URL | Gateways> _gateway_ | URL used to manage the API Gateway deployment in the following format:   
`https://console.cloud.google.com/api-gateway/gateway/GATEWAY_ID/location/LOCATION?project=RUNTIME_PROJECT_ID`  
Deployments> Source project | Gateways> Full resource name | Source project for the deployment.  
Deployments> Endpoints | Gateways> Gateway URL | IP address at which the deployment resource is listening for API requests.  
Insights | **Note:** Insights information is not available for API Gateway APIs at this time.  
Security | **Note:** Security information is not available for API Gateway APIs at this time.  
  
### REST

To list all API Gateway APIs in API hub, use the [List APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apis/list) API. By adding the plugin instance filter, you can list only the API assets for the specified API Gateway plugin instance.

For example:
    
    
    curl 'https://apihub.googleapis.com/v1/projects/HUB_PROJECT_ID/locations/HUB_LOCATION/apis?filter=source_metadata.plugin_instance_action_source.plugin_instance="projects/HUB_PROJECT_ID/locations/HUB_LOCATION/plugins/PLUGIN_TYPE/instances/PLUGIN_INSTANCE_ID"' \
      -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)"
    

Replace the following:

  * HUB_PROJECT_ID: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * HUB_LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
  * PLUGIN_TYPE: Type of plugin. Set to **system-api-gateway**.
  * PLUGIN_INSTANCE_ID: ID of the API Gateway plugin instance. Use the [list plugin instances](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.plugins.instances/list) API to get the plugin instance ID.



The following provides an example of the response.
    
    
    {
      "apis": [
        {
          "name": "projects/myproject/locations/us-west1/apis/4fc95784-16b0-4b6e-8b7f-a08607febf78",
          "displayName": "test-api-1",
          "versions": [
            "projects/myproject/locations/us-west1/apis/4fc95784-16b0-4b6e-8b7f-a08607febf78/versions/843a7e72-c5d2-4af8-95b0-162fa5d5ea10",
            "projects/myproject/locations/us-west1/apis/4fc95784-16b0-4b6e-8b7f-a08607febf78/versions/b6af2674-4a0e-410e-990d-d90ccbe6867e"
          ],
          "createTime": "2025-12-12T18:55:54.445487Z",
          "updateTime": "2025-12-12T18:55:54.445487Z",
          "apiStyle": {
            "attribute": "projects/myproject/locations/us-west1/attributes/system-api-style",
            "enumValues": {
              "values": [
                {
                  "id": "rest",
                  "displayName": "REST",
                  "description": "REST",
                  "immutable": true
                }
              ]
            }
          },
          "fingerprint": "test-api-1",
          "sourceMetadata": [
            {
              "pluginInstanceActionSource": {
                "pluginInstance": "projects/myproject/locations/us-west1/plugins/system-api-gateway/instances/90b21a65-38b4-4159-8e9d-07a8b6cecab0",
                "actionId": "sync-metadata"
              },
              "sourceType": "PLUGIN",
              "originalResourceId": "projects/runtimeproject/locations/global/apis/test-api-1",
              "originalResourceCreateTime": "2025-12-11T01:57:54.841944920Z",
              "originalResourceUpdateTime": "0001-01-01T00:00:00Z"
            }
          ]
        }
      ]
    }

The following table describes the fields that are populated with API metadata from API Gateway in the response. See also [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes) in the API hub documentation for information about the other system and user-defined attributes.

API field | Description  
---|---  
`name` | ID of the API in API hub the following format: `projects/HUB_PROJECT_ID/locations/HUB_LOCATION/apis/API_ID` **Note:** The API_ID is used in the resource name to ensure the value is unique.  
`displayName` | Display name of the API.  
`createTime` | Timestamp when the API was created.  
`updateTime` | Timestamp when the API was created.  
`fingerprint` | Unique ID for API (usually set to display name).  
`sourceMetadata` | API Gateway plugin instance information including: 

  * Plugin instance ID in the following format: `projects/HUB_PROJECT_ID/locations/HUB_LOCATION/plugins/system-api-gateway/instances/PLUGIN_INSTANCE_ID`
  * Original API Gateway resource name in the following format: `projects/RUNTIME_PROJECT_ID/locations/LOCATION/apis/API_ID`

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
