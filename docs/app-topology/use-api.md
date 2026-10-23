---
url: https://docs.cloud.google.com/app-topology/use-api/
title: Use the App Topology API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:12.683679+00:00
---

# Use the App Topology API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/use-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ Guides ](https://docs.cloud.google.com/app-topology/overview)



Send feedback 

#  Use the App Topology API Stay organized with collections  Save and categorize content based on your preferences. 

You can programmatically run queries to correlate data across Google Cloud by using the REST API or Google Cloud CLI.

## Overview

When you run an App Topology API query, the API returns a list of graph nodes (resources) and edges (relationships) that match your query. App Topology combines data across Google Cloud services such as:

  * Resource metadata from Cloud Asset Inventory, App Hub, Agent Registry
  * Deployment data, such as a Git commit or build provenance of a container image
  * Security data from Security Command Center such as vulnerabilities or Identity and Access Management (IAM) ownership
  * Google Cloud Observability data such as traces and alerts



To run a query, you need the following information:

  * The domain that you want to query. The `SRE` domain includes all supported data. See list domains to learn about listing available domains.
  * The supported graph nodes, edges, and properties that you can include in a query. You can get the full or partial schema for a domain. For details, see Get the schema.
  * The query pattern with the nodes and edges that you want to search for. See Run queries.



## Before you begin

  1. [Set up App Topology](https://docs.cloud.google.com/app-topology/setup).

  2. Select the tab for how you plan to use the samples on this page:

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

For information about setting up authentication for a production environment, see [ Set up Application Default Credentials for code running on Google Cloud ](https://docs.cloud.google.com/docs/authentication/set-up-adc-attached-service-account) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to use the App Topology API, ask your administrator to grant you the following IAM roles: 

  * Run queries: [App Topology Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/apptopology#apptopology.viewer) (`roles/apptopology.viewer`) on the projects where you want to use App Topology 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the App Topology API. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the App Topology API:

  * Get domains: 
    * `apptopology.domains.get`
    * `apptopology.domains.list`
  * Get schemas: `apptopology.schemas.get`
  * Get discovered resource data: `apptopology.discoveredResourcesTopologies.generate`
  * Get DevOps domain data: `apptopology.devOpsDomainTopologies.generate`
  * Get Security domain data: `apptopology.securityDomainTopologies.generate`
  * Get SRE domain data (all supported data): `apptopology.sreDomainTopologies.generate`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List domains

[Domains](https://docs.cloud.google.com/app-topology#domains) are sets of resource data focused on specific types of queries.

  * To query all data supported by App Topology, use the `SRE` domain.
  * To get data about agentic resources, you must use the `SRE` domain.
  * All examples of request responses in this document use the `SRE` domain.



If needed, you can list domains that are available in a project.

### gcloud

List domains

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: Your project ID



Execute the [gcloud app-topology domains list](https://docs.cloud.google.com/sdk/gcloud/reference/app-topology/domains/list) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud app-topology domains list --project=PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud app-topology domains list --project=PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud app-topology domains list --project=PROJECT_ID

You should receive a response similar to the following:
    
    
    NAME
    DEVOPS
    SECURITY
    SRE
    

### REST

List domains

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your project ID



HTTP method and URL: 
    
    
    GET https://apptopology.googleapis.com/v1/projects/PROJECT_ID/locations/global/domains

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://apptopology.googleapis.com/v1/projects/PROJECT_ID/locations/global/domains"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://apptopology.googleapis.com/v1/projects/PROJECT_ID/locations/global/domains" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "domains": [
        {
          "name": "projects/PROJECT_ID/locations/global/domains/DEVOPS"
        },
        {
          "name": "projects/PROJECT_ID/locations/global/domains/SECURITY"
        },
        {
          "name": "projects/PROJECT_ID/locations/global/domains/SRE"
        }
      ]
    }
    

## Get the schema

To help you build your queries, you can get a list of all supported nodes, edges, and properties for a domain. The REST API also lets you get a portion of the schema.

Requests for the full schema can take significantly longer than requests for a partial schema because of the large number of items in the schema.

### Get the full schema

### gcloud

Get full schema

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: Your project ID
  * DOMAIN: The domain that you want to query. The `SRE` domain includes all supported data.



Execute the [gcloud app-topology domains schema describe](https://docs.cloud.google.com/sdk/gcloud/reference/app-topology/domains/schema/describe) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud app-topology domains schema describe DOMAIN --project=PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud app-topology domains schema describe DOMAIN --project=PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud app-topology domains schema describe DOMAIN --project=PROJECT_ID

The following example excerpt from a response only includes the first item in the schema for node types, edge types, edge rules, and label properties.
    
    
    {
      "nodeTypes": [
        {
          "type": "Base/compute.googleapis.com/UrlMap",
          "labels": [
            "Base/Resource",
            "Base/compute.googleapis.com/UrlMap"
          ],
          "description": "Represents a Compute UrlMap."
        }
      ],
      "edgeTypes": [
        {
          "type": "Observability/SENDS_TRAFFIC/Base/geminidataanalytics.googleapis.com/DataAgent:Base/apps.k8s.io/DaemonSet",
          "labels": [
            "Observability/SENDS_TRAFFIC"
          ]
        }
      ],
      "labelProperties": [
        {
          "label": "Base/compute.googleapis.com/InstanceSettings",
          "description": "Classifies a node as a Compute Instance Settings."
        }
      ],
      "edgeRules": [
        {
          "edgeType": "Observability/SENDS_TRAFFIC/Base/geminidataanalytics.googleapis.com/DataAgent:Base/apps.k8s.io/DaemonSet",
          "srcNodeType": "Base/geminidataanalytics.googleapis.com/DataAgent",
          "destNodeType": "Base/apps.k8s.io/DaemonSet"
        }
      ]
    }
    

### REST

Get full schema

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your project ID
  * DOMAIN: The domain that you want to query. The `SRE` domain includes all supported data.



HTTP method and URL: 
    
    
    GET https://apptopology.googleapis.com/v1/projects/PROJECT_ID/locations/global/domains/DOMAIN/schema

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://apptopology.googleapis.com/v1/projects/PROJECT_ID/locations/global/domains/DOMAIN/schema"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://apptopology.googleapis.com/v1/projects/PROJECT_ID/locations/global/domains/DOMAIN/schema" | Select-Object -Expand Content

The following example excerpt from a response only includes the first item in the schema for node types, edge types, edge rules, and label properties.
    
    
    {
      "nodeTypes": [
        {
          "type": "Base/compute.googleapis.com/UrlMap",
          "labels": [
            "Base/Resource",
            "Base/compute.googleapis.com/UrlMap"
          ],
          "description": "Represents a Compute UrlMap."
        }
      ],
      "edgeTypes": [
        {
          "type": "Observability/SENDS_TRAFFIC/Base/geminidataanalytics.googleapis.com/DataAgent:Base/apps.k8s.io/DaemonSet",
          "labels": [
            "Observability/SENDS_TRAFFIC"
          ]
        }
      ],
      "labelProperties": [
        {
          "label": "Base/compute.googleapis.com/InstanceSettings",
          "description": "Classifies a node as a Compute Instance Settings."
        }
      ],
      "edgeRules": [
        {
          "edgeType": "Observability/SENDS_TRAFFIC/Base/geminidataanalytics.googleapis.com/DataAgent:Base/apps.k8s.io/DaemonSet",
          "srcNodeType": "Base/geminidataanalytics.googleapis.com/DataAgent",
          "destNodeType": "Base/apps.k8s.io/DaemonSet"
        }
      ]
    }
    

### Get a partial schema

You can get a portion of a domain schema within a specified number of hops of a specified starting label.

The example command in these instructions gets a portion of the schema starting at the `Base/Agent` node, with a depth of `1` and a page size of `5`.

Get partial schema

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your project ID
  * DOMAIN: The domain that you want to query. The `SRE` domain includes all supported data.



HTTP method and URL: 
    
    
    POST https://apptopology.googleapis.com/v1/projects/PROJECT_ID/locations/global/domains/DOMAIN/schema:explore

Request JSON body: 
    
    
    {
      "startLabels": [
        "Base/Agent"
      ],
      "depth": 1,
      "pageSize": 5
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "startLabels": [
        "Base/Agent"
      ],
      "depth": 1,
      "pageSize": 5
    }EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://apptopology.googleapis.com/v1/projects/PROJECT_ID/locations/global/domains/DOMAIN/schema:explore"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "startLabels": [
        "Base/Agent"
      ],
      "depth": 1,
      "pageSize": 5
    }'@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://apptopology.googleapis.com/v1/projects/PROJECT_ID/locations/global/domains/DOMAIN/schema:explore" | Select-Object -Expand Content

In a response, the order of `nodeTypes` and `edgeTypes` is consistent, but the order of `labelProperties` can vary from request to request.

Expand the **Response** heading to view an example response.

#### Response
    
    
    {
      "nodeTypes": [
        {
          "type": "Base/aiplatform.googleapis.com/Agent",
          "labels": [
            "Base/Resource",
            "Base/aiplatform.googleapis.com/Agent"
          ],
          "description": "Represents an Agents API Agent.",
          "optionalLabels": [
            "Base/Agent"
          ]
        },
        {
          "type": "Base/agentregistry.googleapis.com/Binding",
          "labels": [
            "Base/Resource",
            "Base/agentregistry.googleapis.com/Binding"
          ],
          "description": "Represents an Agent Registry Binding."
        },
        {
          "type": "Base/agentregistry.googleapis.com/Service",
          "labels": [
            "Base/Resource",
            "Base/agentregistry.googleapis.com/Service"
          ],
          "description": "Represents a Agent Registry Service.",
          "optionalLabels": [
            "Base/DiscoveredService",
            "Base/Endpoint",
            "Base/MCPServer",
            "Base/Agent"
          ]
        }
      ],
      "edgeTypes": [
        {
          "type": "Base/REVERSED:agentregistry.googleapis.com/Binding:source.identifier.agent:aiplatform.googleapis.com/Agent",
          "labels": [
            "DEPENDS_ON"
          ]
        },
        {
          "type": "Base/REVERSED:agentregistry.googleapis.com/Binding:source.identifier.agentregistry_service:agentregistry.googleapis.com/Service",
          "labels": [
            "DEPENDS_ON"
          ]
        }
      ],
      "labelProperties": [
        {
          "label": "Base/agentregistry.googleapis.com/Service",
          "description": "Classifies a node as a Agent Registry Service."
        },
        {
          "label": "Base/DiscoveredService",
          "properties": [
            {
              "name": "Base/app/names",
              "stringValue": {
                "repeated": true
              },
              "description": "The full name of the application."
            }
          ],
          "description": "Represents a discovered service from AppHub."
        },
        {
          "label": "Base/Agent",
          "properties": [
            {
              "name": "Base/agentregistry/urn",
              "stringValue": {},
              "description": "Canonical Logical URN of the agent, mcp server or endpoint, generated by the Agent Registry."
            },
            {
              "name": "Base/agent/identity",
              "stringValue": {},
              "description": "Cryptographically verifiable SPIFFE ID of the agent."
            },
            {
              "name": "Base/agent/provenance",
              "stringValue": {},
              "description": "Classification of the agent (e.g. 1P, 2P, 3P)."
            },
            {
              "name": "Base/agent/framework",
              "stringValue": {},
              "description": "The agent framework used (e.g. ADK, LangChain)."
            }
          ],
          "description": "Represents an agent."
        },
        {
          "label": "Base/agentregistry.googleapis.com/Binding",
          "description": "Classifies a node as an Agent Registry Binding."
        },
        {
          "label": "Base/Endpoint",
          "properties": [
            {
              "name": "Base/agentregistry/urn",
              "stringValue": {},
              "description": "Canonical Logical URN of the agent, mcp server or endpoint, generated by the Agent Registry."
            },
            {
              "name": "Base/endpoint/urls",
              "stringValue": {
                "repeated": true
              },
              "description": "List of destination URLs for the endpoint."
            },
            {
              "name": "Base/endpoint/protocolBindings",
              "stringValue": {
                "repeated": true
              },
              "description": "List of protocol bindings for the endpoint interfaces (e.g. JSONRPC, GRPC, HTTP_JSON)."
            }
          ],
          "description": "Represents an endpoint."
        },
        {
          "label": "Base/MCPServer",
          "properties": [
            {
              "name": "Base/agentregistry/urn",
              "stringValue": {},
              "description": "Canonical Logical URN of the agent, mcp server or endpoint, generated by the Agent Registry."
            }
          ],
          "description": "Represents a MCP Server."
        },
        {
          "label": "DEPENDS_ON",
          "description": "Signifies operational necessity. The source has an active functional dependency on the destination that enables the source to run or perform its primary function."
        },
        {
          "label": "Base/Resource",
          "properties": [
            {
              "name": "project",
              "stringValue": {},
              "description": "Project number in the format projects/{project_number}."
            },
            {
              "name": "folders",
              "stringValue": {
                "repeated": true
              },
              "description": "List of folder IDs in the format folders/{folder_id}."
            },
            {
              "name": "organization",
              "stringValue": {},
              "description": "Organization Id in the format organizations/{organization_id}."
            },
            {
              "name": "Base/resourceType",
              "stringValue": {},
              "description": "Type of the resource in the format of service.googleapis.com/ResourceType."
            },
            {
              "name": "Base/location",
              "stringValue": {},
              "description": "Location of the resource."
            },
            {
              "name": "Base/displayName",
              "stringValue": {},
              "description": "Display name of the resource."
            }
          ],
          "description": "Represents a GCP resource."
        },
        {
          "label": "Base/aiplatform.googleapis.com/Agent",
          "description": "Classifies a node as an Agents API Agent."
        }
      ],
      "edgeRules": [
        {
          "edgeType": "Base/REVERSED:agentregistry.googleapis.com/Binding:source.identifier.agent:aiplatform.googleapis.com/Agent",
          "srcNodeType": "Base/aiplatform.googleapis.com/Agent",
          "destNodeType": "Base/agentregistry.googleapis.com/Binding"
        },
        {
          "edgeType": "Base/REVERSED:agentregistry.googleapis.com/Binding:source.identifier.agentregistry_service:agentregistry.googleapis.com/Service",
          "srcNodeType": "Base/agentregistry.googleapis.com/Service",
          "destNodeType": "Base/agentregistry.googleapis.com/Binding"
        }
      ],
      "nextPageToken": "CAIQ6_LBy4mN1ox5GP_s5PGS1ZGY-wE"
    }
    

## Run queries

When you run a query, you specify a query pattern that includes the nodes, edges, and properties that you want to search for.

Query patterns are based on the [AIP-160](https://google.aip.dev/160) filtering syntax. For an overview of query patterns and query limitations, see [About queries](https://docs.cloud.google.com/app-topology/about-queries). These instructions assume that you have read the query structure and limitation information.

The following instructions use an example query for all App Hub services and workloads in the specified project, including those that are registered (`Base/apphub.googleapis.com/Service`, `Base/apphub.googleapis.com/Workload`) and those that are discovered (`Base/DiscoveredService`, `Base/DiscoveredWorkload`). 

The commands specify the query pattern in a JSON file. The file is slightly different for gcloud CLI and REST requests in these instructions.

  * For gcloud CLI, specify the domain to query as a parameter of the command. The domain isn't included in the query pattern file.
  * For REST requests, specify both the domain and the query pattern in the JSON body of the request. Set the domain in the `topologyDomains` field and specify the query pattern under the `filter` object.



### gcloud

Generate topology

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: Your project ID
  * DOMAIN: The domain that you want to query. The `SRE` domain includes all supported data.



Save the following content in a file called `request.json`: 
    
    
    {
      "startingNode": {
        "alias": "sw",
        "labelPropertiesPattern": {
          "labelMatcherExpr": "Base/apphub.googleapis.com/Service OR Base/apphub.googleapis.com/Workload OR Base/DiscoveredService OR Base/DiscoveredWorkload"
        }
      }
    }

Execute the [gcloud app-topology resources-graph generate](https://docs.cloud.google.com/sdk/gcloud/reference/app-topology/resources-graph/generate) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud app-topology resources-graph generate --domains=DOMAIN --project=PROJECT_ID --pattern-file=request.json --format=json

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud app-topology resources-graph generate --domains=DOMAIN --project=PROJECT_ID --pattern-file=request.json --format=json

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud app-topology resources-graph generate --domains=DOMAIN --project=PROJECT_ID --pattern-file=request.json --format=json

The following example response excerpt shows the first 2 nodes. These nodes are MCP servers. Google MCP servers have the label `Base/DiscoveredService`, which is one of the labels in the query pattern. 

In the output, the following variables represent values associated with the project you specified with `PROJECT_ID`:

  * `PROJECT_NUMBER` \- The project number for the specified project.
  * `ORGANIZATION_NUMBER` \- The organization number for the Google Cloud organization that contains the specified project.


    
    
    {
      "graph": {
        "nodes": [
          {
            "properties": {
              "project": "projects/PROJECT_NUMBER",
              "Base/location": "global",
              "createTime": "2026-08-13T15:14:53.477680Z",
              "Base/agentregistry/urn": "urn:mcp:googleapis.com:projects:PROJECT_NUMBER:locations:global:storage",
              "Base/resourceType": "agentregistry.googleapis.com/GoogleMcpServer",
              "organization": "organizations/ORGANIZATION_NUMBER"
            },
            "name": "urn:mcp:googleapis.com:projects:PROJECT_NUMBER:locations:global:storage",
            "labels": [
              "Base/MCPServer",
              "Base/DiscoveredService",
              "Base/Resource",
              "Base/agentregistry.googleapis.com/GoogleMcpServer"
            ],
            "context": {
              "type": "Base/agentregistry.googleapis.com/GoogleMcpServer"
            }
          },
          {
            "properties": {
              "createTime": "2026-08-13T16:22:24.732600Z",
              "Base/resourceType": "agentregistry.googleapis.com/GoogleMcpServer",
              "Base/agentregistry/urn": "urn:mcp:googleapis.com:projects:PROJECT_NUMBER:locations:global:pubsub",
              "Base/location": "global",
              "organization": "organizations/ORGANIZATION_NUMBER",
              "project": "projects/PROJECT_NUMBER"
            },
            "name": "urn:mcp:googleapis.com:projects:PROJECT_NUMBER:locations:global:pubsub",
            "labels": [
              "Base/agentregistry.googleapis.com/GoogleMcpServer",
              "Base/Resource",
              "Base/DiscoveredService",
              "Base/MCPServer"
            ],
            "context": {
              "type": "Base/agentregistry.googleapis.com/GoogleMcpServer"
            }
          }
        ]
      }
    }
    

### REST

Generate topology

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your project ID
  * DOMAIN: The domain that you want to query. The `SRE` domain includes all supported data.



HTTP method and URL: 
    
    
    POST https://apptopology.googleapis.com/v1/projects/PROJECT_ID/locations/global/discoveredResourcesTopology:generate

Request JSON body: 
    
    
    {
      "topologyDomains": [
        "projects/PROJECT_ID/locations/global/domains/DOMAIN"
      ],
      "filter": {
        "startingNode": {
          "alias": "sw",
          "labelPropertiesPattern": {
            "labelMatcherExpr": "Base/apphub.googleapis.com/Service OR Base/apphub.googleapis.com/Workload OR Base/DiscoveredService OR Base/DiscoveredWorkload"
          }
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "topologyDomains": [
        "projects/PROJECT_ID/locations/global/domains/DOMAIN"
      ],
      "filter": {
        "startingNode": {
          "alias": "sw",
          "labelPropertiesPattern": {
            "labelMatcherExpr": "Base/apphub.googleapis.com/Service OR Base/apphub.googleapis.com/Workload OR Base/DiscoveredService OR Base/DiscoveredWorkload"
          }
        }
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://apptopology.googleapis.com/v1/projects/PROJECT_ID/locations/global/discoveredResourcesTopology:generate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "topologyDomains": [
        "projects/PROJECT_ID/locations/global/domains/DOMAIN"
      ],
      "filter": {
        "startingNode": {
          "alias": "sw",
          "labelPropertiesPattern": {
            "labelMatcherExpr": "Base/apphub.googleapis.com/Service OR Base/apphub.googleapis.com/Workload OR Base/DiscoveredService OR Base/DiscoveredWorkload"
          }
        }
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://apptopology.googleapis.com/v1/projects/PROJECT_ID/locations/global/discoveredResourcesTopology:generate" | Select-Object -Expand Content

The following example response excerpt shows the first 2 nodes. These nodes are MCP servers. Google MCP servers have the label `Base/DiscoveredService`, which is one of the labels in the query pattern. 

In the output, the following variables represent values associated with the project you specified with `PROJECT_ID`:

  * `PROJECT_NUMBER` \- The project number for the specified project.
  * `ORGANIZATION_NUMBER` \- The organization number for the Google Cloud organization that contains the specified project.


    
    
    {
      "graph": {
        "nodes": [
          {
            "properties": {
              "project": "projects/PROJECT_NUMBER",
              "Base/location": "global",
              "createTime": "2026-08-13T15:14:53.477680Z",
              "Base/agentregistry/urn": "urn:mcp:googleapis.com:projects:PROJECT_NUMBER:locations:global:storage",
              "Base/resourceType": "agentregistry.googleapis.com/GoogleMcpServer",
              "organization": "organizations/ORGANIZATION_NUMBER"
            },
            "name": "urn:mcp:googleapis.com:projects:PROJECT_NUMBER:locations:global:storage",
            "labels": [
              "Base/MCPServer",
              "Base/DiscoveredService",
              "Base/Resource",
              "Base/agentregistry.googleapis.com/GoogleMcpServer"
            ],
            "context": {
              "type": "Base/agentregistry.googleapis.com/GoogleMcpServer"
            }
          },
          {
            "properties": {
              "createTime": "2026-08-13T16:22:24.732600Z",
              "Base/resourceType": "agentregistry.googleapis.com/GoogleMcpServer",
              "Base/agentregistry/urn": "urn:mcp:googleapis.com:projects:PROJECT_NUMBER:locations:global:pubsub",
              "Base/location": "global",
              "organization": "organizations/ORGANIZATION_NUMBER",
              "project": "projects/PROJECT_NUMBER"
            },
            "name": "urn:mcp:googleapis.com:projects:PROJECT_NUMBER:locations:global:pubsub",
            "labels": [
              "Base/agentregistry.googleapis.com/GoogleMcpServer",
              "Base/Resource",
              "Base/DiscoveredService",
              "Base/MCPServer"
            ],
            "context": {
              "type": "Base/agentregistry.googleapis.com/GoogleMcpServer"
            }
          }
        ]
      }
    }
    

For additional query pattern examples, see Example query patterns.

## Example query patterns

Use the following query pattern examples to help you build your own query patterns for running queries. All examples in this section use the JSON format.

### VMs with instance groups, networks, and disks

Query for Compute Engine instances in an instance group with networking and disk.

The pattern starts at `Base/compute.googleapis.com/Instance` and has three primary `edge` branches under the top level `neighbors` object that define these criteria:

  * Instances that belong to a managed instance group
  * Instances with a connected network
  * Instances with Persistent Disk



Because branches are combined with `AND`, the response only includes instances that belong to a managed instance group and have both a network and a disk.
    
    
    {
      "startingNode": {
        "alias": "instance",
        "labelPropertiesPattern": {
          "labelMatcherExpr": "Base/compute.googleapis.com/Instance"
        }
      },
      "neighbors": [
        {
          "edge": {
            "direction": "FROM",
            "labelPropertiesPattern": {
              "labelMatcherExpr": "CONTAINS"
            }
          },
          "graph": {
            "startingNode": {
              "alias": "instance_group",
              "labelPropertiesPattern": {
                "labelMatcherExpr": "Base/compute.googleapis.com/InstanceGroup"
              }
            },
            "neighbors": [
              {
                "edge": {
                  "direction": "FROM",
                  "labelPropertiesPattern": {
                    "labelMatcherExpr": "DEPENDS_ON"
                  }
                },
                "graph": {
                  "startingNode": {
                    "alias": "instance_group_manager",
                    "labelPropertiesPattern": {
                      "labelMatcherExpr": "Base/compute.googleapis.com/InstanceGroupManager"
                    }
                  }
                }
              }
            ]
          }
        },
        {
          "edge": {
            "direction": "TO",
            "labelPropertiesPattern": {
              "labelMatcherExpr": "DEPENDS_ON"
            }
          },
          "graph": {
            "startingNode": {
              "alias": "network",
              "labelPropertiesPattern": {
                "labelMatcherExpr": "Base/compute.googleapis.com/Network"
              }
            }
          }
        },
        {
          "edge": {
            "direction": "TO",
            "labelPropertiesPattern": {
              "labelMatcherExpr": "DEPENDS_ON"
            }
          },
          "graph": {
            "startingNode": {
              "alias": "disk",
              "labelPropertiesPattern": {
                "labelMatcherExpr": "Base/compute.googleapis.com/Disk"
              }
            }
          }
        }
      ]
    }
    

### Agentic resources

Query for agentic resources and their relationships using information from Agent Registry, including data for agents, MCP servers, endpoints, and skills.
    
    
    {
      "startingNode": {
        "alias": "resource",
        "labelPropertiesPattern": {
          "labelMatcherExpr": "Base/Agent OR Base/MCPServer OR Base/agentregistry.googleapis.com/Skill OR Base/agentregistry.googleapis.com/SkillRevision OR Base/agentregistry.googleapis.com/AiApplication OR Base/agentregistry.googleapis.com/GoogleMcpServer OR Base/agentregistry.googleapis.com/McpEnablement OR Base/agentregistry.googleapis.com/Publisher OR Base/agentregistry.googleapis.com/Binding OR Base/agentregistry.googleapis.com/Service OR Base/aiplatform.googleapis.com/Endpoint"
        }
      }
    }
    

App Topology supports two types of endpoints:

  * `Base/aiplatform.googleapis.com/Endpoint` is a Gemini Enterprise Agent Platform [model endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/choose-endpoint-type).
  * `Base/Endpoint` is the [target URL for an agent](https://docs.cloud.google.com/agent-registry/register-endpoints), and is a label on an Agent Registry service (`Base/agentregistry.googleapis.com/Service`). Since `Base/agentregistry.googleapis.com/Service` is included in the query pattern, agent endpoints are included in the query response results.



### Agent traffic

Query for traffic between agents and other agents or MCP servers using data from Cloud Trace. Each edge includes error rate and p95 latency data.
    
    
    {
      "startingNode": {
        "alias": "agent",
        "labelPropertiesPattern": {
          "labelMatcherExpr": "Base/Agent"
        }
      },
      "neighbors": [
        {
          "edge": {
            "direction": "ANY",
            "labelPropertiesPattern": {
              "labelMatcherExpr": "Observability/SENDS_TRAFFIC"
            }
          },
          "graph": {
            "startingNode": {
              "alias": "peer",
              "labelPropertiesPattern": {
                "labelMatcherExpr": "Base/Agent OR Base/MCPServer"
              }
            }
          }
        }
      ]
    }
    

## What's next

  * Learn about using the [remote MCP server](https://docs.cloud.google.com/app-topology/use-apptopology-mcp).
  * Learn about running queries in [Cloud Hub](https://docs.cloud.google.com/hub/docs/app-topology/run-queries).
  * Learn about running queries in [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
