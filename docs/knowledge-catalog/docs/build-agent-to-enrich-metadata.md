---
url: https://docs.cloud.google.com/knowledge-catalog/docs/build-agent-to-enrich-metadata/
title: Build an agent to enrich your metadata \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:57.160604+00:00
---

# Build an agent to enrich your metadata  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/build-agent-to-enrich-metadata/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Build an agent to enrich your metadata Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Catalog (formerly Dataplex Universal Catalog) manages metadata for data assets across the organization. This metadata provides the context that agents use to discover, understand, and query the data required to answer user questions.

While Knowledge Catalog automatically manages resources, tracks technical schemas, and generates descriptions and [data profiles](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview), valuable business context often resides in other locations, such as:

  * Internal documents and wikis
  * Code repositories
  * Communication channels such as Google Chat and Slack



You can build AI agents to extract context from these sources and continuously enrich your metadata at scale. This tutorial uses sample code from the [`knowledge-catalog`](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/samples/enrichment) repository to show you how to build an agent that does the following:

  * **Extract context:** Extracts business context from knowledge bases, documents, code, or chat to enrich technical metadata.
  * **Generate documentation:** Generates documentation for BigQuery tables based on extracted context and other information sources.
  * **Improve search and discovery:** Publishes generated documentation to Knowledge Catalog, making entries easier to find and understand through search.



## Before you begin

To run the Knowledge Catalog enrichment agent, you must meet the following requirements:

### Required roles

To get the permissions that you need to use the enrichment agent, ask your administrator to grant you the following IAM roles on your Google Cloud project iam.gserviceaccount.com: 

  * To manage sample BigQuery resources: [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) 
  * To search for catalog metadata: [Dataplex Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.viewer) (`roles/dataplex.viewer`) 
  * To manage catalog metadata: [Dataplex Catalog Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) 
  * To access Vertex AI features (Gemini LLM APIs): [Vertex AI User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`) 
  * To consume service APIs: [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the enrichment agent. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the enrichment agent:

  * `bigquery.projects.get/createDatasets`
  * `dataplex.projects.search`
  * `dataplex.entryGroups.get/updateEntries`
  * `aiplatform.endpoints.predict`
  * `serviceusage.services.use`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

To use Knowledge Catalog enrichment agent, enable the following APIs in your project:

  * BigQuery API
  * Knowledge Catalog API
  * Vertex AI API
  * Service Usage API



**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,dataplex.googleapis.com,aiplatform.googleapis.com,serviceusage.googleapis.com)

### Install dependencies

You need the following Python packages and tools to run the sample:

  * `google-adk` (Agent Development Kit (ADK))
  * `google-cloud-dataplex` Knowledge Catalog Python Client
  * `google-auth` manages [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials)
  * `mcp[cli]` for building a sample MCP server
  * `gcloud` for authentication and configuration. To install Google Cloud CLI, see the [Google Cloud SDK](https://docs.cloud.google.com/sdk/docs/install) documentation.



## Set up the environment

  1. Configure `gcloud` and sign in:
         
         gcloud auth application-default login
         gcloud config set core/project PROJECT_ID
         

Replace the following:

     * `PROJECT_ID` with the ID of your project
  2. Clone the [`knowledge-catalog`](https://github.com/GoogleCloudPlatform/knowledge-catalog) repository and navigate to the sample source directory:
         
         git clone https://github.com/GoogleCloudPlatform/knowledge-catalog.git
         cd knowledge-catalog/samples/enrichment/src
         

  3. To install dependencies, use the provided script that sets up a Python virtual environment and the necessary environment variables:
         
         source env.sh --install
         

  4. To create a sample BigQuery dataset named `kc_sample_analytics` in the `us` region of your cloud project, run the `create_data.py` script:
         
         python3 ../sample/data/create_data.py
         

The sample also includes a number of documents in the `sample/docs` directory. These documents form a local knowledge base. The enrichment agent uses this knowledge base to extract information and produce documentation.




## Download metadata

Start by running the download tool to extract a metadata snapshot from Knowledge Catalog for the BigQuery dataset and its tables. This creates local metadata artifacts.

The `--dir` argument specifies the directory where the metadata files are written.
    
    
    python3 -m enrichment.download \
      --dir ../sample/metadata.initial \
      --dataset ${KC_ENRICH_SAMPLE_PROJECT}.kc_sample_analytics
    

The script creates one Markdown file per table in the `sample/metadata` directory using the following naming convention: `<project_id>.<dataset_id>.<table_id>.md`.

## Enrich the metadata

After you create the local Markdown files, run the enrichment agent. The agent iterates over each file, finds information relevant to the tables, and summarizes findings along with citations to generate updated Markdown files.

  * `--dir`: Specifies the directory containing the local metadata files.
  * `--output-dir`: Specifies the target directory for the updated metadata files.
  * `--config-dir`: Specifies the directory that contains agent instructions, MCP tools, and skills.


    
    
    python3 -m enrichment.enrich \
      --dir ../sample/metadata.initial \
      --output-dir ../sample/metadata.new \
      --config-dir ../sample/config
    

## Review the metadata

The enriched metadata files contain the agent-produced documentation. Review and modify the files as needed before publishing the changes to Knowledge Catalog.
    
    
    git diff --no-index ../sample/metadata.initial ../sample/metadata.new
    

## Publish the metadata

Run the publish tool to deploy the enriched metadata to Knowledge Catalog.
    
    
    python3 -m src.enrichment.publish --dir ../sample/metadata.new
    

## Customize for your data

In the previous step, you used the `--config-dir` argument to point the agent to the `../sample/config` directory for its configuration. This is how the agent knows where to find information and how to interact with different sources.

The sample comes with a default configuration that instructs the agent to use a local MCP server to access files in the local knowledge base (`sample/docs`). To apply this workflow in your environment, you can customize these configuration files to connect the agent to your internal wikis, code repositories, Google Drive, or other systems.

The `sample/config/` directory contains the following files:
    
    
    sample/config/
    ├─ instructions.md
    ├─ mcp.json
    └─ skills/
        └─ kb-search/
            └─ SKILL.md
    

  * `instructions.md`: Augments the agent's baseline instructions with details relevant to your organization, such as telling it to search a specific knowledge base.
  * `mcp.json`: Configures MCP servers that the agent can use to access tools for your information sources, such as a tool to read files from a local directory.
  * `SKILL.md`: Describes how the agent should use specific tools to interact with an information source, such as using `list_contents`, `read_file`, and `search_content` to find information in local documents.



## Explore the sample Knowledge Catalog code

The `download` and `publish` tools in the enrichment flow section use Knowledge Catalog APIs to read and write metadata.

This section covers how these APIs work so you can adapt the sample for your own integrations.

### Search for and retrieve metadata

The sample uses the following APIs to search for and retrieve metadata:

  * `SearchEntries` to retrieve the entry and location metadata for the dataset.
  * `ListEntries` to enumerate BigQuery tables within a Catalog EntryGroup.
  * `GetEntry` to fetch the specific metadata for each BigQuery table.



The following code shows how to search for a dataset to locate its entry group, list all contained tables, and retrieve their specific metadata:
    
    
    import google.cloud.dataplex_v1 as dataplex
    
    BIGQUERY_TABLE_TYPE = "projects/dataplex-types/locations/global/entryTypes/bigquery-table"
    OVERVIEW_ASPECT_TYPE = "projects/dataplex-types/locations/global/aspectTypes/overview"
    
    catalog = dataplex.CatalogServiceClient()
    
    dataset_reference = '...'   # project_id.dataset_id
    project_id, dataset_id = dataset_reference.split('.')
    
    # 1. Search for dataset to determine its location
    search_response = catalog.search_entries(
        request=dataplex.SearchEntriesRequest(
            name=f"projects/{project_id}/locations/global",
            query=f"type=dataset name={dataset_id}",
            page_size=1
        )
    )
    dataset_entry = search_response.results[0].dataplex_entry
    location_id = dataset_entry.entry_source.location
    
    # 2. List resources in the underlying group
    entry_group_name = f"projects/{project_id}/locations/{location_id}/entryGroups/@bigquery"
    entry_filter = f'parent_entry="{dataset_entry.name}"'
    list_response = catalog.list_entries(
        request=dataplex.ListEntriesRequest(
            parent=entry_group_name,
            entry_filter=entry_filter,
        )
    )
    
    # 3. Retrieve metadata for each table in the list
    for table_entry in list_response.entries:
        entry = catalog.get_entry(
            request=dataplex.GetEntryRequest(
                name=table_entry.name,
                view="CUSTOM",
                aspect_types=[OVERVIEW_ASPECT_TYPE]
            )
        )
    

### Update table metadata

The following code shows how to publish the generated documentation to the Overview aspect for a table and update its metadata:
    
    
    import google.cloud.dataplex_v1 as dataplex
    import google.protobuf.field_mask_pb2 as field_mask_pb2
    import google.protobuf.json_format as jsonpb
    
    OVERVIEW_ASPECT_TYPE = "projects/dataplex-types/locations/global/aspectTypes/overview"
    OVERVIEW_ASPECT_KEY = "dataplex-types.global.overview"
    
    catalog = dataplex.CatalogServiceClient()
    
    table_reference = "..."    # project_id.dataset_id.table_id
    project_id, dataset_id, table_id = table_reference.split('.')
    
    entry_data = {
        "name": f"bigquery.googleapis.com/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}",
        "aspects": {
            OVERVIEW_ASPECT_KEY: {
                "aspectType": OVERVIEW_ASPECT_TYPE,
                "data": {
                    "content": "...", # content parsed from local markdown file
                    "contentType": "MARKDOWN"
                }
            }
        }
    }
    
    entry = dataplex.Entry()
    jsonpb.ParseDict(entry_data, entry._pb)
    
    catalog.update_entry(
        request=dataplex.UpdateEntryRequest(
            entry=entry,
            update_mask=field_mask_pb2.FieldMask(paths=["aspects"]),
            aspect_keys=[OVERVIEW_ASPECT_KEY],
        )
    )
    

## What's next

  * Learn more about working with [metadata](https://docs.cloud.google.com/knowledge-catalog/docs/metadata).
  * Use the Antigravity CLI to [test your data context](https://docs.cloud.google.com/knowledge-catalog/docs/use-antigravity-cli-agent-to-test-data-context).
  * Learn about [managing aspects and enriching metadata](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata).
  * Explore other classes and methods available in the [Knowledge Catalog client library for Python](https://cloud.google.com/python/docs/reference/dataplex/latest).
  * Try other [Knowledge Catalog use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
