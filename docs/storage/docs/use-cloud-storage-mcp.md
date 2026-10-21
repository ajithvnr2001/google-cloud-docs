---
url: https://docs.cloud.google.com/storage/docs/use-cloud-storage-mcp/
title: Use the Cloud Storage MCP server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:32.896698+00:00
---

# Use the Cloud Storage MCP server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/use-cloud-storage-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use the Cloud Storage MCP server Stay organized with collections  Save and categorize content based on your preferences. 

[Model Context Protocol](https://cloud.google.com/discover/what-is-model-context-protocol) (MCP) standardizes the way large language models (LLMs) and AI applications or agents connect to outside data sources. MCP servers let you use their tools, resources, and prompts to take actions and get updated data from their backend service.

Local MCP servers typically run on your local machine and use the standard input and output streams (stdio) for communication between services on the same device. While local MCP servers often communicate with local services, they can also be used to call services or data sources that are not running on the local machine. For example, a local MCP server running on an agent's machine or virtual machine can call Cloud Storage APIs.

You might use the Cloud Storage local MCP server for the following reasons:

  * You need to build a custom tool.
  * You don't have permissions to enable or use the MCP server in your project.



To learn how to use the local MCP server, see [Connect LLMs to Cloud Storage with MCP](https://docs.cloud.google.com/storage/docs/pre-built-tools-with-mcp-toolbox).

Remote MCP servers run on the service's infrastructure and offer an HTTP endpoint to AI applications for communication between the AI MCP client and the MCP server. The Cloud Storage MCP server is a remote MCP server with an HTTP endpoint. For more information about MCP architecture, see [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture).

This document describes how to use the Cloud Storage MCP server to connect to Cloud Storage from AI applications such as Gemini CLI, agent mode in Gemini Code Assist, Claude Code, or in AI applications that you're developing.

With the Cloud Storage MCP server, you can use AI applications and agents to perform the following tasks:

  * Create and delete buckets.
  * Retrieve object metadata.
  * Read and delete object data, and write text content.
  * List buckets and objects.

The Cloud Storage remote MCP server is enabled when you enable the Cloud Storage API. To disable the Cloud Storage MCP server, you must disable the Cloud Storage API. For information about how to disable the Cloud Storage API, see [Disable a service](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling). 

## Google and Google Cloud remote MCP servers

Google and Google Cloud remote MCP servers have the following features and benefits: 

  * Simplified, centralized discovery
  * Managed global or regional HTTP endpoints
  * Fine-grained authorization
  * Optional prompt and response security with Model Armor protection
  * Centralized audit logging



For information about other MCP servers and information about security and governance controls available for Google Cloud MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).

## Limitations

The Cloud Storage MCP server has the following limitations:

  * **File types** : read operations support text and binary files (such as PDFs, images, audios, and videos); write operations are restricted to text files.

  * **File size** : maximum of 8 MiB for read and write operations.

  * **Endpoint** : global endpoint only.




For detailed information on quotas and limits that apply to the Cloud Storage MCP server, see [Quotas and limits](https://docs.cloud.google.com/storage/quotas#gcs-mcp).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Required roles

To get the permissions that you need to use the Cloud Storage MCP server, ask your administrator to grant you the following IAM roles on the project where you want to use the Cloud Storage MCP server: 

  * Make MCP tool calls: [MCP Tool User ](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) (`roles/mcp.toolUser`) 
  * List objects, read objects and their contents, or get an object's metadata: [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) 
  * Write content to an object: [Storage Object Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`) 
  * Delete objects: Storage Object User (`roles/storage.objectUser`) or Storage Object Admin (`roles/storage.objectAdmin`) 
  * Create, list, or delete buckets: [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the Cloud Storage MCP server. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the Cloud Storage MCP server:

  * Make MCP tool calls: `mcp.tools.call`
  * List objects: `storage.objects.list`
  * Read objects and their contents or get an object's metadata: `storage.objects.get`
  * Write content to an object: `storage.objects.create`
  * Delete objects: `storage.objects.delete`
  * List buckets: `storage.buckets.list`
  * Create buckets: `storage.buckets.create`
  * Delete buckets: `storage.buckets.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Authentication and authorization

The Cloud Storage remote MCP server uses the [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) protocol with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) for authentication and authorization. All [Google Cloud identities](https://docs.cloud.google.com/docs/authentication/identity-products) are supported for authentication to MCP servers. 

The Cloud Storage MCP server doesn't accept API keys for authentication because all requests require Identity and Access Management (IAM) authorization.

We recommend that you create a separate identity for agents that are using MCP tools so that access to resources can be controlled and monitored. For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).

## Cloud Storage MCP OAuth scopes

OAuth 2.0 uses scopes and credentials to determine if an authenticated principal is authorized to take a specific action on a resource. For more information about OAuth 2.0 scopes at Google, read [Using OAuth 2.0 to access Google APIs](https://developers.google.com/identity/protocols/oauth2).

Cloud Storage has the following MCP tool OAuth scopes:

Scope URI for gcloud CLI | Description  
---|---  
`https://www.googleapis.com/auth/devstorage.read_only` | Only allows access to read data.  
`https://www.googleapis.com/auth/devstorage.read_write` | Allows access to read and modify data.  
  
Additional scopes might be required on the resources accessed during a tool call. To view a list of scopes required for Cloud Storage, see [Cloud Storage API](https://developers.google.com/identity/protocols/oauth2/scopes#storage). If your agent interacts with other Google Cloud services as part of its workflow, such as BigQuery or Storage Insights, it requires the appropriate OAuth scopes for those services in addition to the Cloud Storage scopes.

## Configure an MCP client to use the Cloud Storage MCP server

AI applications and agents, such as Claude or Antigravity, can instantiate an MCP client that connects to a single MCP server. An AI application can have multiple clients that connect to different MCP servers. If your application isn't listed in the [client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance), then you can use the following information to connect from most applications.

In your AI application, look for a way to add or connect to a remote MCP server. For the Cloud Storage MCP server, enter the following information as required:

  * **Server name** : Cloud Storage MCP server
  * **Server URL** or **Endpoint** : `https://storage.googleapis.com/storage/mcp`
  * **Transport** : [Streamable HTTP](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http)
  * **Authentication details** : depending on how you want to authenticate, you can enter your Google Cloud credentials, your OAuth Client ID and secret, or an agent identity and credentials. For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).
  * **OAuth scope** : one of the scopes listed in this document that you want to use when connecting to the Cloud Storage MCP server.



For application-specific guidance about setting up and connecting to MCP server, see [Client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance).

For more general guidance, see the following resources:

  * [Connect to remote MCP servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers).
  * [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).



## Available tools

To view details of available MCP tools and their descriptions for the Cloud Storage MCP server, see the [Cloud Storage MCP reference](https://docs.cloud.google.com/storage/docs/reference/mcp). For schemas and examples, see the [Cloud Storage MCP GitHub repository](https://github.com/googleapis/gcloud-mcp/tree/main/packages/storage-mcp).

### List tools

Use the [MCP inspector](https://modelcontextprotocol.io/docs/tools/inspector) to list tools, or send a `tools/list` HTTP request directly to the Cloud Storage remote MCP server. The `tools/list` method doesn't require authentication.
    
    
    curl -X POST https://storage.googleapis.com/TOOLSET_ENDPOINT \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
        -H 'MCP-Protocol-Version: MCP_PROTOCOL_VERSION' \
        -H 'Mcp-Method: tools/list' \
        -d '{
          "jsonrpc": "2.0",
          "id": 1,
          "method": "tools/list",
          "params": {
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
        }'
    

Replace the following:

  * `TOOLSET_ENDPOINT`: the remainder of the MCP endpoint after the service name. For example, for Cloud Storage, this might be `mcp/toolset-name`.
  * `MCP_PROTOCOL_VERSION`: the MCP protocol version. For example, `2026-07-28`.



### Call a tool

To call a specific tool, use the `tools/call` method and provide the tool name and necessary arguments in the `params` object. The following example shows how to call the `list_buckets` tool for the project `my-project`:
    
    
    POST /storage/mcp HTTP/1.1
    Host: storage.googleapis.com
    Content-Type: application/json
    Authorization: Bearer OAUTH2_TOKEN
    
    {
      "jsonrpc": "2.0",
      "method": "tools/call",
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "params": {
        "name": "list_buckets",
        "arguments": {
          "projectId": "my-project"
        }
      }
    }
    

## Example use cases

The following are example use cases for the Cloud Storage MCP server.

### Manage retail content and campaigns

A sample use case for the Cloud Storage MCP server is to assist a retailer's marketing agent to create and manage product listings and promotional campaigns. The Cloud Storage MCP server lets you list, read, and write objects, and create buckets for storing product and campaign assets by using natural language.

**Sample prompt** :

"Create a product listing for SKU-123 using assets from the product-images bucket, then create a new bucket called campaign-q3-assets and generate and save banner images into it."

**Workflow** : The workflow for creating product listings and campaigns might look like the following:

  * **List assets** : the agent uses `list_objects` to find all images for the new product in a dedicated Cloud Storage bucket.
  * **Fetch content** : the agent uses `read_object` to access product assets (up to 8 MiB in size), and also fetches product descriptions from a product information management (PIM) system using another tool.
  * **Generate listing** : the agent generates a draft of the product listing, including marketing copy and links to the images and videos.
  * **Create campaign bucket** : the agent uses `create_bucket` to create a new bucket for campaign assets.
  * **Save campaign assets** : the agent generates promotional copy and uses `write_text` to save it into the new "campaigns" bucket. The copy must be less than 8 MiB in size.



### Analyze financial data

A sample use case for the Cloud Storage MCP server is to help portfolio managers gain insights from financial reports and audio recordings of trader calls with clients. The Cloud Storage MCP server helps the agent to identify and download relevant documents and pass them to an LLM for analysis.

**Sample prompt** :

"What were the key takeaways from ExampleCorp's most recent earnings call, and how does that compare to the sentiment in their last three financial reports?"

**Workflow** : The workflow for analyzing financial documents might look like the following:

  * **Identify documents** : the agent extracts keywords from the user's question to identify relevant buckets or prefixes, for example, `earnings-calls/ExampleCorp/` or `financial-reports/ExampleCorp/` and uses `list_objects` to find relevant audio transcripts and financial reports.
  * **Download content** : the agent uses `read_object` to download the content of the identified files, up to 8 MiB per file.
  * **Analyze and respond** : the agent passes the content to an LLM to summarize findings, compare sentiment, and synthesize an answer to the user's question. If needed, other tools like BigQuery can be used for deeper analysis.



### Assess vendor risk

A sample use case for the Cloud Storage MCP server is to help automate the initial vendor risk assessment process for a bank's risk management team. The Cloud Storage MCP server lets the AI agent fetch and analyze documents that vendors submit to identify potential risks by using natural language.

**Sample prompt** :

"Assess vendor "Example Inc." by reviewing their latest security questionnaire and compliance certificate in the `vendor-docs` bucket. Summarize any potential risks based on our policies and save the report."

**Workflow** : The workflow for assessing vendor risk might look like the following:

  * **Find documents** : the agent uses the `list_objects` tool to find the vendor's folder in a Cloud Storage bucket dedicated to vendor documents.
  * **Download documents** : the agent uses `read_object` to download all relevant documents, such as security questionnaires, compliance certificates, and financial statements, up to 8 MiB per file.
  * **Analyze documents** : the agent analyzes the content of these documents, possibly using other tools to extract text, to look for red flags or missing information based on the bank's risk policies.
  * **Compile and save report** : the agent compiles a summary report of its findings and uses `write_text` to save it to the vendor's folder in Cloud Storage for the risk assessor to review.



## Optional security and safety configurations

MCP introduces new security risks and considerations due to the wide variety of actions that you can do with the MCP tools. To minimize and manage these risks, Google Cloud offers default settings and customizable policies to control the use of MCP tools in your Google Cloud organization or project.

For more information about MCP security and governance, see [AI security and safety](https://docs.cloud.google.com/mcp/ai-security-safety).

### Use Model Armor

[Model Armor](https://docs.cloud.google.com/model-armor/overview) is a Google Cloud service designed to enhance the security and safety of your AI applications. It works by proactively screening LLM prompts and responses, protecting against various risks and supporting responsible AI practices. Whether you are deploying AI in your cloud environment, or on external cloud providers, Model Armor can help you prevent malicious input, verify content safety, protect sensitive data, maintain compliance, and enforce your AI safety and security policies consistently across your diverse AI landscape.

When Model Armor is enabled with [logging enabled](https://docs.cloud.google.com/model-armor/configure-logging), Model Armor logs the entire payload. This might expose sensitive information in your logs.

#### MCP request routing to Model Armor

Model Armor is available in [certain regions](https://docs.cloud.google.com/model-armor/locations). When Model Armor is enabled and you use an MCP server in a jurisdiction that Model Armor doesn't support, the routing behavior of the call might be different for different MCP servers and might break data residency compliance for in-use and in-transit data. For more information about the behavior of individual MCP servers, see [Model Armor supported products](https://docs.cloud.google.com/mcp/model-armor-supported-products). 

#### Enable Model Armor

You must enable Model Armor APIs before you can use Model Armor.

###  Console 

  1. Enable the Model Armor API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=modelarmor.googleapis.com)

  2. Select the project where you want to activate Model Armor.




###  gcloud 

Before you begin, follow these steps using the Google Cloud CLI with the Model Armor API:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the following command to set the API endpoint for the Model Armor service.
         
         gcloud config set api_endpoint_overrides/modelarmor "https://modelarmor.LOCATION.rep.googleapis.com/"

Replace `LOCATION` with the region where you want to use Model Armor.




#### Configure protection for Google and Google Cloud remote MCP servers

To help protect your MCP tool calls and responses you can use Model Armor floor settings. A floor setting defines the minimum security filters that apply across the project. This configuration applies a consistent set of filters to all MCP tool calls and responses within the project.

**Tip:** Don't enable the prompt injection and jailbreak filter unless your MCP traffic carries natural language data.

Set up a Model Armor floor setting with MCP sanitization enabled. For more information, see [Configure Model Armor floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings).

**Note:** If the agent and the MCP server are in different projects, you can create floor settings in both projects (the client project and the resource project). In this case, Model Armor is invoked twice, once for each project.

See the following example command:
    
    
    gcloud model-armor floorsettings update \
    --full-uri='projects/PROJECT_ID/locations/global/floorSetting' \
    --enable-floor-setting-enforcement=TRUE \
    --add-integrated-services=GOOGLE_MCP_SERVER \
    --google-mcp-server-enforcement-type=INSPECT_AND_BLOCK \
    --enable-google-mcp-server-cloud-logging \
    --malicious-uri-filter-settings-enforcement=ENABLED \
    --add-rai-settings-filters='[{"confidenceLevel": "MEDIUM_AND_ABOVE", "filterType": "DANGEROUS"}]'

Replace `PROJECT_ID` with your Google Cloud project ID.

Note the following settings:

  * `INSPECT_AND_BLOCK`: The enforcement type that inspects content for the Google MCP server and blocks prompts and responses that match the filters.
  * `ENABLED`: The setting that enables a filter or enforcement.
  * `MEDIUM_AND_ABOVE`: The confidence level for the Responsible AI - Dangerous filter settings. You can modify this setting, though lower values might result in more false positives. For more information, see [Model Armor confidence levels](https://docs.cloud.google.com/model-armor/overview#ma-confidence-levels).



#### Disable scanning MCP traffic with Model Armor

To stop Model Armor from automatically scanning traffic to and from Google MCP servers based on the project's floor settings, run the following command:
    
    
    gcloud model-armor floorsettings update \
      --full-uri='projects/PROJECT_ID/locations/global/floorSetting' \
      --remove-integrated-services=GOOGLE_MCP_SERVER
    

Replace `PROJECT_ID` with the Google Cloud project ID. Model Armor doesn't automatically apply the rules defined in this project's floor settings to any Google MCP server traffic.

Model Armor floor settings and general configuration can impact more than just MCP. Because Model Armor integrates with services like Vertex AI, any changes you make to floor settings can affect traffic scanning and safety behaviors across all integrated services, not just MCP.

### Control MCP use with IAM policies

Identity and Access Management (IAM) [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) and [allow policies](https://docs.cloud.google.com/iam/docs/allow-policies) help you secure Google Cloud and Google MCP servers.

You can combine multiple criteria to build customized security and governance policies by allowing or denying access based on the following:

  * The principal.
  * Tool properties like the read-only attribute.
  * The service name or tool name.
  * The application's OAuth client ID.



For more information, see [Control MCP use with Identity and Access Management](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

## What's next

  * Read the [Cloud Storage MCP reference documentation](https://docs.cloud.google.com/storage/docs/reference/mcp).
  * Learn more about [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
