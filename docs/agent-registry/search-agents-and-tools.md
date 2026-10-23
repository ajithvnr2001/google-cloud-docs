---
url: https://docs.cloud.google.com/agent-registry/search-agents-and-tools/
title: Search for agents, tools, and skills \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:15.654864+00:00
---

# Search for agents, tools, and skills  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/search-agents-and-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Search for agents, tools, and skills Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry lets you search across your registered agents, Agent2Agent (A2A) skills, standalone skills, and Model Context Protocol (MCP) servers by keyword, prefix, or natural language in the Google Cloud console, Google Cloud CLI, or the Agent Registry API. Keyword and prefix searches help you quickly find resources by name, identifier, or metadata. Semantic search finds conceptually related capabilities across natural language instructions and descriptions based on intent.

Search queries evaluate agent, MCP server, and skill capability descriptions, tool schemas, and skill instructions. You can't use search queries to discover endpoints; for instructions on listing and filtering endpoints by metadata, see Discover endpoints and filter components by metadata.

## Before you begin

  1. [Register an agent](https://docs.cloud.google.com/agent-registry/register-agents), an [MCP server](https://docs.cloud.google.com/agent-registry/register-mcp-servers), or a [skill](https://docs.cloud.google.com/agent-registry/register-skills) in Agent Registry.
  2. Get [the project ID](https://support.google.com/googleapi/answer/7014113) for the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled.
  3. To use the gcloud CLI commands in this document, [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).



### Required roles

To get the permissions that you need to search for agents, tools, and skills in Agent Registry, ask your administrator to grant you the [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) IAM role on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Search for agents and tools

To discover capabilities within your registry, you can search for registered agents and MCP servers in the Google Cloud console, gcloud CLI, or the REST API.

When you search for agents or MCP servers, you can query by display name, description, or capability keywords:

  * **Agents** : search queries check the agent's display name, description, [agent identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers), and the names, descriptions, and tags of inline [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a) declared in its Agent Card to find a match.
  * **MCP servers** : search queries check the server's display name, description, [MCP server identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#mcp-server-identifiers), and the names and descriptions of its tools to find a match.



### Search by keywords

You can perform a keyword search to find resources that contain specific terms across their capabilities, such as an agent's A2A skill or an MCP server's tool. To understand how these capabilities are structured in the registry, see [JSON schemas](https://docs.cloud.google.com/agent-registry/json-schemas). For a complete list of searchable fields, see the [API reference](https://docs.cloud.google.com/agent-registry/reference/rest).

Keyword queries accept free-text strings and support the logical operators `AND`, `OR`, and `NOT`:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select your Google Cloud project.

  3. In the **Search your registry** bar at the top of the page, enter a keyword query of at least three characters, such as `flight` or `database`, or a field filter, such as `Name:booking`, and then press `Enter`.

The **Search results** table displays matching agents, MCP servers, and standalone skills across your selected locations.




###  gcloud 

Provide the `--search-string` flag to the [`gcloud agent-registry agents search`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/agents/search) or [`gcloud agent-registry mcp-servers search`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/mcp-servers/search) command.

For example, search for an agent that can handle flight bookings:
    
    
    gcloud agent-registry agents search \
        --project=PROJECT_ID \
        --location=REGION \
        --search-string="flight OR booking"
    

Search for an MCP server that provides database tools:
    
    
    gcloud agent-registry mcp-servers search \
        --project=PROJECT_ID \
        --location=REGION \
        --search-string="database"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



###  REST 

Send a `POST` request to the [`agents:search`](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.agents/search) or [`mcpServers:search`](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers/search) endpoint with the `searchString` field in the request body.

For example, search for an agent that can handle flight bookings:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{"searchString": "flight OR booking"}' \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/agents:search"
    

Search for an MCP server that provides database tools:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{"searchString": "database"}' \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/mcpServers:search"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



### Search by prefix

Prefix searches are optimized for low latency, letting your applications retrieve relevant agents and tools dynamically as a user types.

If you are building an orchestrator interface or an autocomplete feature, you can perform prefix searches in Agent Registry to find results that start with a given string. Prefix searches use the `*` suffix wildcard symbol to search for the beginning of a word:

###  gcloud 

Run the [`gcloud agent-registry agents search`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/agents/search) or [`gcloud agent-registry mcp-servers search`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/mcp-servers/search) command with a prefix expression.

For example, search for agents whose display name begins with `Best_A2A_*`:
    
    
    gcloud agent-registry agents search \
        --project=PROJECT_ID \
        --location=REGION \
        --search-string="displayName:Best_A2A_*"
    

Similarly, search for MCP servers whose display name begins with `Prod_Server_*`:
    
    
    gcloud agent-registry mcp-servers search \
        --project=PROJECT_ID \
        --location=REGION \
        --search-string="displayName:Prod_Server_*"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



###  REST 

Pass the prefix expression in the `searchString` field of the request body:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{"searchString": "displayName:Best_A2A_*"}' \
        "https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/agents:search"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



## Search for standalone skills

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can search for standalone [skills](https://docs.cloud.google.com/agent-registry/skills-architecture) registered in Agent Registry. This feature lets you discover reusable capabilities to attach to your agents.

When you search for skills, you search for the default [skill revision](https://docs.cloud.google.com/agent-registry/skills-architecture#skill-revision). To update the default revision of a skill, see [Update skill metadata or default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill).

### Search modes

You can use two search modes for skills based on your requirements:

  * **Keyword search** : scans only basic metadata attributes such as the display name, description, [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names), and [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers). This mode is optimized for low-latency searches, exact lookups, and name autocomplete. For an example, see Search for skills by keyword or expression.
  * **Semantic search** : automatically indexes the complete contents of the `SKILL.md` payload, including natural language instructions, scripts, and metadata assets. This mode identifies conceptual themes and is optimized for orchestrator agents discovering relevant capability bundles dynamically, based on your intent. For an example, see Search for skills by semantic meaning.



### Search fields and syntax

When searching by metadata or keyword strings, the following fields are indexed:

Field name | Case behavior | Prefix search | All-fields search | Description  
---|---|---|---|---  
`displayName` | Case insensitive | Yes | Yes | The display name of the skill. Use this field to search for common names.  
`description` | Case insensitive | No | Yes | The detailed description of the skill's purpose and functionality. Use this field to search for keywords.  
`name` | Case insensitive | Yes | Yes | The [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names) of the skill. Use this field to search by resource name.  
`skillId` | Case insensitive | Yes | Yes | The [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) of the skill. Use this field to find a specific publisher's assets. For example, the format for Google-managed skills is `urn:skill:PUBLISHER_ID:NAMESPACE:SKILL_ID`.   
`publisher` | Case insensitive | Yes | No | The publisher associated with the skill. Use this field to filter by the publishing organization.  
`frontmatter.name` | Case insensitive | No | No | The name of the skill defined in the front matter of the `SKILL.md` file.  
`frontmatter.description` | Case insensitive | No | No | The description of the skill defined in the front matter of the `SKILL.md` file.  
`frontmatter.compatibility` | Case insensitive | No | No | The compatibility of the skill defined in the front matter of the `SKILL.md` file.  
`frontmatter.license` | Case insensitive | No | No | The license of the skill defined in the front matter of the `SKILL.md` file.  
`createTime` | Not applicable | No | No | The timestamp when the skill was created. This field is only available in filters. Supports range operators, such as `<`, `>`, and exact matches.  
`updateTime` | Not applicable | No | No | The timestamp when the skill was last updated. This field is only available in filters. Supports range operators, such as `<`, `>`, and exact matches.  
  
To search for skills, provide a query string using the `--query` flag in gcloud CLI or the `searchString` parameter in the REST API. You can use the following syntax elements in your search requests:

  * **Boolean operators** : include `AND`, `OR`, or `NOT` operators to chain requirements.
  * **Field-specific filters** : target a field using the `:` operator, for example, `displayName:database`.
  * **Prefix search** : use the `*` suffix wildcard symbol to find values starting with a specific prefix, for example, `displayName:cloud-*`.



### Search for skills by keyword or expression

Search for skills that have a specific display name prefix and description keyword:

###  gcloud 

Run the [`gcloud alpha agent-registry skills search`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/skills/search) command with `--search-type=keyword`:
    
    
    gcloud alpha agent-registry skills search \
        --project=PROJECT_ID \
        --location=REGION \
        --query="displayName:cloud-* AND description:database" \
        --search-type=keyword
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



###  REST 

Send a `GET` request to the [`skills:search`](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/search) endpoint with `searchString` and `searchType=KEYWORD`:
    
    
    curl -G -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        --data-urlencode "searchString=displayName:cloud-* AND description:database" \
        --data-urlencode "searchType=KEYWORD" \
        "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/REGION/skills:search"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



### Search for skills by semantic meaning

Find skills related to managing relational databases by using semantic search:

###  gcloud 

Run the [`gcloud alpha agent-registry skills search`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/skills/search) command with `--search-type=semantic`:
    
    
    gcloud alpha agent-registry skills search \
        --project=PROJECT_ID \
        --location=REGION \
        --query="manage and configure relational databases" \
        --search-type=semantic
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



###  REST 

Send a `GET` request to the [`skills:search`](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/search) endpoint with `searchString` and `searchType=SEMANTIC`:
    
    
    curl -G -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        --data-urlencode "searchString=manage and configure relational databases" \
        --data-urlencode "searchType=SEMANTIC" \
        "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/REGION/skills:search"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region or `global`.



### Google-managed skills

Google-managed skills are discoverable from any project. For a list of available Google-managed skills, see the [`google/skills` repository](https://github.com/google/skills/tree/main) on GitHub.

## Discover endpoints and filter components by metadata

You can also discover any component in Agent Registry, including registered [endpoints](https://docs.cloud.google.com/agent-registry/register-endpoints), by listing its collection and filtering on structured metadata fields:

  * **Discover endpoints** : because `Endpoint` resources don't support `:search` queries, you discover them by browsing the **Endpoints** tab in the Google Cloud console, running `gcloud agent-registry endpoints list --filter`, or calling the [`endpoints.list`](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints/list) REST method. For complete instructions, see [Manage and discover endpoints](https://docs.cloud.google.com/agent-registry/manage-endpoints#discover-endpoints).
  * **Filter agents, MCP servers, and skills** : when you know a component's [registry identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#registry-identifiers) (URN), display name, or attribute, filter the collection in the Google Cloud console or pass `--filter` to `gcloud agent-registry agents list`, `gcloud agent-registry mcp-servers list`, or `gcloud alpha agent-registry skills list`. For details, see [Manage agents](https://docs.cloud.google.com/agent-registry/manage-agents), [Manage MCP servers and tools](https://docs.cloud.google.com/agent-registry/manage-mcp-tools), and [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
