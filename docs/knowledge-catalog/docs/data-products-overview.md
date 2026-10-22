---
url: https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview/
title: About data products \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:26.975995+00:00
---

# About data products  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About data products Stay organized with collections  Save and categorize content based on your preferences. 

Data products in Knowledge Catalog (formerly Dataplex Universal Catalog) let you package related catalog assets into a single, curated unit to solve specific business problems. You can then add context and contracts to help data consumers discover, evaluate, and request self-service access to trusted data.

## Key capabilities

Data products provide the following key capabilities:

  * Organize catalog assets into a logical unit that solves a specific business problem and speeds up time to insights.
  * Distribute data assets with context that includes a description, documentation, and aspects.
  * Establish trust with contracts that let data producers provide assurance to data consumers.
  * Provide a self-service workflow for data consumers to evaluate data products and get access to data.



## Key concepts

This section describes the key concepts and terminologies related to data products.

### Data product

A curated, logical grouping of data assets, formally packaged to be discoverable, trusted, and accessible for solving specific business problems.

### Asset

A pointer to a physical data resource, such as a BigQuery dataset, table, or view. A data product contains one or more assets.

### Access group

Access groups simplify permission management for your data product. They map user-friendly roles (such as `Reader` or `Analyst`) to underlying Google Groups or service accounts. This abstraction enables data product owners to manage access at a conceptual level, and helps data product consumers request the appropriate level of access.

  * Data product owners configure access groups and can optionally assign a default IAM role, which is automatically applied to all supported assets in the data product. If a default role isn't assigned, owners can assign specific IAM roles to assets directly.

  * Data product consumers use these groups to request access to the data product.




### Data product owner or data producer

The individual or team responsible for the creation and management of data products. This includes managing quality, access, and documentation.

### Data product consumer

The individual, team, or AI agent that consumes data products to generate insights.

### Contract

An agreement between the data product owner and its consumers. This agreement sets clear expectations by defining specific terms for how the data will be provided and used, such as its refresh schedule and quality standards.

## Example use case

Consider a data scientist analyzing an ecommerce business. Their goal is to find the average order value (AOV) by traffic source and see if there's a correlation between user age and order size. To do this, they need to combine data from multiple tables, such as `order_details`, `user_traffic`, and `user_demographics`.

In a conventional setup, this process creates friction. To generate insights, the data scientist must first discover the correct tables within the organization's vast data landscape, then contact each data owner, justify their access request, and wait for approval.

With data products, data owners can streamline this experience by packaging the relevant assets into a single product named "Ecommerce Business Data". This package includes the following:

  * Assets

    * BigQuery tables `order_details` and `user_traffic` (containing historical order data and traffic sources)
    * BigQuery view `user_demographics` (providing user details with PII excluded)
  * Access groups

    * Predefined `Reader` and `Writer` groups to streamline access requests
  * Contract

    * A contract defining the data refresh frequency (for example, weekly at 8:00 AM PST)
  * Context

    * Documentation with sample queries and other details
    * Additional metadata to depict data sensitivity



Data scientists can now discover this data product as a single logical unit. This lets them confidently generate insights to answer questions like, 'What is the average order value for each traffic source?'—ultimately revealing which sources generate the highest value customers.

## Data product user flow

The data product lifecycle in Knowledge Catalog involves two key user journeys: one for the data product owner (or producer) who creates and manages the data, and one for the data product consumer who discovers and uses it.

### Data product owner journey

This journey focuses on packaging, securing, and governing the data products to ensure it's trusted and accessible.

  * Create: Define the data product and include assets. This involves the following actions:

    * Configure the unique name, project, region, and description.
    * Add assets such as BigQuery tables, datasets, or views.
    * Configure access groups (for example, `Analyst` or `Reader`) and map them to underlying Google Groups or service accounts to simplify permission management.
    * Optionally, assign a default IAM role to an access group to automatically grant permissions across all supported assets in the data product.
    * Assign the necessary IAM roles to these access groups for the specific assets.
    * Add a contract (a system aspect) to formally communicate the agreed-upon data refresh cadence, frequency, and threshold.

For more information, see [Create data products](https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products).

  * Manage: Update the data product and ensure discoverability. This involves the following actions:

    * Update basic details, assets, permissions, and supplementary aspects (metadata), and rich text documentation.
    * Grant access to consumers to discover and request access to data products.

For more information, see [Manage data products](https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-products).




### Data product consumer journey

This journey focuses on quickly finding trusted data and gaining the necessary permissions to use it.

  * Discover: Find relevant, trusted data for a specific business problem. This involves the following actions:

    * Use the [Knowledge Catalog Search](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets) with keywords or natural language to find the packaged data product.
    * Review the data product's overview, assets, contract, and other aspects to determine its fitness for use.

For more information, see [Search for data products](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products#search).

  * Request access: Ask the data product owner for permission to access the data.

For more information, see [Request access to data products](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products#request-access).

  * Use: Access the underlying assets to generate insights. This involves the following action:

    * Upon approval, you can access the product and its assets. For example, if the asset is a BigQuery table, you can navigate to the BigQuery studio and query the data directly.

    * For applications and development workflows operating outside of Google Cloud, you can expose the data product using an external metadata gateway. For more information, see [Use the Knowledge Catalog remote MCP server](https://docs.cloud.google.com/knowledge-catalog/docs/use-remote-mcp).

For more information, see [Consume data products](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products#consume-data-products).




## Assets supported

A data product can be composed of one or more data assets. The following data assets are supported:

  * BigQuery datasets
  * BigQuery tables
  * BigQuery views
  * BigQuery routines
  * BigQuery models
  * BigQuery external tables
  * Gemini Enterprise Agent Platform datasets
  * Gemini Enterprise Agent Platform models
  * Cloud Storage buckets
  * Iceberg REST Catalog catalogs
  * Iceberg REST Catalog namespaces
  * Iceberg REST Catalog tables
  * Looker (Google Cloud core) dashboards
  * Looker (Google Cloud core) dashboard elements
  * Looker (Google Cloud core) Looks
  * Looker (Google Cloud core) Explores
  * Looker (Google Cloud core) LookML projects
  * Looker (Google Cloud core) LookML models
  * Looker (Google Cloud core) LookML views



## Limitations

  * Location: Data products and their underlying assets must reside in the same Google Cloud location.
  * BigQuery models: Access to BigQuery models within a data product is managed through [IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) applied to the parent dataset's IAM policy. Sharing BigQuery models is subject to the [limitations of IAM conditions](https://docs.cloud.google.com/iam/quotas#limits).
  * Looker (Google Cloud core) assets: Using Looker (Google Cloud core) assets in data products has the following limitations:

    * Service accounts aren't supported: [Google Group mirroring](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#mirroring) in Looker (Google Cloud core) only supports human user identities. Access groups configured on Looker (Google Cloud core) assets can't include a service account principal.
    * Default access group IAM roles aren't supported: Default IAM roles assigned at the access group level aren't applied to Looker (Google Cloud core) assets and are marked as `unsupported`. You must explicitly configure access group permissions on each Looker (Google Cloud core) asset.
    * Manual permission synchronization inside Looker (Google Cloud core): Role names configured on a Looker (Google Cloud core) asset in a data product are informational placeholders for consumers. Data producers must manually configure and maintain [folder access levels](https://docs.cloud.google.com/looker/docs/admin-panel-users-content-access#access_levels) and [Looker roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) for the mirrored group inside the Looker (Google Cloud core) instance.
  * Quotas and limits: For a complete list of API rate limits and capacity quotas, see [Quotas for data products API requests](https://docs.cloud.google.com/knowledge-catalog/docs/quotas#data-product-quotas).

  * [Zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) aren't supported.




## What's next

  * Learn how to [create a data product](https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products).
  * Learn more about [managing data products](https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-products).
  * Learn how to [search for data products](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products#search).
  * Learn how to [request access for data products](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products#request-access).
  * Learn how to [use VPC Service Controls with data products](https://docs.cloud.google.com/knowledge-catalog/docs/vpcsc-data-products).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
