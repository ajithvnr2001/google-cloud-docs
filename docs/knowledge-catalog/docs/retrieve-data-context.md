---
url: https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context/
title: Retrieve context for data assets \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:27.903261+00:00
---

# Retrieve context for data assets  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Retrieve context for data assets Stay organized with collections  Save and categorize content based on your preferences. 

The context that surrounds your data equips your AI applications with a deep understanding of your data assets, improving the accuracy and relevance of LLM-generated responses.

The [`lookupContext`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupContext) method bridges the context gap using a single API request to retrieve a pre-formatted bundle of data asset metadata optimized for interactive agentic workflows. You can use this compact, LLM-ready context to ground your agents in assessing and using data assets.

You can use the `lookupContext` method for any data assets stored in Knowledge Catalog, for example, BigQuery tables, datasets, and routines, as well as [data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-use#retrieve-domain-context) and any other [entries](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview#entries).

## How can agents get data context?

  1. The agent retrieves data assets that are potentially relevant for context retrieval, for example, by using [Knowledge Catalog semantic search](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).
  2. The agent uses the `lookupContext` method to make a single API call or an MCP tool request that retrieves the context for a specific asset.
  3. The method returns a response containing a pre-formatted text block. Depending on the `format` parameter you specify in the request, the document can be in YAML, XML, or JSON format.

The response contains the following context elements:

Context element | Description  
---|---  
Technical metadata | Resource schemas and physical configurations, such as BigQuery partition and clustering strategies, and BigQuery routine definitions, including arguments, return types, and source code.  
Operational metadata | Joins and other relationships, based on historical query logs and data insights. For more information, see [View data relationships](https://docs.cloud.google.com/knowledge-catalog/docs/data-relationships).  
Business descriptions | Related business terms, overviews, catalog annotations, descriptions captured in the source system and auto-generated in Knowledge Catalog, and guidelines.  
  
Note: You can use the guidelines aspect on data assets to capture additional context useful for agents when they discover, inspect, or use data assets.  
Data profile | Distribution statistics, distinct value counts, null ratios, and sample values.  
Data quality | Automated data quality check outputs against predefined rules.  
Context on related data assets | Context on related data assets, such as glossary terms or other related assets, like frequently joined tables. The context returned for related assets includes the same range of elements as for the main asset or assets.  
  4. The agent uses this response to guide the selection of relevant assets or their usage.




## Before you begin

Before using the `lookupContext` method, ensure you have the necessary roles and enable the required APIs.

### Required roles

To get the permissions that you need to call the `lookupContext` method, ask your administrator to grant you the following IAM roles on your Google Cloud project iam.gserviceaccount.com: 

  * Read access to catalog resources, including entries, entry groups, and glossaries: [Dataplex Catalog Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

To use the `lookupContext` method, enable the following APIs in your project:

  * Knowledge Catalog API



**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

## Retrieve context for a data asset

To retrieve the context for a data asset, access the `lookupContext` method directly with the [Dataplex API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupContext) or use [Knowledge Catalog remote Model Context Protocol (MCP) server](https://docs.cloud.google.com/knowledge-catalog/docs/use-remote-mcp) or [MCP Toolbox For Databases](https://mcp-toolbox.dev/integrations/knowledge-catalog/tools/knowledge-catalog-lookup-context/).

The `lookupContext` method filters the resources based on your permissions. The response contains data only for assets that your identity has the necessary Identity and Access Management (IAM) permissions to access. If you have no permissions on the requested resources, the method returns an empty response.

###  REST 

To retrieve context for a data asset, send the following request:
    
    
    curl --request POST \
       'https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:lookupContext' \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
      "resources": RESOURCES
      "options": OPTIONS
      }' \
    --compressed
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the region where the asset exists (for example, `us-central1`)
  * RESOURCES: up to ten entry names to retrieve context for, formatted as `projects/{project}/locations/{location}/entryGroups/{entryGroup}/entries/{entry}`. For multiple resources, the API establishes relationships between the requested resources, such as frequent schema joins, and returns the relationship information in the context.
  * OPTIONS: the options that let you define the context: 
    * `format` is the format of the context file. For example, `yaml`.
    * `context_budget` is the number of characters to which the response is limited. If you set the `all_schema_fields` parameter to `true`, the API returns all schema fields regardless of the `context_budget` value.



An example request that retrieves context for a BigQuery table looks as follows:
    
    
    curl --request POST \
    'https://dataplex.googleapis.com/v1/projects/test-project/locations/us:lookupContext?key=[YOUR_API_KEY]' \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "resources":
        ["projects/test-project/locations/us/entryGroups/@bigquery/entries/bigquery.googleapis.com/projects/test-project/datasets/test-dataset/tables/test-table"],
        "options":
        {
          "format":"yaml",
          "context_budget":"4000"
        }
      }' \
    --compressed
    

The response is a pre-formatted block of text similar to the following:
    
    
    {
    "context": "resource: \"projects/test-project/locations/us/entryGroups/@bigquery/entries/bigquery.googleapis.com/projects/test-project/datasets/sales_data/tables/orders\"\ntechnical_metadata:\n  schema:\n    - name: order_id\n      type: STRING\n      description: \"Primary key for the order.\"\n    - name: customer_id\n      type: STRING\n    - name: total_amount\n      type: NUMERIC\n  partitioning:\n    type: TIMESTAMP\n    field: order_date\nbusiness_descriptions:\n  overview: \"Historical record of all customer transactions.\"\n  related_terms:\n    - \"Revenue\"\n    - \"Sales Transactions\"\n  guidelines: \"Always filter by 'order_date' to optimize query costs due to partitioning.\"\ndata_profile:\n  columns:\n    - name: total_amount\n      null_ratio: 0.001\n      distinct_values: 52340\n      sample_values: [45.99, 120.00, 15.50]\ndata_quality:\n  summary:\n    - rule: \"positive_amounts\"\n      status: PASSED\n      description: \"Ensures total_amount is greater than zero.\"\noperational_metadata:\n  frequent_joins:\n    - table: \"projects/test-project/locations/us/entryGroups/@bigquery/entries/bigquery.googleapis.com/projects/test-project/datasets/sales_data/tables/customers\"\n      join_key: \"customer_id\"\n"
    }
    

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_lookup_context():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[LookupContextRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.LookupContextRequest.html)(
            name="name_value",
            resources=["resources_value1", "resources_value2"],
        )
    
        # Make the request
        response = client.[lookup_context](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_lookup_context)(request=request)
    
        # Handle the response
        print(response)
    
    

The following example shows how to retrieve context for a BigQuery table:
    
    
     from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
     # Initialize the client
     client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
     # Define the request with a seed resource
     request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[LookupContextRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.LookupContextRequest.html)(
         name="projects/test-project/locations/us",
         resources=["projects/test-project/locations/us/entryGroups/@bigquery/entries/bigquery.googleapis.com/projects/test-project/datasets/test-dataset/tables/test-table"],
         options={"format": "yaml", "budget": "4000"}
     )
    
     # Retrieve the LLM-ready context
     response = client.[lookup_context](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_lookup_context)(request=request)
     context_yaml = response.context
    
     print(f"Retrieved Context: \n{context_yaml}")
    

## Retrieve context for routines

You can use the `lookupContext` method to retrieve context for [BigQuery routines](https://docs.cloud.google.com/bigquery/docs/routines-intro), such as user-defined functions, table functions, and stored procedures. Agents can use this context to understand what a routine does and how to call it, for example, when they generate SQL queries. The context for a routine includes the following information:

  * The routine type, such as scalar function, table function, or procedure.
  * The routine language.
  * The routine arguments and return type.
  * The routine source code (definition body).
  * Descriptions and other metadata from Knowledge Catalog.



To retrieve context for a routine, include the entry name of the routine in the `resources` list of the request. The entry name has the following format:
    
    
    projects/PROJECT_ID/locations/LOCATION/entryGroups/@bigquery/entries/bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/routines/ROUTINE_ID
    

Replace the following:

  * PROJECT_ID: the ID of the project that contains the routine.
  * LOCATION: the location of the dataset that contains the routine (for example, `us`).
  * DATASET_ID: the ID of the dataset that contains the routine.
  * ROUTINE_ID: the ID of the routine.



## What are some best practices for context lookups?

To optimize your results when using the `lookupContext` method, consider the following best practices:

  * Request the selected length of the output context with `context_budget` parameter. The `lookupContext` method will aim to fit the most relevant context into output as close as possible within the limits prescribed by the parameter.
  * You can list up to ten data assets in the `resources` list. For example, including several tables in the `resources` list makes the API provide the context not only for those tables but also for possible join paths between them therefore providing necessary guidance on how to use these tables together.
  * Use the `format` option, such as `yaml` or `json`, that aligns best with the LLM or agent's parsing logic to avoid costly transformations.



## What's next

  * Learn [how to build an agent to discover your data](https://docs.cloud.google.com/knowledge-catalog/docs/use-discovery-agent).
  * Learn [how to build an agent to enrich your metadata](https://docs.cloud.google.com/knowledge-catalog/docs/build-agent-to-enrich-metadata).
  * Understand [search syntax for Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-syntax).
  * Learn more about [viewing data relationships](https://docs.cloud.google.com/knowledge-catalog/docs/data-relationships).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
