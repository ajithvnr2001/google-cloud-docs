---
url: https://docs.cloud.google.com/oracle/database/docs/use-oracledatabase-mcp/
title: Use the Oracle Database@Google Cloud remote MCP server \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:42.359682+00:00
---

# Use the Oracle Database@Google Cloud remote MCP server  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/use-oracledatabase-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Use the Oracle Database@Google Cloud remote MCP server Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows you how to use the Oracle Database@Google Cloud remote Model Context Protocol (MCP) server to connect with AI applications including Gemini CLI, ChatGPT, Claude, and custom applications you are developing. The Oracle Database@Google Cloud remote MCP server lets you access and run Oracle Database@Google Cloud tools to manage Oracle Database@Google Cloud resources from your AI-enabled development environments and AI agent platforms. The Oracle Database@Google Cloud remote MCP server is enabled when you enable the Oracle Database@Google Cloud API. 

[Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) standardizes how large language models (LLMs) and AI applications or agents connect to external data sources. MCP servers let you use their tools, resources, and prompts to take actions and get updated data from their backend service.

Remote MCP servers run on the service's infrastructure and offer an HTTP endpoint to AI applications for communication between the AI MCP client and the MCP server. For more information about MCP architecture, see [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture).

## Google and Google Cloud remote MCP servers

Google and Google Cloud remote MCP servers have the following features and benefits: 

  * Simplified, centralized discovery
  * Managed global or regional HTTP endpoints
  * Fine-grained authorization
  * Optional prompt and response security with Model Armor protection
  * Centralized audit logging



For information about other MCP servers and information about security and governance controls available for Google Cloud MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).

## Limitations

  * For Autonomous AI Databases and DB systems, the `create_autonomous_database` tool and `create_db_system` tool, respectively, support only secrets stored in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview). They don't support raw passwords.

  * While Secret Manager provides a secure storage mechanism, project administrators, users with the `secretmanager.versions.access` permission, or users with permissions to modify IAM policies (such as, `resourcemanager.projects.setIamPolicy`) can potentially access the secrets, even if IAM deny policies are in place.




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. Enable the Oracle Database@Google Cloud API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=oracledatabase.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  10. Enable the Oracle Database@Google Cloud API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=oracledatabase.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Required roles

**Note:** We recommend that you grant the roles that follow the principle of least privilege, which states that principals should have no more permissions than they actually need.

To get the permissions that you need to use the Oracle Database@Google Cloud MCP server, ask your administrator to grant you the following IAM roles on the project where you want to use the Oracle Database@Google Cloud MCP server: 

  * Make MCP tool calls: [MCP Tool User ](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) (`roles/mcp.toolUser`) 
  * Create an ODB Network and ODB Subnet: [ODB Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`) 
  * View ODB Networks and subnets details: 
    * [ODB Network Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkViewer) (`roles/oracledatabase.odbNetworkViewer`)
    * [ODB Subnet Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetViewer) (`roles/oracledatabase.odbSubnetViewer`)
  * Create an Exadata Infrastructure instance: [Exadata Infrastructure Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`) 
  * View Exadata Infrastructure instance details: [Exadata Infrastructure Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureViewer) (`roles/oracledatabase.cloudExadataInfrastructureViewer`) 
  * Create an Exadata VM Cluster: 
    * [VM Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)
    * [Exadata Infrastructure User ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)
  * View Exadata VM Cluster details: [VM Cluster Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterViewer) (`roles/oracledatabase.cloudVmClusterViewer`) 
  * Create an Exascale VM Cluster and Exascale Storage Vault: 
    * [Exascale Infrastructure VM Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)
    * [Exascale Infrastructure Storage Vault Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)
  * View Exascale VM Cluster details: [Exascale Infrastructure VM Cluster Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterViewer) (`roles/oracledatabase.exadbVmClusterViewer`) 
  * View Exascale Storage Vault details: [Exascale Infrastructure Storage Vault Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultViewer) (`roles/oracledatabase.exascaleDbStorageVaultViewer`) 
  * Create an Autonomous AI Database: [Autonomous Database Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`) 
  * View Autonomous AI Database details: [Autonomous Database Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`) 
  * Create a DB system: [DB System Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`) 
  * View DB system details: [DB System Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the Oracle Database@Google Cloud MCP server. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the Oracle Database@Google Cloud MCP server:

  * Make MCP tool calls: `mcp.tools.call`
  * ODB Network and ODB Subnet: 
    * `oracledatabase.odbNetworks.create`
    * `oracledatabase.odbSubnets.create`
    * `oracledatabase.odbNetworks.list`
    * `oracledatabase.odbNetworks.get`
  * Exadata Infrastructure instance: 
    * `oracledatabase.cloudExadataInfrastructures.create`
    * `oracledatabase.cloudExadataInfrastructures.list`
    * `oracledatabase.cloudExadataInfrastructures.get`
  * Exadata VM Cluster: 
    * `oracledatabase.cloudVmClusters.create`
    * `oracledatabase.cloudVmClusters.list`
    * `oracledatabase.cloudVmClusters.get`
  * Exascale VM Cluster: 
    * `oracledatabase.exadbVmClusters.create`
    * `oracledatabase.exadbVmClusters.list`
    * `oracledatabase.exadbVmClusters.get`
  * Exascale Storage Vault: 
    * `oracledatabase.exascaleDbStorageVaults.create`
    * `oracledatabase.exascaleDbStorageVaults.list`
    * `oracledatabase.exascaleDbStorageVaults.get`
  * Autonomous AI Database: 
    * `oracledatabase.autonomousDatabases.create`
    * `oracledatabase.autonomousDatabases.list`
    * `oracledatabase.autonomousDatabases.get`
  * DB system: 
    * `oracledatabase.dbSystems.create`
    * `oracledatabase.dbSystems.list`
    * `oracledatabase.dbSystems.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Authentication and authorization

The Oracle Database@Google Cloud remote MCP server uses the [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) protocol with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) for authentication and authorization. All [Google Cloud identities](https://docs.cloud.google.com/docs/authentication/identity-products) are supported for authentication to MCP servers. 

We recommend that you create a separate identity for agents that are using MCP tools so that access to resources can be controlled and monitored. For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).

## Oracle Database@Google Cloud MCP OAuth scopes

OAuth 2.0 uses scopes and credentials to determine if an authenticated principal is authorized to take a specific action on a resource. For more information about OAuth 2.0 scopes at Google, read [Using OAuth 2.0 to access Google APIs](https://developers.google.com/identity/protocols/oauth2).

Oracle Database@Google Cloud has the following MCP tool OAuth scopes:

Scope URI for gcloud CLI | Description  
---|---  
`https://www.googleapis.com/auth/oracle-database` | Create and list resources, and view information about the resources.  
  
Additional scopes might be required on the resources accessed during a tool call. To view a list of scopes required for Oracle Database@Google Cloud, see [Oracle Database@Google Cloud API](https://developers.google.com/identity/protocols/oauth2/scopes#oracledatabase).

## Configure an MCP client to use the Oracle Database@Google Cloud MCP server

AI applications and agents, such as Claude or Antigravity, can instantiate an MCP client that connects to a single MCP server. An AI application can have multiple clients that connect to different MCP servers. If your application isn't listed in the [client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance), then you can use the following information to connect from most applications.

In your AI application, look for a way to add or connect to a remote MCP server. For the Oracle Database@Google Cloud MCP server, enter the following information as required:

  * **Server name** : Oracle Database@Google Cloud MCP server
  * **Server URL** or **Endpoint** : `https://oracledatabase.googleapis.com/mcp`
  * **Transport** : [Streamable HTTP](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http)
  * **Authentication details** : depending on how you want to authenticate, you can enter your Google Cloud credentials, your OAuth Client ID and secret, or an agent identity and credentials. For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).
  * **OAuth scope** : the [OAuth 2.0 scope](https://developers.google.com/identity/protocols/oauth2/scopes) that you want to use when connecting to the Oracle Database@Google Cloud MCP server.



For application-specific guidance about setting up and connecting to MCP server, see [Client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance).

For more general guidance, see the following resources:

  * [Connect to remote MCP servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers).
  * [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).



## Available tools

To view details of available MCP tools and their descriptions for the Oracle Database@Google Cloud MCP server, see the [Oracle Database@Google Cloud MCP reference](https://docs.cloud.google.com/oracle/database/docs/reference/mcp).

### List tools

Use the [MCP inspector](https://modelcontextprotocol.io/docs/tools/inspector) to list tools, or send a `tools/list` HTTP request directly to the Oracle Database@Google Cloud remote MCP server. The `tools/list` method doesn't require authentication.
    
    
    curl -X POST https://oracledatabase.googleapis.com/TOOLSET_ENDPOINT \
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

  * `TOOLSET_ENDPOINT`: the remainder of the MCP endpoint after the service name. For example, for Oracle Database@Google Cloud, this might be `mcp/toolset-name`.
  * `MCP_PROTOCOL_VERSION`: the MCP protocol version. For example, `2026-07-28`.



## Sample prompts

You can use the following sample prompts to create and list Oracle Database@Google Cloud resources, and to get information about them:

  * "Create an ODB Subnet ODB_SUBNET_ID in project PROJECT_ID in zone ZONE_ID in ODB Network ODB_NETWORK_ID."
  * "List ODB Networks in project PROJECT_ID in region REGION_ID."
  * "Create a Exadata VM Cluster CLUSTER_ID in project PROJECT_ID in zone ZONE_ID."
  * "List Exadata VM Clusters in project PROJECT_ID in region REGION_ID."
  * "Get Exadata VM Cluster CLUSTER_ID in project PROJECT_ID in region REGION_ID."
  * "Create an Exascale VM Cluster CLUSTER_ID with ODB Subnet ODB_SUBNET_ID and vault VAULT_ID in project PROJECT_ID in zone ZONE_ID."
  * "Create a DB system DB_SYSTEM_ID in project PROJECT_ID in zone ZONE_ID."
  * "Create an Autonomous AI Database DATABASE_ID in project PROJECT_ID in region REGION_ID."
  * "List Autonomous AI Databases in project PROJECT_ID in region REGION_ID."
  * "Get Autonomous AI Database DATABASE_ID in project PROJECT_ID in region REGION_ID."



In the prompts, replace the following:

  * PROJECT_ID with your Google Cloud project ID.
  * ZONE_ID with your Google Cloud Oracle zone.
  * REGION_ID with your Google Cloud region.
  * ODB_NETWORK_ID with the ODB Network ID.
  * ODB_SUBNET_ID with the ODB Subnet ID.
  * CLUSTER_ID with the Exadata VM Cluster ID.
  * CLUSTER_ID with the Exascale VM Cluster ID.
  * VAULT_ID with the Exascale Storage Vault ID.
  * DB_SYSTEM_ID with the DB system ID.
  * DATABASE_ID with the Autonomous AI Database ID.



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

  * Read the [Oracle Database@Google Cloud MCP reference documentation](https://docs.cloud.google.com/oracle/database/docs/reference/mcp).
  * Learn more about [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
