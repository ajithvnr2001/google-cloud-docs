---
url: https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-overview/
title: About data domains \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:20.624706+00:00
---

# About data domains  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-overview/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About data domains Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Data domains in Knowledge Catalog (formerly Dataplex Universal Catalog) let you organize and curate enterprise data resources into a logical hierarchy that reflects your business structure and ownership. You can then manage metadata visibility at scale, capture shared governance context, and scope data discovery to specific business domains.

## Key capabilities of data domains

Data domains decouple logical data organization from the underlying Google Cloud resource hierarchy of folders and projects. Data domains provide the following key capabilities:

  * Define a logical data organization hierarchy aligned with your business processes and logical groupings of data, decoupled from the Google Cloud resource hierarchy of folders and projects.
  * Act as the logical unit of ownership for decentralized domain teams, complementing [data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview).
  * Provide centralized control over who can discover resources and their metadata at scale.
  * Capture common context, such as usage guidance, governance standards, descriptions, and ownership information.
  * Use data domain to narrow search results down to a specific domain. For example, allow the users to search exclusively within the `Marketing` domain for faster, more relevant discovery.
  * Ground AI agents in domain context. The [`lookupContext`](https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context) method returns context for data domains and indicates which data domains a data asset belongs to. For more information, see [Retrieve context for data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-use#retrieve-domain-context).



## Example use case

Consider a global retail enterprise with data assets scattered across departments such as Sales, Supply Chain, and Marketing. Logically similar data assets, such as sales-related tables or datasets, are scattered across multiple Google Cloud projects, making discovery and consistent governance difficult.

The following examples show how various users interact with data domains:

  * **Data domain administrator**

Establishes a logical hierarchy, independent of underlying Google Cloud projects and delegates domain-level governance.

    * Creates top-level domains matching the organizational structure (such as `Sales`, `Supply Chain`, and `Marketing`) and configures subdomains (such as `Online Sales` and `Store Transactions` under `Sales`).
    * Assigns designated data domain owners for each domain (for example, assigning the Sales Lead as the owner of the `Sales` domain).

For more information on how to create a data domain hierarchy and include resources, see [Create data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-manage) and [Include resources in a data domain](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-resources).

  * **Data domain owner**

Defines the content of data domains under their ownership: includes data assets into the domains, defines domain-wide context, and establishes metadata policies over the domains to manage at scale discoverability of the domain's data assets and visibility of its context and metadata. For example, the Sales domain data owner performs the following actions:

    * Includes datasets, tables, and data products scattered across different projects into the `Sales` domain.
    * Defines domain-level aspects, such as data retention standards and cost centers. Defines who can discover the domain's assets and access their context and metadata by granting the required roles and permissions to the `analysts@example.com` group.

For more information on how to manage data domains, see [Manage data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-manage).

  * **Data domain user**

Efficiently discovers relevant, trusted sales assets within a business context without sifting through unrelated enterprise data. For example, to obtain sales data for an upcoming marketing campaign, the data domain user does the following:

    * Explores the domain hierarchy to identify the `Sales` domain.
    * Scopes the search to the domain to find the relevant resources.
    * Inspects the resource metadata, schemas, and usage guidance to evaluate fitness for use.

For more information on how to use data domains to find relevant data, see [Use data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-use).




## Supported assets

You can use data domains for the following assets:

  * Projects
  * Data products
  * BigQuery datasets
  * BigQuery tables
  * Dataform repositories
  * Dataproc Metastore databases
  * Dataproc Metastore tables
  * Spanner databases
  * BigLake tables
  * AlloyDB for PostgreSQL instances
  * Gemini Enterprise Agent Platform datasets



## Data domains and data products

Data domains and data products serve as complementary building blocks you can use to discover and access your data assets. A data domain provides a logical way to organize data assets based on business structure. A data product packages related assets, such as tables or views, into a curated bundle designed to solve specific business use cases.

## Limitations

### Search limitations

When you search for resources outside the domain context, for example when using a global search, the domain's discoverability permissions don't apply. You only see resources that you have access to in the underlying system, such as BigQuery.

Suppose a BigQuery dataset is included in a data domain. You have the `Dataplex Data Domain Entry Reader` role for the domain, but you don't have direct permission to view the dataset in BigQuery:

  * **Searching within the domain:** You see the dataset in your search results because the domain permissions apply.
  * **Searching outside the domain:** You don't see the dataset in your search results. In a general search, domain permissions don't apply, and you don't have direct access in BigQuery.



### Authorization limitations

In the **Preview** launch stage, there is no continuous background IAM synchronization. Domain authorization is verified only when a binding is created. This means that if you revoke the domain principal's IAM role on a resource, that resource isn't automatically unbound or removed from the domain.

## What's next

  * Learn how to [create data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-create).
  * Learn how to [manage data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-manage).
  * Learn how to [include resources in data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-resources).
  * Learn how to [use data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-use).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
