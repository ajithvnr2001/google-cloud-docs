---
url: https://docs.cloud.google.com/agent-registry/search-agents-and-tools/
title: Search for agents, tools, and skills \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:14.440944+00:00
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

As your agentic ecosystem grows, finding the right agent or tool becomes critical. Agent Registry provides search capabilities that let you perform advanced keyword, prefix, and semantic searches across your agents, their skills, and your Model Context Protocol (MCP) servers.

This document explains how to construct search queries to discover capabilities within your environment.

## Before you begin

Before you search for agents, tools, or skills in Agent Registry, [register an agent](https://docs.cloud.google.com/agent-registry/register-agents) or an [MCP server](https://docs.cloud.google.com/agent-registry/register-mcp-servers). You also need [your project ID](https://support.google.com/googleapi/answer/7014113) to perform these tasks.

To use the gcloud CLI commands in this document, make sure you have [set up your Google Cloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).

### Required roles

To get the permissions that you need to search for agents, tools, and skills in Agent Registry, ask your administrator to grant you the [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Search for agents and tools

To discover capabilities within your registry, you can search for registered [agents](https://docs.cloud.google.com/agent-registry/concepts#agent) and [MCP servers](https://docs.cloud.google.com/agent-registry/concepts#server).

Searching for agents matches their basic metadata, description, and descriptive [A2A skills](https://docs.cloud.google.com/agent-registry/concepts#a2a-skill) declared inline in their Agent Card. Searching for MCP servers matches their description and their deterministic [tools](https://docs.cloud.google.com/agent-registry/concepts#tool).

### Search by keywords

You can perform a keyword search to find resources that match specific terms across their capabilities, such as an agent's A2A skill or an MCP server's tool. To understand how these capabilities are structured in the registry, see [JSON schemas](https://docs.cloud.google.com/agent-registry/json-schemas). For a complete list of searchable fields, see the [API reference](https://docs.cloud.google.com/agent-registry/reference/rest).

To search by keywords provide the `--search-string` flag. This parameter accepts free-text queries and supports logical operators: `AND`, `OR`, and `NOT`.

For example, search for an agent that can handle flight bookings:
    
    
    gcloud agent-registry agents search \
      --project=PROJECT_ID \
      --location=REGION \
      --search-string="flight OR booking"
    

You can also search for an MCP server based on the specific tools it offers or its description. For example, search for an MCP server that provides database tools:
    
    
    gcloud agent-registry mcp-servers search \
      --project=PROJECT_ID \
      --location=REGION \
      --search-string="database"
    

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `REGION`: The registry region.



### Search by prefix

Prefix searches are highly optimized for latency, letting your applications retrieve relevant agents and tools dynamically as a user types.

If you are building an orchestrator interface or an autocomplete feature, you can perform prefix searches in Agent Registry to get results matching the beginning of a query string. Prefix searches use the suffix wildcard symbol (`*`) to match the beginning of a word.

For example, search for agents whose display name begins with a specific prefix, such as `Best_A2A_*`:
    
    
    gcloud agent-registry agents search \
      --project=PROJECT_ID \
      --location=REGION \
      --search-string="displayName:Best_A2A_*"
    

Similarly, you can search for MCP servers whose display name begins with a specific prefix, such as `Prod_Server_*`:
    
    
    gcloud agent-registry mcp-servers search \
      --project=PROJECT_ID \
      --location=REGION \
      --search-string="displayName:Prod_Server_*"
    

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `REGION`: The registry region.



## Search for standalone skills

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can search for standalone [skills](https://docs.cloud.google.com/agent-registry/concepts#skill) registered in Agent Registry. This feature lets you discover reusable capabilities to attach to your agents.

When you search for skills, you search for the default [skill revision](https://docs.cloud.google.com/agent-registry/concepts#skill-revision). To update the default revision of a skill, see [Update skill metadata or default revision](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill).

### Search modes

You can use two search modes for skills based on your requirements:

  * **Keyword search:** Scans only basic metadata attributes such as the display name, description, name (URN), and skill ID. This mode is optimized for low-latency searches, matching, and name autocomplete. For an example, see Search for skills by keyword or expression.
  * **Semantic search:** Automatically indexes the complete contents of the `SKILL.md` payload, including natural language instructions, code structure, and assets. This mode matches conceptual themes and is optimized for orchestrator agents discovering relevant capability bundles dynamically, based on your intent. For an example, see Search for skills by semantic meaning.



### Search fields and syntax

When searching by metadata or keyword strings, the following fields are indexed:

Field name | Case behavior | Prefix search | All-fields search | Description  
---|---|---|---|---  
`displayName` | Case insensitive | Yes | Yes | The user-facing name of the skill. Use this field to search for common names.  
`description` | Case insensitive | No | Yes | The detailed description of the skill's purpose and functionality. Use this field to match keywords.  
`name` | Case insensitive | Yes | Yes | The programmatic identifier of the skill. Use this field for matches on identifier strings.  
`skillId` | Case insensitive | Yes | Yes | The logical Uniform Resource Name (URN) of the skill. Use this field to find a specific publisher's assets. For example, the format for Google-created skills is `urn:skill:PUBLISHER_ID:NAMESPACE:SKILL_ID`.   
`publisher` | Case insensitive | Yes | No | The publisher associated with the skill. Use this field to filter by the publishing organization.  
`frontmatter.name` | Case insensitive | No | No | The name of the skill defined in the frontmatter of the `SKILL.md` file.  
`frontmatter.description` | Case insensitive | No | No | The description of the skill defined in the frontmatter of the `SKILL.md` file.  
`frontmatter.compatibility` | Case insensitive | No | No | The compatibility of the skill defined in the frontmatter of the `SKILL.md` file.  
`frontmatter.license` | Case insensitive | No | No | The license of the skill defined in the frontmatter of the `SKILL.md` file.  
`createTime` | Not applicable | No | No | The timestamp when the skill was created. This field is only available in filters. Supports range operators, such as `<`, `>`, and exact matches.  
`updateTime` | Not applicable | No | No | The timestamp when the skill was last updated. This field is only available in filters. Supports range operators, such as `<`, `>`, and exact matches.  
  
To search for skills, provide a query string using the `--query` flag in gcloud CLI or the `searchString` parameter in the REST API. You can use the following syntax elements in your search requests:

  * **Boolean operators:** include `AND`, `OR`, or `NOT` operators to chain requirements.
  * **Field-specific filters:** target a field using the `:` operator, for example, `displayName:database`.
  * **Prefix matching:** use the suffix wildcard symbol (`*`) to find matches starting with a specific prefix, for example, `displayName:cloud-*`.



### Search for skills by keyword or expression

For example, search for skills that match a display name prefix and description keyword:
    
    
    gcloud alpha agent-registry skills search \
      --project=PROJECT_ID \
      --location=REGION \
      --query="displayName:cloud-* AND description:database" \
      --search-type=keyword
    

Replace the following:

  * `PROJECT_ID`: the project ID
  * `REGION`: the registry region



### Search for skills by semantic meaning

For example, find skills related to managing relational databases by using semantic search:
    
    
    gcloud alpha agent-registry skills search \
      --project=PROJECT_ID \
      --location=REGION \
      --query="manage and configure relational databases" \
      --search-type=semantic
    

Replace the following:

  * `PROJECT_ID`: the project ID
  * `REGION`: the registry region



### Public skills

Public skills provided by Google are global and discoverable from any project. For a list of available public skills, see the [`google/skills` repository](https://github.com/google/skills/tree/main) on GitHub.

When you search, Agent Registry dynamically rewrites the resource names of public skills in the output so that they appear hosted in your local project. This process simplifies integration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
