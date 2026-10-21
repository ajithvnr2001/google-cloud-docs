---
url: https://docs.cloud.google.com/knowledge-catalog/docs/about-search/
title: About search in Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:35.671174+00:00
---

# About search in Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/about-search/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About search in Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

Use Knowledge Catalog (formerly Dataplex Universal Catalog) search to discover resources across your organization using natural language queries with semantic matching, keywords, and structured predicates.

**Note:** Knowledge Catalog search supports both semantic and keyword matching. It also supports keyword-only search mode for backward compatibility. For information about keyword-only search, its filters, and how to use it, see [Keyword-only search](https://docs.cloud.google.com/knowledge-catalog/docs/keyword-search).

## Use cases

The following list describes common search use cases, along with descriptions and example queries:

  * **Targeted asset lookup** : Find a specific asset by searching for keywords related to the asset name, columns, or description.

Example queries

    * `retail_transactions_2026`
    * `customer_id`
    * `column:customer_id`

  * **Broad data discovery** : Identify relevant assets across your organization using open-ended natural language or keyword queries.

Example queries

    * `quarterly financial reports`
    * `ad campaign click through rates tables`
    * `server health metrics`
    * `audit logs system=bigquery`

  * **Scoped asset retrieval for workflows** : Enumerate assets within a specific container, such as a project, or with specific properties, such as type or system. This approach is frequently used for programmatic and agentic workflows.

Example queries

    * `type=table projectid:banking-prod aspect:classification.tier=PII`
    * `system=spanner projectid:inventory-service (parent=marketing_analytics OR parent=finance_analytics)`


**Note:** Full data retrieval might be limited, as search is optimized for discovery and exploration by returning a limited set of the most relevant results. For more information, see Recall limitations in search.

## How it works

Search automatically indexes all context for data assets maintained in Knowledge Catalog. This includes the following:

  * Metadata automatically ingested from Google Cloud data sources such as BigQuery and Cloud SQL
  * Context for resources you ingest through connectors and integrations
  * Additional context you create for resources, for example representing business context or describing data semantics. The context might be also captured in the form of [aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata) or linked [business terms](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries#create-manage-terms).



When processing your query, search applies a combination of semantic and keyword matching. The following table describes the query types you can use with Knowledge Catalog search along with descriptions and sample queries:

Query type | Usage | Examples  
---|---|---  
**Single keyword** | For exact and substring matching across metadata elements, such as asset name, description, and schema. | `prd_fin_invoices_fct_v02`  
**Partial keywords and tokenized fragments** | Matches substrings across metadata content, finding resources even with abbreviated terms, separated words, or naming variations. | `fin transactions 2026` (matches `prd_fin_transactions_fy2026_raw`)  
**Natural language queries** | Uses semantic matching without requiring exact name or column matches. | `customer churn prediction features`  
**Structured predicates** | Combines free-text queries with explicit predicate filters for narrowing down search results. | `audit logs system=bigquery`  
**Extended syntax** | For precise search, narrowed down to a specific scope. Extended syntax is most often used in agentic and programmatic use cases. For more information, see [Search syntax](https://docs.cloud.google.com/knowledge-catalog/docs/search-syntax). | `(system:bigquery OR system:spanner) AND column:credit_card_number aspect:classification.tier=PII -projectid:sandbox-project`  
  
## Access search in Knowledge Catalog

You have the following options to access search in Knowledge Catalog:

  * Through the **Search** page in Google Cloud console. For more information, see [Search for resources](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).
  * [`gcloud dataplex entries search`](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/search) gcloud CLI. 
  * [`searchEntries` API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries) and [Cloud Client Libraries](https://docs.cloud.google.com/sdk/docs/libraries-reference).
  * [Remote MCP server](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries) and [MCP Toolbox for Databases](https://mcp-toolbox.dev/integrations/knowledge-catalog/tools/knowledge-catalog-search-entries/) for interactive usage and to power your agentic and programmatic workloads.



## Search scope

The search results in Knowledge Catalog respect permissions that you have over the corresponding resources in source systems.

For example, if you have BigQuery metadata read access to an object, that object appears in your Knowledge Catalog search results. If you have access to a BigQuery table but not to the dataset containing that table, the table still appears as expected in the Knowledge Catalog search.

By default, search is scoped to your organization. Results include only resources from the same organization as the project you're searching in.

The search results include only those resources that belong to the same VPC Service Controls perimeter as the project under which search is performed. When using the Google Cloud console, this is the project that is selected in the console.

To broaden the scope of your search results beyond the resources within your project's VPC Service Controls perimeter, use [VPC Service Controls ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies). These rules facilitate private and efficient data exchange across your organization. You can configure ingress and egress rules using the Google Cloud console or through JSON or YAML files. Refer to the following YAML example and consult the [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs) to tailor the rule to your specific requirements.
    
    
    egressPolicies:
      - egressFrom:
          identityType: ANY_USER_ACCOUNT
        egressTo:
          # Specify which resources should be present in the search results. In this example,
          # BigQuery.
          operations:
          - methodSelectors:
            - method: '*'
            serviceName: bigquery.googleapis.com
          # Specify project ids under which the search is performed.
          resources:
          - projects/SEARCH_PROJECT_ID
    ingressPolicies:
      - ingressFrom:
          identityType: ANY_USER_ACCOUNT
          sources:
          - accessLevel: '*'
        ingressTo:
          # Specify which resources should be present in the search results. In this example,
          # BigQuery.
          operations:
          - methodSelectors:
            - method: '*'
            serviceName: bigquery.googleapis.com
          # Specify project ids to expose in search results.
          resources:
          - projects/INGRESS_PROJECT_ID
    

For more information about the Identity and Access Management roles that you need to use Knowledge Catalog search, see [Knowledge Catalog IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles).

**Note:** Permissions propagation to search might be delayed if the change affects a large number of resources or principals.

## Isolate search results by environment using VPC Service Controls

To isolate Knowledge Catalog search results between environments like development, test, and production, [configure separate VPC Service Controls perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) for each environment. Assign both the projects that contain the data assets and the projects that are used for performing searches to the corresponding environment's perimeter. Searches that are performed from a project within a specific perimeter only returns results for assets that are located within that same perimeter.

## Recall limitations in search

Knowledge Catalog search optimizes for exploratory discovery instead of exhaustive inventory retrieval, so search queries don't guarantee full recall. A query might omit matching results, and returned results might vary across repeated queries.

### Causes of recall loss

When you search, Knowledge Catalog dynamically checks your permissions against an access control limit of 600 restricts (permission evaluation rules). If your access check exceeds this limit, the system stops checking early to keep searches fast. When that happens, search might leave out matching assets.

You're most likely to hit this limit if any of the following conditions apply:

  * IAM roles assigned directly on hundreds of individual resources.
  * Memberships in many Google Groups that each grant access to individual resources.
  * Memberships in Google Groups that have access granted directly across hundreds of individual resources.



### Resolve recall limitations and missing results

To resolve recall issues or retrieve full metadata, choose the approach that matches your goal:

  * **To fix missing or inconsistent search results:** Reduce your total access checks to stay under the 600-restrict limit. Grant access only to resources you need, and remove access from resources or Google Groups where you don't need permissions. You can also grant roles at the project or folder level instead of on individual resources.
  * **To retrieve a complete, guaranteed metadata inventory:** Do not use search. Instead, [export metadata](https://docs.cloud.google.com/knowledge-catalog/docs/export-metadata) to Cloud Storage and query the full dataset with BigQuery.



## What's next

  * Understand [search syntax for Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-syntax).
  * Learn how to [search for resources](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).
  * Try [Knowledge Catalog use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases).
  * Leverage answering complex natural language queries with the Knowledge Catalog [discovery agent](https://docs.cloud.google.com/knowledge-catalog/docs/use-discovery-agent).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
