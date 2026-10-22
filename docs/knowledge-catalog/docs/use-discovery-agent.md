---
url: https://docs.cloud.google.com/knowledge-catalog/docs/use-discovery-agent/
title: Build an agent to discover your data \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:48.050884+00:00
---

# Build an agent to discover your data  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/use-discovery-agent/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Build an agent to discover your data Stay organized with collections  Save and categorize content based on your preferences. 

The Knowledge Catalog discovery agent is an AI-powered assistant that improves search relevance for complex natural language queries based on Knowledge Catalog search capabilities. By optimizing query understanding and formulation, it provides more accurate results than the standard Knowledge Catalog Search API. This capability is critical especially for complex or lengthy queries.

## Use cases

The discovery agent provides a rich, conversational experience for scenarios such as the following:

  * **Complex or combined intents and constraints:** Handling search requests with multiple criteria, such as finding datasets in `us-central1` but excluding resources in BigQuery.
  * **Business-oriented search:** Discovering data assets based on intent and business context rather than matching exact technical terms.
  * **Multi-turn exploration:** Refining your search through a conversational dialogue to narrow down results.



The discovery agent is built on top of [Knowledge Catalog semantic search](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets) which provides you out-of-the box hybrid search. You can continue to use Knowledge Catalog semantic search directly when you need to process high-intent searches (when you know the specific resource or column), low-latency requirements, or zero-setup hybrid search.

## How it works

The discovery agent performs the following steps to respond to a search query: 

  1. Analyzes input for intent to understand the query, generates multiple search variations, and maps terms to metadata filters.
  2. Searches for resources using the Knowledge Catalog semantic search.
  3. Ranks the merged results based on relevance.



The following diagram provides the details of the process:

![Discovery agent process for search requests.](https://docs.cloud.google.com/static/knowledge-catalog/images/discovery-agent-process.png) Processing path for search requests in the discovery agent.![](https://docs.cloud.google.com/static/knowledge-catalog/images/discovery-agent-process.png)

The agent relies on the Knowledge Catalog Search API to fetch relevant Google Cloud resources. The following code snippet shows how the agent calls Knowledge Catalog semantic search:
    
    
          # Configure the request parameters for the
          # call to Knowledge Catalog Semantic Search API.
          endpoint = "dataplex.googleapis.com"
    
          client = dataplex_v1.CatalogServiceClient(
              client_options={"api_endpoint": endpoint}
          )
    
          location = "global"
          consumer_project_id = "my-gcp-project"
          parent_name = f"projects/{consumer_project_id}/locations/{location}"
    
          # Call Knowledge Catalog Semantic Search API.
          response = client.search_entries(
              request={
                  "name": parent_name,
                  "query": query,
                  "page_size": 50,
                  "semantic_search": True,
              }
          )
    
          # Call Knowledge Catalog LookupContext for each search result
          # to retrieve rich, LLM-ready metadata.
          entries = []
          for result in response.results:
              entry_name = result.dataplex_entry.name
              
              # Prepare the LookupContext request for the specific resource
              lookup_request = {
                  "name": parent_name,
                  "resources": [entry_name]
              }
              
              # Call the LookupContext API
              lookup_response = client.lookup_context(request=lookup_request)
              
              # Extract the rich context YAML to share with the agent
              entries.append({
                  "entry_name": entry_name,
                  "context": lookup_response.context
              })
    
          return {"results": entries}
    

## Before you begin

To run the Knowledge Catalog discovery agent, ensure you meet the following requirements:

### Required roles

To get the permissions that you need to use the discovery agent, ask your administrator to grant you the following IAM roles on your Google Cloud project iam.gserviceaccount.com: 

  * [Dataplex Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`)
  * [Vertex AI User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the discovery agent. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the discovery agent:

  * `dataplex.projects.search`
  * `aiplatform.endpoints.predict`
  * `serviceusage.services.use`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

To use Knowledge Catalog discovery agent, enable the following APIs in your project: Knowledge Catalog API, Vertex AI API, and Service Usage API.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,aiplatform.googleapis.com,serviceusage.googleapis.com)

## Set up the environment

To set up the development environment for the discovery agent, do the following:

  1. Clone the `dataplex-labs` repository.
         
         git clone https://github.com/GoogleCloudPlatform/dataplex-labs.git
         

  2. Change to the agent directory:
         
         cd dataplex-labs/knowledge_catalog_discovery_agent
         

  3. Create and activate a Python Virtual Environment, then install the dependencies listed in the [`requirements.txt`](https://github.com/GoogleCloudPlatform/dataplex-labs/tree/main/knowledge_catalog_discovery_agent/requirements.txt) file:

     * `google-adk` (Agent Development Kit) 
     * `google-cloud-dataplex` (Knowledge Catalog Python Client)
     * `google-api-core`
    
    python3 -m venv /tmp/kcsearch
    
      source /tmp/kcsearch/bin/activate
    
      pip3 install -r requirements.txt
    

  4. Set up the environment variables with the following command:
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID
         export GOOGLE_GENAI_USE_VERTEXAI=True
         

Replace the following:

     * `PROJECT_ID` with the ID of your project



## Run the discovery agent as the root agent

To run the discovery agent directly as the root agent, do the following:

  1. In the `agent.py` file located in the `knowledge_catalog_discovery_agent` folder, rename the `discovery_agent` variable to `root_agent`.
  2. Run the agent using the [`adk run`](https://adk.dev/get-started/python/#run-with-command-line-interface) command:
         
         adk run path/to/agent/parent/folder
         

Replace the following:

     * `path/to/agent/parent/folder` with the parent directory that contains the folder with your agent. For example, if your agent resides in `knowledge_catalog_discovery_agent/`, run `adk run` from the `agents/` directory.



## Run the discovery agent as an agent tool

To integrate the discovery agent into a larger custom agent, such as `my_custom_agent`, do the following:

  1. Set up your project structure to contain the discovery agent module:
         
         my_custom_agent/
         ├── agent.py
         └── knowledge_catalog_discovery_agent/
             ├── SKILL.md
             ├── agent.py
             ├── tools.py
             └── utils.py
         

  2. In your custom agent's `agent.py` file, import the discovery agent and use it as an agent tool. See the example:
         
         root_agent = llm_agent.Agent(
             model=google_llm.Gemini(model=GEMINI_MODEL),
             name="my_custom_agent",
             instruction=(
                 "You are a Custom Agent. Your goal is to help users understand"
                 " their data landscape, evaluate data assets, and derive insights"
                 " from available resources. **IMPORTANT**: You should use the"
                 " `knowledge_catalog_discovery_agent` to search for and discover"
                 " data assets. For best results, pass in the Natural Language user'"
                 " query as is to the `knowledge_catalog_discovery_agent`. Once assets"
                 " are found, you should analyze their metadata, compare them, and"
                 " provide recommendations or summaries to the user to help them make"
                 " decisions. Focus on general metadata summary and comparison."
             ),
             tools=[
                 agent_tool.AgentTool(discovery_agent),
             ],
         )
         

  3. Run the agent using the `adk run` command:
         
         adk run path/to/agent/parent/folder
         

Replace the following:

     * `path/to/agent/parent/folder` with the parent directory that contains your `my_custom_agent/` folder. For example, if your agent resides in `agents/my_custom_agent/`, run `adk run` from the `agents/` directory.



## What's next

  * Understand [search syntax for Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-syntax).
  * Learn more about [Agent Development Kit](https://adk.dev/get-started/python/).
  * Try other [Knowledge Catalog use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
