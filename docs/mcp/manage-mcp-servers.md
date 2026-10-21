---
url: https://docs.cloud.google.com/mcp/manage-mcp-servers/
title: Manage MCP servers \u00a0|\u00a0 Google Cloud MCP servers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:50:53.010672+00:00
---

# Manage MCP servers  |  Google Cloud MCP servers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/manage-mcp-servers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Guides ](https://docs.cloud.google.com/mcp/overview)



Send feedback 

#  Manage MCP servers Stay organized with collections  Save and categorize content based on your preferences. 

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers let your AI applications connect with databases, calendars, productivity tools, and APIs. You can list available Google and Google Cloud remote MCP servers, authenticate your AI applications, and configure optional security and safety settings.

You can use MCP servers when building AI applications or when working with AI assistants such as Claude Code, Gemini Code Assist, Gemini CLI, and Google AI Studio. Because Google and Google Cloud MCP servers run on Google infrastructure instead of your local machine, their endpoints are available as soon as you enable the service API. For more information, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Required roles

To get the permissions that you need to use MCP servers, ask your administrator to grant you the Make MCP tool calls to Google and Google Cloud MCP tools IAM role on the Google Cloud project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to use MCP servers. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use MCP servers:

  * Make MCP tool calls to Google and Google Cloud MCP tools: 
    * `mcp.tools.call`
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Available MCP servers

Available Google and Google Cloud remote MCP servers are listed in [Supported products](https://docs.cloud.google.com/mcp/supported-products) and are registered in [Agent Registry](https://docs.cloud.google.com/agent-registry/overview) when you enable the product or service.

## Manage MCP with Agent Registry

To list your available MCP servers and get updated tool descriptions, see [Manage MCP tools in Agent Registry](https://docs.cloud.google.com/agent-registry/manage-mcp-tools).

## List available tools, prompts, and resources

Most MCP clients automatically list available tools, prompts, and resources. The following tabs describe how to manually list them using HTTP requests:

###  Tools 

To get a list of available tools and their descriptions, MCP clients use the MCP [tools/list](https://modelcontextprotocol.io/specification/2026-07-28/server/tools#listing-tools) method in an HTTP request to the MCP server or toolset endpoint. Authentication isn't required for the `tools/list` method.
    
    
    POST /TOOLSET_ENDPOINT HTTP/1.1
    Host: SERVICE_NAME
    Content-Type: application/json
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "tools/list",
      "params": {
        "cursor": "OPTIONAL_CURSOR_VALUE",
        "_meta": {
          "io.modelcontextprotocol/protocolVersion": "MCP_PROTOCOL_VERSION",
          "io.modelcontextprotocol/clientCapabilities": {
            "extensions": {
              "io.modelcontextprotocol/ui": {
                "mimeTypes": ["text/html;profile=mcp-app"]
              }
            ...
            }
          }
        }
      }
    }
    

Replace the following:

  * `SERVICE_NAME`: The service name—for example, the BigQuery service name is `bigquery.googleapis.com`. For information about listing enabled services, see [List services](https://docs.cloud.google.com/service-usage/docs/list-services). To see a list of Google and Google Cloud services that have remote MCP servers without running commands, see [Supported products](https://docs.cloud.google.com/mcp/supported-products).
  * `TOOLSET_ENDPOINT`: The remainder of the MCP endpoint after the service name. For example, for Gemini Enterprise Agent Platform, this might be `mcp/models` or `mcp/generate`.
  * `OPTIONAL_CURSOR_VALUE`: The cursor value from the previous response, used to retrieve the next page of results.
  * `MCP_PROTOCOL_VERSION`: The MCP protocol version. For example, `2026-07-28`.



You can send an HTTP request to list tools directly to a Google remote MCP server with the following command:
    
    
    curl -X POST https://SERVICE_NAME/TOOLSET_ENDPOINT \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
        -H 'MCP-Protocol-Version: 2026-07-28' \
        -H 'Mcp-Method: tools/list' \
        -d '{
          "jsonrpc": "2.0",
          "id": 1,
          "method": "tools/list",
          "params": {
            "_meta": {
              "io.modelcontextprotocol/protocolVersion": "2026-07-28",
              "io.modelcontextprotocol/clientCapabilities": {
                "extensions": {
                  "io.modelcontextprotocol/ui": {
                    "mimeTypes": ["text/html;profile=mcp-app"]
                  }
                }
              }
            }
          }
        }'
    

The response resembles the following:
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": {
        "tools": [
          {
            "name": "list_topics",
            "title": "List Topics",
            "description": "Get list of available topics.",
            "input_schema": {...}
            "output_schema": {...}
          },
          {
            "name": "get_topic",
            "title": "Get Topic",
            "description": "Get messages in a Topic.",
            "input_schema": {...}
            "output_schema": {...}
          },
          "nextCursor": "next-page-cursor",
          "ttlMs": 300000,
          "cacheScope": "public"
          ...
        ]
      }
    }
    

For more information about the structure of the response, see the MCP specification for [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools), [caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching), and [pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination).

###  Prompts 

To get a list of available prompts and their descriptions, MCP clients use the MCP [prompts/list](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts#listing-prompts) method in an HTTP request to the MCP server or toolset endpoint. Authentication isn't required for the `prompts/list` method. All prompts are listed for all toolsets, even if they don't apply to the toolset that you're using.
    
    
    POST /TOOLSET_ENDPOINT HTTP/1.1
    Host: SERVICE_NAME
    Content-Type: application/json
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "prompts/list",
      "params": {
        "cursor": "OPTIONAL_CURSOR_VALUE",
        "_meta": {
          "io.modelcontextprotocol/protocolVersion": "MCP_PROTOCOL_VERSION",
          "io.modelcontextprotocol/clientCapabilities": {
            "extensions": {
              "io.modelcontextprotocol/ui": {
                "mimeTypes": ["text/html;profile=mcp-app"]
              }
            }
          }
        }
      }
    }
    

Replace the following:

  * `SERVICE_NAME`: The service name—for example, the BigQuery service name is `bigquery.googleapis.com`. For information about listing enabled services, see [List services](https://docs.cloud.google.com/service-usage/docs/list-services). To see a list of Google and Google Cloud services that have remote MCP servers without running commands, see [Supported products](https://docs.cloud.google.com/mcp/supported-products).
  * `TOOLSET_ENDPOINT`: The remainder of the MCP endpoint after the service name. For example, for Gemini Enterprise Agent Platform, this might be `mcp/models` or `mcp/generate`.
  * `OPTIONAL_CURSOR_VALUE`: The cursor value from the previous response, used to retrieve the next page of results.
  * `MCP_PROTOCOL_VERSION`: The MCP protocol version. For example, `2026-07-28`.



You can send an HTTP request to list prompts directly to a Google remote MCP server with the following command:
    
    
    curl -X POST https://SERVICE_NAME/TOOLSET_ENDPOINT \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
        -H 'MCP-Protocol-Version: 2026-07-28' \
        -H 'Mcp-Method: prompts/list' \
        -d '{
          "jsonrpc": "2.0",
          "id": 1,
          "method": "prompts/list",
          "params": {
            "_meta": {
              "io.modelcontextprotocol/protocolVersion": "2026-07-28",
              "io.modelcontextprotocol/clientCapabilities": {
                "extensions": {
                  "io.modelcontextprotocol/ui": {
                    "mimeTypes": ["text/html;profile=mcp-app"]
                  }
                }
              }
            }
          }
        }'
    

**Note:** Not all MCP servers support prompts. Calling `prompts/list` on a server that does not support prompts results in an error.

The response resembles the following:
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": {
        "prompts": [
          {
            "name": "deploy",
            "description": "Deploys the current working directory to Cloud Run.",
            "arguments": [
              {
                "name": "name",
                "description": "Name of the Cloud Run service to deploy to.",
                "required": false
              }
            ]
          },
          "nextCursor": "next-page-cursor",
          "ttlMs": 600000,
          "cacheScope": "public"
          ...
        ]
      }
    }
    

For more information about the structure of the response, see the MCP specification for [prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts), [caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching), and [pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination).

###  Resources 

To get a list of available resources and their descriptions, MCP clients use the MCP [resources/list](https://modelcontextprotocol.io/specification/2026-07-28/server/resources#listing-resources) method in an HTTP request to the MCP server or toolset endpoint. Authentication isn't required for the `resources/list` method. All resources are listed for all toolsets.
    
    
    POST /TOOLSET_ENDPOINT HTTP/1.1
    Host: SERVICE_NAME
    Content-Type: application/json
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "resources/list",
      "params": {
        "cursor": "OPTIONAL_CURSOR_VALUE",
        "_meta": {
          "io.modelcontextprotocol/protocolVersion": "MCP_PROTOCOL_VERSION",
          "io.modelcontextprotocol/clientCapabilities": {
            "extensions": {
              "io.modelcontextprotocol/ui": {
                "mimeTypes": ["text/html;profile=mcp-app"]
              }
            }
          }
        }
      }
    }
    

Replace the following:

  * `SERVICE_NAME`: The service name—for example, the BigQuery service name is `bigquery.googleapis.com`. For information about listing enabled services, see [List services](https://docs.cloud.google.com/service-usage/docs/list-services). To see a list of Google and Google Cloud services that have remote MCP servers without running commands, see [Supported products](https://docs.cloud.google.com/mcp/supported-products).
  * `TOOLSET_ENDPOINT`: The remainder of the MCP endpoint after the service name. For example, for Gemini Enterprise Agent Platform, this might be `mcp/models` or `mcp/generate`.
  * `OPTIONAL_CURSOR_VALUE`: The cursor value from the previous response, used to retrieve the next page of results.
  * `MCP_PROTOCOL_VERSION`: The MCP protocol version. For example, `2026-07-28`.



You can send an HTTP request to list resources directly to a Google remote MCP server with the following command:

**Note:** Not all MCP servers support resources. Calling `resources/list` on a server that does not support resources results in an error.
    
    
    curl -X POST https://SERVICE_NAME/TOOLSET_ENDPOINT \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
        -H 'MCP-Protocol-Version: 2026-07-28' \
        -H 'Mcp-Method: resources/list' \
        -d '{
          "jsonrpc": "2.0",
          "id": 1,
          "method": "resources/list",
          "params": {
            "_meta": {
              "io.modelcontextprotocol/protocolVersion": "2026-07-28",
              "io.modelcontextprotocol/clientCapabilities": {
                "extensions": {
                  "io.modelcontextprotocol/ui": {
                    "mimeTypes": ["text/html;profile=mcp-app"]
                  }
                }
              }
            }
          }
        }'
    

The response resembles the following:
    
    
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": {
        "resources": [
          {
            "uri": "file:///project/src/main.rs",
            "name": "main.rs",
            "title": "Rust Software Application Main File",
            "description": "Primary application entry point",
            "mime_type": "text/x-rust"
          },
          "nextCursor": "next-page-cursor",
          "ttlMs": 300000,
          "cacheScope": "public"
          ...
        ]
      }
    }
    

For more information about the structure of the response, see the MCP specification for [resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources), [caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching), and [pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination).

## Authenticate your AI application

Once you have enabled a product or service that supports MCP in your project, you can use your Google credentials to authenticate and use its tools through your AI application. For safety and observability, you might want to create a separate identity with specific permissions for your application instead of using your own permissions if you are working with production resources. For more information, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).

## Optional security and safety configurations

MCP tools can take a wide variety of actions on behalf of AI applications, introducing security risks and considerations. To help you minimize and manage these risks, Google Cloud provides default and customizable policies that control how MCP tools are used within your Google Cloud organization or project. For more information about MCP security and governance, see [AI security and safety](https://docs.cloud.google.com/mcp/ai-security-safety).

### Enable Model Armor

[Model Armor](https://docs.cloud.google.com/model-armor/overview) is a Google Cloud service designed to enhance the security and safety of your AI applications. It works by proactively screening LLM prompts and responses, protecting against various risks and supporting responsible AI practices. Whether you are deploying AI in your cloud environment, or on external cloud providers, Model Armor can help you prevent malicious input, verify content safety, protect sensitive data, maintain compliance, and enforce your AI safety and security policies consistently across your diverse AI landscape.

When Model Armor is enabled with [logging enabled](https://docs.cloud.google.com/model-armor/configure-logging), Model Armor logs the entire payload. This might expose sensitive information in your logs.

#### MCP request routing to Model Armor

Model Armor is available in [certain regions](https://docs.cloud.google.com/model-armor/locations). When Model Armor is enabled and you use an MCP server in a jurisdiction that Model Armor doesn't support, the routing behavior of the call might be different for different MCP servers and might break data residency compliance for in-use and in-transit data. For more information about the behavior of individual MCP servers, see [Model Armor supported products](https://docs.cloud.google.com/mcp/model-armor-supported-products). 

To enable Model Armor, complete the steps in [Configure Model Armor protection for Google and Google Cloud MCP servers](https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration).

#### Model Armor logging

For information about Model Armor audit and platform logs, see [Model Armor audit logging](https://docs.cloud.google.com/model-armor/audit-logging-model-armor).

## Use MCP servers

To use Google and Google Cloud remote MCP servers, AI applications must have the MCP Tool User role (`roles/mcp.toolUser`) and the necessary service permissions for the tool's Google Cloud service.

To grant the MCP Tool User role, run the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="PRINCIPAL" \
        --role="roles/mcp.toolUser"
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project.
  * `PRINCIPAL`: the [principal identifier](https://docs.cloud.google.com/iam/docs/principal-identifiers) for the identity you are granting the MCP Tool User role to. For information about the types of principals available on Google Cloud, see [Identity and Access Management (IAM) Principals](https://docs.cloud.google.com/iam/docs/principals-overview).



## What's next

  * Learn about [access control with IAM](https://docs.cloud.google.com/mcp/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
