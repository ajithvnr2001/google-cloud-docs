---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-mcp-proxies/
title: Manage MCP proxies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:19.994865+00:00
---

# Manage MCP proxies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-mcp-proxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage MCP proxies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

API hub simplifies the creation of Model Context Protocol (MCP) proxies by providing a centralized interface for composing MCP tools out of existing Apigee proxies. While MCP proxies can be manually configured in Apigee, API hub allows you to browse your registered API catalog, select specific operations across different versions, and automatically bundle them into a unified MCP discovery proxy. This streamlined workflow automates the generation of the MCP proxy specification and deploys it directly to your Apigee environment, making your APIs instantly accessible to AI agents.

This page describes how to create and deploy MCP proxies using API hub.

## Before you begin

  * **Required roles:** Ensure you have the following roles in your Google Cloud project: 
    * `roles/apihub.admin`: To manage APIs and specifications within API hub.
    * `roles/apigee.admin`: To deploy and manage proxies in Apigee.

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You can also get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

  * **API hub setup:** A Google Cloud runtime project must be attached to API hub, and the Apigee plugin must be active. Only Apigee proxies imported using this plugin can be converted into MCP tools. For more information, see [Manage Google Cloud plugins](https://docs.cloud.google.com/apigee/docs/apihub/manage-gcp-plugins).
  * **Associated specification files:** The Apigee proxy must have an OpenAPI specification (OAS) file in its proxy bundle. The Apigee plugin automatically detects and uploads this file to API hub. **Note:** In the proxy's specification file, ensure the path is the relative path of the API operation. Do not include the proxy basepath, as this will cause mapping in API hub to fail.
  * **Deployment status:** The source proxy must be deployed in an Apigee environment that is attached to an environment group.



## Create an MCP proxy

You can create an MCP proxy using the Google Cloud console or the API hub API.

### Console

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. In the **APIs** page, click **Configure MCP tools**.
  3. In the **Proxy details** section, do the following: 
     1. From the **Apigee runtime project** dropdown menu, choose the project you want to use for deploying the MCP proxy.
     2. From the **Apigee environment group** dropdown menu, choose the environment group where the MCP proxy will be available.
     3. In the **MCP proxy name** field, enter a unique name for the discovery proxy.
     4. In the **Description** field, enter a clear description for the proxy.
     5. From the **Deployment environment** dropdown menu, choose the specific environment for deploying the proxy.
     6. Click **Continue** to proceed to tool selection.
  4. In the **MCP tools** section, click **Add tools**. Repeat this process to include operations from multiple APIs as needed. 
     1. From the **API** dropdown, select the registered API from your catalog that contains the operations you want to use.
     2. From the **Version** dropdown, select the specific version of the API. This allows you to precisely control which version's logic and data structures are exposed to the AI agent. 
     3. Select the deployment associated with that version.
     4. The **Specification** menu lists the specification files linked to the selected deployment. Select the specification file that contains the operations you want to convert into an MCP tool. **Note:** Operations will only appear if a valid OpenAPI Specification (OAS) file is included in the Apigee proxy bundle.
     5. The **Select Operations** section lists all operations found in the specification. Select the operations you want to convert into an MCP tool.
     6. Click **Add** to include these operations in your MCP proxy configuration.
     7. The tool name and description are auto-populated based on the selected operations. Click the **Edit** icon to modify the tool name and description, if needed. **Note:** Each tool name must be unique within the MCP server.
  5. Click **Continue**.
  6. In the **Review and deploy** section, review the following details: 
     1. Tools: Verify the API operations that will be exposed as tools.
     2. MCP Proxy details: Verify the runtime project, environment group, MCP proxy name, and description.
  7. Click **Deploy in Apigee**. 

You will be redirected to the Apigee **API Proxies** page to check the deployment status of the MCP proxy.




### REST

To create an MCP proxy, use the [Configure and deploy server](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.servers/configureAndDeployServer) API. Use the following command:
    
    
        curl --location 'https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/servers:configureAndDeployServer' \
        --header "Authorization: Bearer $(gcloud auth print-access-token)" \
        --header 'Content-Type: application/json' \
        --data '{
          "mcp_server_config": {
            "apigee_x_target_details": {
              "environment": "APIGEE_ENVIRONMENT",
              "proxy": "APIGEE_PROXY",
              "target_project": "TARGET_PROJECT",
              "metadata": {
                "display_name": "DISPLAY_NAME",
                "description": "DESCRIPTION"
              }
            },
            "tools": [
              {
                "tool_id": "TOOL_1_ID",
                "description": "TOOL_1_DESCRIPTION",
                "operation": {
                  "http_operation": {
                    "spec": "projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_1_ID/versions/VERSION_1_ID/specs/SPEC_1_ID",
                    "path": "HTTP_PATH",
                    "method": "HTTP_METHOD"
                  }
                }
              },
              {
                "tool_id": "TOOL_2_ID",
                "description": "TOOL_2_DESCRIPTION",
                "operation": {
                  "operation": "projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_2_ID/versions/VERSION_2_ID/operations/OPERATION_ID"
                }
              }
            ]
          }
        }'
    

Replace the following:

  * HUB_PROJECT: The project ID of the API hub instance.
  * HUB_LOCATION: The location of the API hub instance.
  * TARGET_PROJECT: The target Google Cloud project ID for Apigee X.
  * APIGEE_ENVIRONMENT: The Apigee environment name (e.g., test).
  * APIGEE_PROXY: The name of the Apigee proxy.
  * DISPLAY_NAME: The display name of the server backend revision. You can use any name you wish.
  * DESCRIPTION: A description of the server configuration.
  * TOOL_1_ID, TOOL_2_ID: The ID for the tool (e.g., tool_1).
  * TOOL_1_DESCRIPTION, TOOL_2_DESCRIPTION: A description of the tool.
  * API_1_ID, API_2_ID: The ID of the API resource for the tool.
  * VERSION_1_ID, VERSION_2_ID: The ID of the API version for the tool.
  * SPEC_1_ID: The ID of the API spec for the tool.
  * HTTP_PATH: The HTTP path for the tool's operation (e.g., /entities).
  * HTTP_METHOD: The HTTP method for the tool's operation (e.g., GET).
  * OPERATION_ID: The ID of the tool's specific API operation.



## Edit an MCP proxy

You can edit an MCP proxy that was created in API hub or directly in Apigee, to add or remove tools. If an MCP proxy was created directly in Apigee, you can update it in API hub, provided the MCP specification and underlying proxies (used as tools) are configured correctly.

### Console

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. In the **APIs** page, click the **MCP** filter. This displays a list of MCP proxies.
  3. Locate the MCP proxy you want to edit and click **Apigee MCP tools**.
  4. From the **Select deployment** dropdown menu, select a deployment associated with the MCP proxy. **Note:** The **Select deployment** dropdown is visible only if the proxy was manually created in Apigee and there are multiple deployments associated with the MCP proxy.
  5. Click **Apigee MCP tools**.
  6. In the **Proxy details** section, you can edit the proxy name and description.
  7. Click **Continue**.
  8. In the **MCP tools** section, you can add, edit, or remove tools as needed.
  9. Click **Continue**.
  10. In the **Review and deploy proxy** section, review the updated configuration.
  11. Click **Deploy in Apigee**. 

You will be redirected to the Apigee API Proxies page to check the deployment status of the MCP proxy.




### REST

To update an MCP proxy, use the [Configure and deploy server](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.servers/configureAndDeployServer) API. Use the following command:
    
    
        curl --location 'https://apihub.googleapis.com/v1/projects/HUB_PROJECT/locations/HUB_LOCATION/servers:configureAndDeployServer' \
        --header "Authorization: Bearer $(gcloud auth print-access-token)" \
        --header 'Content-Type: application/json' \
        --data '{
          "mcp_server_config": {
            "apigee_x_target_details": {
              "environment": "APIGEE_ENVIRONMENT",
              "proxy": "APIGEE_PROXY",
              "target_project": "TARGET_PROJECT",
              "metadata": {
                "display_name": "DISPLAY_NAME",
                "description": "DESCRIPTION"
              }
            },
            "tools": [
              {
                "tool_id": "TOOL_1_ID",
                "description": "TOOL_1_DESCRIPTION",
                "operation": {
                  "http_operation": {
                    "spec": "projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_1_ID/versions/VERSION_1_ID/specs/SPEC_1_ID",
                    "path": "HTTP_PATH",
                    "method": "HTTP_METHOD"
                  }
                }
              },
              {
                "tool_id": "TOOL_2_ID",
                "description": "TOOL_2_DESCRIPTION",
                "operation": {
                  "operation": "projects/HUB_PROJECT/locations/HUB_LOCATION/apis/API_2_ID/versions/VERSION_2_ID/operations/OPERATION_ID"
                }
              }
            ]
          }
        }'
    

Replace the following:

  * HUB_PROJECT: The project ID of the API hub instance.
  * HUB_LOCATION: The location of the API hub instance.
  * TARGET_PROJECT: The target Google Cloud project ID for Apigee X.
  * APIGEE_ENVIRONMENT: The Apigee environment name (e.g., test).
  * APIGEE_PROXY: The name of the Apigee proxy.
  * DISPLAY_NAME: The display name of the server backend revision. You can use any name you wish.
  * DESCRIPTION: A description of the server configuration.
  * TOOL_1_ID, TOOL_2_ID: The ID for the tool (e.g., tool_1).
  * TOOL_1_DESCRIPTION, TOOL_2_DESCRIPTION: A description of the tool.
  * API_1_ID, API_2_ID: The ID of the API resource for the tool.
  * VERSION_1_ID, VERSION_2_ID: The ID of the API version for the tool.
  * SPEC_1_ID: The ID of the API spec for the tool.
  * HTTP_PATH: The HTTP path for the tool's operation (e.g., /entities).
  * HTTP_METHOD: The HTTP method for the tool's operation (e.g., GET).
  * OPERATION_ID: The ID of the tool's specific API operation.



## Limitations

  * API hub only manages MCP tool-to-Apigee operation mappings. Policy modifications within the proxy must be done in Apigee.
  * Complete deletion of an MCP proxy is not supported in API hub. At least one tool must always remain. You can delete the MCP proxy directly in Apigee, if needed.
  * When adding a tool, you cannot select an API which is deployed in an environment group different than the one selected while configuring the MCP proxy in API hub.
  * If any configured tool loses its valid reverse proxy mapping (for example, the proxy was undeployed), you cannot edit the MCP proxy in API hub. You must fix the broken mapping in Apigee.
  * In API hub, you can only deploy an MCP proxy to a single environment. Multi-environment deployment for the same MCP proxy is not supported.



## Troubleshooting

You might encounter the following common issues when configuring MCP proxies in API hub:

### Missing specification files when adding tools

**Cause:** Specification ingestion failed for the API proxy. A valid OAS file must be included in the proxy bundle to generate the specification list in API hub.

**Recommendation action:**

  1. Verify the API proxy is deployed in the selected environment.
  2. In the APIs page, locate the API and check if a specification file is available for the API version.
  3. If the specification file is missing, upload a valid OAS file to the Apigee proxy, and then redeploy the proxy for it to appear in API hub properly.



### "Reverse proxy not found" error when entering proxy details

**Cause:** The MCP proxy's operations in Apigee do not match the reverse proxy operations in API hub.

**Recommendation action:**

Ensure that the operation path (excluding any basepath) and HTTP method defined in the MCP proxy's OAS in Apigee exactly match those in the reverse proxy's OAS in API hub.

The following is an example of a valid MCP proxy configuration:

MCP proxy OAS operation:
    
    
    /v1/orders:
      get:
        operationId: getOrders
        summary: Get orders
    

Reverse proxy OAS operation:
    
    
    /orders:
      get:
        operationId: getOrders
        summary: Get orders
    

In this example, the MCP OAS operation path `/v1/orders` has a basepath of `/v1`. When this basepath is excluded, the remaining path is `/orders`. Since this matches the reverse proxy's OAS operation path `/orders` and both use the `GET` method, the mapping is valid.

### Errors when selecting environment group

**Cause:** API hub only supports one MCP proxy deployed to a single environment per environment group. The error typically occurs from one of the following scenarios:

  * Multiple MCP proxies are deployed to different environments within the same environment group.
  * An MCP proxy is deployed to multiple environments within a single environment group.
  * An MCP proxy is deployed to an environment attached to more than one environment group.



**Recommendation action:**

  * **For multiple MCP proxies:**
    1. List all MCP proxies deployed across all environments in the selected environment group in Apigee.
    2. Undeploy the extra MCP proxy or move it to a different environment group, as only one MCP proxy per environment group is supported.
  * **For a single MCP proxy in multiple environments:**
    1. List the deployments of the MCP proxy in Apigee to check for multiple environment entries within the same group.
    2. Reduce the deployment to a single environment per environment group.
  * **For a single MCP proxy in an environment attached to multiple environment groups:**
    1. Verify the environment's group attachments in Apigee.
    2. Detach the environment from any extra environment groups so that it belongs to exactly one group.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
