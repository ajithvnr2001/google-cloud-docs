---
url: https://docs.cloud.google.com/knowledge-catalog/docs/context-sets/
title: Context sets overview \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:41.332896+00:00
---

# Context sets overview  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/context-sets/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Context sets overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Knowledge Studio gated preview**  
Knowledge Studio is currently available as a gated preview. To view the context graph, create context sets, and run enrichment workflows, you must first request allowance for your organization.   
  
[Request preview access](https://docs.google.com/forms/d/e/1FAIpQLScw1O38BmcLIvqL1ZvpybJsLGO_Dmuq0a5RrCJIqW11iljsKQ/viewform)

Knowledge Catalog context sets let you package data schemas, semantic definitions, and validated query patterns into bounded, domain-specific knowledge containers. This targeted domain knowledge reliably grounds autonomous AI applications such as Gemini Enterprise and custom agents so they can operate with high precision.

This document is for data architects, governance leads, and AI engineers who want to understand how context sets structure domain knowledge for AI agents.

## What is a context set?

A _context set_ is a specialized Knowledge Catalog **entry group** (a logical container for metadata records) that packages a self-contained collection of semantic information and data asset references for specific analytical domains and AI agents.

Inside this container, knowledge is organized into **entries** , which represent individual business concepts, documents, or data assets. These entries are enriched with **aspects** , which are modular metadata attributes that store specific details like business terms, SQL templates, and Markdown documentation.

Rather than forcing agents to search an entire enterprise catalog, which introduces latency, wastes prompt tokens, and risks hallucinated answers, context sets establish hermetic, domain-scoped knowledge containers that agents can consult with high precision.

Because context sets act as administrative containers, you can organize metadata by project ownership and apply Identity and Access Management (IAM) access control policies across all bundled entries at once without configuring permissions individually. For more information about entry groups, entries, and aspects, see [About metadata management](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).

## AI agent grounding requirements

As organizations deploy autonomous AI agents (such as Gemini Enterprise, Antigravity, and custom Agent Development Kit agents) to orchestrate data workflows and generate analytics, agents require reliable grounding:

  * **Semantic definitions** : What does a specific column or metric mean in business terms?
  * **Validated query patterns** : How have domain experts successfully queried and joined these tables?
  * **Operational rules** : What business policies, exception criteria, and standard operating procedures (SOPs) govern this data?



## Recommended context set naming patterns

The following architecture diagram illustrates how the four core logical naming naming conventions operate together within the entry group boundary to ground downstream AI applications:

![The four naming conventions within a context set boundary that restrict AI agent searches.](https://docs.cloud.google.com/static/knowledge-catalog/images/context-set-architecture.svg)**Figure 1.** The four curated naming conventions within a context set entry group boundary.

While a context set doesn't strictly require every type of entry to function, we recommend organizing your entries using the following logical naming naming conventions. Using these naming conventions helps ensure humans and autonomous agents can consistently discover and interpret knowledge:

Naming pattern | Entry type | Description and purpose | Attached aspects  
---|---|---|---  
Business concepts `concepts_<id>` | `generic` | Business glossary terms, metric definitions, acronyms, and calculation formulas. | `glossary-term-aspect`, `contacts`.  
Documents `documents_<path>` | `document` | Narrative context, standard operating procedures (SOPs), onboarding wikis, and pointers to external documentation. | `Document`, `overview` (rich text Markdown and links).  
Query templates `query-templates_<path>` | `query-template` | Pre-validated, parameterized SQL query templates, high-frequency join logic, and execution patterns. | `query-template` (includes fields such as sources, intent, nlQuery, parameters, and query).  
Semantic models `semantic-models_<id>` | `semantic-model`, `semantic-entity`, `semantic-metric` | Formal relational models, entity definitions, dimensional hierarchies, and measures. | `semantic-model`, `semantic-entity`, `semantic-metric`.  
  
### Business concepts

A business concept entry (Entry of type generic using the `concepts_*` naming convention) defines standardized business terminology, domain metrics, acronyms, and calculation formulas (`glossary-term-aspect`).

Key capabilities include:

  * **Terminology alignment** : Eliminates terminology ambiguity across business units and analytical teams.
  * **KPI formulas** : Provides mathematical formulas and logic for domain-specific key performance indicators (KPIs).
  * **Organizational ownership** : Establishes clear organizational ownership through attached governance aspects (`contacts`).



For example, within an ecommerce context set, an entry at `concepts_net_items_sold` specifies the exact net units sold calculation. When an agent receives a prompt asking for "net items sold," it consults the concept entry to apply the verified calculation rather than inventing SQL logic.

**Example resource representation:**
    
    
    name: projects/cymbal-style/locations/us-central1/entryGroups/online-apparel-store/entries/concepts_net_items_sold
    entryType: generic
    aspects:
      dataplex-types.global.glossary-term-aspect:
        definition: "Calculates the absolute number of items sold minus customer returns in a given time period."
    

### Documents

A document entry (Entry of type document using the `documents_*` naming convention) stores narrative and procedural context in structured Markdown (`Document`, `overview`).

Key capabilities include:

  * **Standard operating procedures (SOPs)** : Captures SOPs, runbook checklists, and onboarding guides directly within the catalog.
  * **Compliance policies** : Documents compliance policies, regulatory constraints (such as GDPR or HIPAA handling rules), and exception criteria.
  * **External reference wikis** : References external living wikis (such as Google documents, Atlassian Confluence, Notion, or GitHub) through source URI pointers (`overview` links).



For example, an apparel context set includes `documents_return_policy_rules` to instruct agents on how to exclude finalized sales and damaged-in-transit items when calculating standard return rates.

**Example resource representation:**
    
    
    name: projects/cymbal-style/locations/us-central1/entryGroups/online-apparel-store/entries/documents_return_policy_rules
    entryType: document
    aspects:
      dataplex-types.global.overview:
        content: "## Return Policy Rules\nItems marked FINAL_SALE or DAMAGED_IN_TRANSIT are excluded from return rates..."
    

### Query templates

A query template entry (Entry of type `query-template` using the `query-templates_*` naming convention) contains human-verified, parameterized SQL queries mapped to common natural language analytical intents (using the `query-template` aspect).

Key capabilities include:

  * **Pre-validated queries** : Stores pre-validated join paths, filter conditions, and aggregation patterns for high-frequency business questions.
  * **Runtime parameterization** : Supports runtime parameter substitution (such as `@start_date`, `@region`, and `@limit`) for dynamic agent execution.
  * **Error prevention** : Prevents hallucinated table joins and SQL dialect syntax errors.



For example, when an agent needs to answer a question about top-performing accounts, it matches `query-templates_sales_top_accounts_by_arr` and substitutes the requested date range into the verified SQL template.

**Example resource representation:**
    
    
    name: projects/cymbal-style/locations/us-central1/entryGroups/online-apparel-store/entries/query-templates_top_categories_by_season
    entryType: query-template
    aspects:
      dataplex-types.global.query-template:
        intent: "Which e-commerce product categories performed best this season?"
        query: "SELECT category, SUM(revenue) FROM sales WHERE season = @season GROUP BY category ORDER BY 2 DESC LIMIT @limit"
        parameters:
          -   name: "season"
            type: "STRING"
          -   name: "limit"
            type: "INTEGER"
    

### Semantic models

Semantic model entries (using the `semantic-model`, `semantic-entity`, and `semantic-metric` entry types using the `semantic-models_*` naming convention) formalize relational structures, dimensional hierarchies, and aggregation measures across normalized tables.

Key capabilities include:

  * **Relational definition** : Defines primary keys, foreign keys, and join cardinalities (such as one-to-many or many-to-many relationships).

  * **Business dimension mapping** : Maps raw underlying columns to business dimensions, time grains, and reusable measures.

  * **Agent guidance** : Guides autonomous agents when assembling complex, multi-table analytical queries when no exact query template exists.

  * **Abstracting underlying complexity** : Unlike raw schema-join entry links that only document mechanical table connections in the source dataset, semantic models operate at the logical business layer to prevent the AI agent from hallucinating incorrect ER diagram traversals.




For example, an apparel context set uses `semantic-models_apparel_sales_model` to define how `warehouses`, `shipments`, and `line_items` join across star-schema fact and dimension tables.

**Example resource representation:**
    
    
    name: projects/cymbal-style/locations/us-central1/entryGroups/online-apparel-store/entries/semantic-models_apparel_sales_model
    entryType: semantic-model
    aspects:
      dataplex-types.global.semantic-model:
        entities:
          -   name: "products"
          -   name: "orders"
        relationships:
          -   sourceEntity: "orders"
            foreignKey: "product_id"
            targetEntity: "products"
            primaryKey: "id"
            type: "MANY_TO_ONE"
    

## Example: Online clothing store context set

To show how the four naming conventions work together, consider an online clothing retailer deploying an AI assistant for store merchandisers. Without bounded context, the agent might query raw staging tables or miscount popular items by not subtracting customer returns.

To ground the agent, a data steward creates a context set named `online-apparel-store`:
    
    
    EntryGroup: projects/cymbal-style/locations/us-central1/entryGroups/online-apparel-store
    (EntryGroup.type = "context-set")
    │
    ├── concepts_* (Business concepts)
    │   ├── concepts_net_items_sold
    │   │     Formula: SUM(orders.quantity) - SUM(returns.quantity)
    │   └── concepts_bestseller
    │         Definition: Any clothing item with >= 500 net units sold within a 30-day window
    │
    ├── documents_* (Documents and SOPs)
    │   ├── documents_return_policy_rules
    │   │     Markdown SOP: Exclude items marked 'FINAL_SALE' or 'DAMAGED_IN_TRANSIT' from standard return rates
    │   └── documents_size_chart_guide
    │         Markdown guide: Sizing conversions across US, UK, and EU clothing labels
    │
    ├── query-templates_* (Golden SQL queries)
    │   └── query-templates_top_categories_by_season
    │         Verified SQL template with parameters: @season, @limit
    │
    └── semantic-models_* (Semantic models)
        └── semantic-models_apparel_sales_model
              Join keys: orders.product_id = products.product_id (many-to-one)
                         orders.order_id = returns.order_id (one-to-many)
    

**Note:** Unlike other entry link types, `entryLinkTypes/context` links are created automatically based on the context aspect attached to the target asset.

### How an agent resolves a prompt

When a merchandiser asks the agent, _"What were our top 5 bestselling winter jacket styles, excluding damaged returns?"_ , the agent resolves the prompt through the context set:

  1. **Query template lookup** : The agent checks `query-templates_*` and matches `query-templates_top_categories_by_season`, substituting `@season = 'Winter'` and `@limit = 5`.

  2. **Concept verification** : The agent inspects `concepts_net_items_sold` and `concepts_bestseller` to confirm that returned items must be subtracted from total order quantities.

  3. **SOP rule enforcement** : The agent reads `documents_return_policy_rules` and adds the filter condition `WHERE return_reason != 'DAMAGED_IN_TRANSIT'`.

  4. **Schema and join validation** : Using `semantic-models_apparel_sales_model` and the linked `@bigquery` tables, the agent joins `store.orders`, `store.products`, and `store.returns` using verified foreign keys and runs the SQL query.




## Architectural capabilities

Context sets provide several core capabilities for enterprise data environments:

  * **Hermetic execution boundaries** : By bounding context to a curated set of assets and semantic entries, agents operate within a hermetic sandbox. This eliminates extraneous catalog noise, helps ensure deterministic evaluations, and minimizes token usage.

  * **Fast upload and bulk indexing** : Teams can upload and index sets of concepts, queries, and documents as a single atomic operation, which lets you integrate with continuous integration and deployment (CI/CD) pipelines.

  * **Zero-copy packaging** : Context sets package metadata and relationships without copying or moving underlying data storage, avoiding redundant storage costs and data synchronization lag.




## Agent consultation patterns

Downstream agents consume context sets through the Model Context Protocol (MCP) or direct Knowledge Catalog APIs. For more information, see [Retrieve data context with the Catalog APIs](https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context). To optimize response latency and minimize token consumption, agents follow a three-tier consultation hierarchy:

  1. **Query template matching** : The agent searches `query-templates_*`. If a verified template matches the user's intent, the agent parameterizes the query and runs it directly. This provides the fastest response with near-zero risk of query error.

  2. **Semantic model assembly** : If no query template matches, the agent evaluates `semantic-models_*` to understand entity relationships and construct a multi-table SQL statement.

  3. **Document and concept consultation** : For ambiguous edge cases (such as fiscal calendar cutoffs or dispute exclusions), the agent reads `concepts_*` and `documents_*` to apply business rules.




## Consuming context in generative AI applications

Generative AI applications use curated context sets to understand enterprise domain semantics, navigate complex schemas, and generate reliable SQL without hallucinations. Applications typically consume these context sets through two primary patterns:

  * **Dynamic context discovery** : In conversational or self-service analytics environments, users ask ad hoc questions in natural language. The application dynamically evaluates the user's intent to identify and retrieve the most relevant context set from Knowledge Catalog, injecting the retrieved domain knowledge into the active prompt.

  * **Pre-configured context sets** : For dedicated agent applications, you can pre-configure the agent with an explicit context set reference by supplying its resource URI. Binding a dedicated context set provides deterministic grounding, guaranteeing that all interactions use certified business definitions without runtime search overhead. The agent automatically inherits quality improvements as recurring enrichment workflows refine the context set over time.

To optimize these enrichment and self-learning capabilities, we recommend specifying a Gemini 3.8 Flash or later model in the Gemini Enterprise application. For more information about the model selection steps, see the "Create an agent using the flow builder" section in [Design agents in Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/design-agents).




## How context sets compare to related constructs

To choose the right metadata construct for your architecture, read how Knowledge Catalog context sets compare to related platform capabilities.

### Context sets compared to context graphs

The context graph and context sets are two separate constructs with distinct roles in the Knowledge Studio architecture:

  * **Context graph** : The live, comprehensive semantic topology across your organization. It links underlying data assets, business glossary terms, and interaction traces. You explore and traverse this open graph interactively in the [Explore interface](https://docs.cloud.google.com/knowledge-catalog/docs/explore-data-assets).

  * **Context set** : A bounded, regional, and curated packaging unit. It extracts and hermetically packages a specific subset of domain knowledge into an entry group (`type="context-set"`) for downstream AI agents to query through the [Model Context Protocol (MCP)](https://docs.cloud.google.com/knowledge-catalog/docs/mcp-overview). A context set acts as a cohesive, high-density sub-graph within the broader context graph.




### Knowledge Catalog context sets compared to database context sets

Both Knowledge Catalog and Google Cloud operational databases use the term _context set_ to refer to curated information that grounds generative AI models.

While both variations share the same underlying architecture—they are stored natively as Knowledge Catalog context sets (extensible entry groups with `type="context-set"`) and use standard Knowledge Catalog APIs they target different layers of the enterprise data stack:

  * **Database context sets (QueryData)** : Built to serve operational, transactional databases (such as AlloyDB for PostgreSQL, Cloud SQL, and Spanner). These context sets are heavily optimized for SQL configurations. They bundle golden query templates, schema metadata, and filtering facets that a dedicated context engineering agent evaluates to improve natural language-to-SQL (NL2SQL) translation in operational runtimes.
  * **Knowledge Catalog context sets (Knowledge Studio)** : Built to serve analytical data estates (such as BigQuery, data lake houses, and Knowledge Catalog data products). These context sets package broader, multi-modal knowledge across multiple naming conventions, including business concepts, Markdown documentation wikis, and semantic models. They are curated using Knowledge Studio enrichment workflows and served to downstream analytical agents through the Model Context Protocol (MCP).



### Context sets compared to data products

Understanding how context sets interact with Knowledge Catalog [data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview) helps you establish clear data and AI governance boundaries:

  * **Data products manage the underlying resources:** Data products securely bundle concrete resources like BigQuery tables, buckets, and streams, establishing a primary unit for data sharing, data contracts, and data-plane access control.

  * **Context sets bundle conversational semantics:** Context sets do not grant data access; instead, they bundle domain knowledge such as concepts, query templates, and documents required by AI agents and humans to understand the data. Data stewards can link a context set to a data product by declaring it in the product's `additional_context` references.




## Enterprise security and governance

Context sets integrate with Google Cloud security and governance controls to help protect sensitive enterprise metadata:

  * **Context set IAM roles** : Because context sets often contain sensitive semantic information, access is governed by IAM roles applied directly to the `context-set` entry group. This lets you organize curated knowledge by geographic region and domain ownership, granting modification permissions to domain stewards and read permissions to consuming AI agents. To create a context set, you must have the `dataplex.entryGroups.setIamPolicy` IAM permission. This permission is required to automatically grant you owner permissions during context set creation. You can get this permission through predefined roles such as the **Dataplex Catalog Admin** (`roles/dataplex.catalogAdmin`) or **Dataplex Entry Group Owner** (`roles/dataplex.entryGroupOwner`) roles.

  * **Zero-copy underlying data security** : Granting an agent access to a context set lets the agent read semantic metadata and query templates, but it doesn't bypass access controls on underlying tables. To run a SQL query against BigQuery or read files in Cloud Storage, the identity running the query must hold the required data-plane IAM permissions on those underlying resources.

  * **Human-in-the-loop governance** : When autonomous Knowledge Studio enrichment tasks extract new concepts, SOPs, or query templates from operational logs, the proposals are staged as reviewable change requests. Data stewards inspect diff comparisons and evaluation scores before approving changes to a production context set. For more information about proposal review, see [Manage requests](https://docs.cloud.google.com/knowledge-catalog/docs/manage-requests).

  * **User-managed execution identity** : Automated enrichment tasks that populate context sets run under a user-managed service account impersonated by the Dataplex Service Agent through the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




## Preview scope and boundaries

During Preview, context sets operate within the following boundaries:

  * **Regional scope** : Global context sets linked to regional data assets are not supported. A context set must align with the regional boundaries of the assets it packages.

  * **Authoring and consumption interfaces** : You can create context sets through the Knowledge Studio container in the Google Cloud console, keeping them logically distinct from standard Knowledge Catalog administrative entry groups. You can populate context sets automatically through Knowledge Studio enrichment workflows. Downstream AI agents can discover and query context sets programmatically by using the Knowledge Catalog APIs (`ListEntries` and `LookupEntry`) and the Model Context Protocol (MCP). For more information, see [About MCP servers](https://docs.cloud.google.com/knowledge-catalog/docs/mcp-overview).

  * **Billing** : Knowledge Catalog doesn't charge a separate standalone SKU for creating context set entry groups.

  * **Shared quotas** : Because context sets are fundamentally specialized entry groups (`type="context-set"`), they consume and share the same resource quotas as standard Knowledge Catalog entry groups.




## What's next

Concept 

###  [ Knowledge Studio overview ](https://docs.cloud.google.com/knowledge-catalog/docs/knowledge-studio)

Learn how to orchestrate rich data context, build context sets, and ground AI agents using Knowledge Studio interfaces. 

Task 

###  [ Explore data assets and the context graph ](https://docs.cloud.google.com/knowledge-catalog/docs/explore-data-assets)

Use the visual canvas in Knowledge Studio to chat with your data and trace semantic relationships. 

Concept 

###  [ About metadata management ](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview)

Understand how entries, entry groups, and aspects form the structural foundation of context sets. 

Concept 

###  [ About MCP servers ](https://docs.cloud.google.com/knowledge-catalog/docs/mcp-overview)

Expose context sets and rich metadata to downstream generative AI agents using MCP. 

Task 

###  [ Retrieve data context with the Catalog APIs ](https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context)

Programmatically discover and retrieve context sets for generative AI reasoning using the `ListEntries` and `LookupEntry` APIs. 

Task 

###  [ Manage context sets ](https://docs.cloud.google.com/knowledge-catalog/docs/manage-context-sets)

Learn how to create, view, edit, and delete context sets in the to organize domain knowledge. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
