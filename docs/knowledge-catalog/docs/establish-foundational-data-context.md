---
url: https://docs.cloud.google.com/knowledge-catalog/docs/establish-foundational-data-context/
title: Establish foundational data context with Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:22.085627+00:00
---

# Establish foundational data context with Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/establish-foundational-data-context/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Establish foundational data context with Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

When working with data, you've probably asked questions like "What does this column name mean?", "Who owns this broken dataset?", or "Is this table approved for use?" Metadata tags try to answer these questions, but they quickly become outdated or inconsistent. Knowledge Catalog (formerly Dataplex Universal Catalog) solves this by letting you attach structured metadata and clear business definitions directly to data assets. Providing clear data context [grounds AI agents](https://docs.cloud.google.com/knowledge-catalog/docs/introduction) and builds a foundation of trust for every user who interacts with the data.

This tutorial shows you how to establish data context in Knowledge Catalog. Designed for users such as data stewards and business analysts, this tutorial walks you through UI-based steps to build standard business terms and context before you automate these workflows. The tutorial clarifies relationships between key [Knowledge Catalog concepts](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview). By the end, you'll know how to make your data discoverable and trustworthy.

## Objectives

In this tutorial, you learn how to:

  * Create a single source of truth for business terms with a **business glossary**.
  * Structure and organize metadata with **aspect types**.
  * Attach metadata to data assets with **aspects**.
  * Use Knowledge Catalog Search to find exactly what you need using this new structured metadata.



## Before you begin

Before you begin, do the following:

  * Select a [Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects) for this tutorial.
  * Confirm that [billing is enabled](https://cloud.google.com/billing/docs/how-to/modify-project) for your project.



## Set up your environment

This tutorial uses [Cloud Shell](https://cloud.google.com/shell/docs/), a command-line environment that runs in the cloud.

  1. From the Google Cloud console, click **Activate Cloud Shell** in the top right toolbar. It takes a few moments to provision and connect to the environment.

  2. In Cloud Shell, set your `PROJECT_ID` and `LOCATION` variables so that all future commands target your specific Google Cloud project.
         
         export PROJECT_ID=$(gcloud config get-value project)
         gcloud config set project $PROJECT_ID
         export LOCATION="us-central1"
         

**Note:** Cloud Shell sessions occasionally time out. Before you run shell scripts, you can check your environment variables by running `echo $PROJECT_ID`. If the command returns an empty line, re-run the export commands from this environment setup step. 
  3. Enable the necessary Google Cloud services.
         
         gcloud services enable \
           dataplex.googleapis.com \
           bigquery.googleapis.com 
         




## Create a BigQuery dataset and prepare sample data

Use the following code to create a BigQuery dataset and load some sample CSV transactions into a table. After you create the table, Knowledge Catalog discovers it and creates an _entry_ for it in the catalog.

Think of an entry as Knowledge Catalog's representation of a data asset. It's like a record in the catalog that you can attach metadata to. Instead of adding context to (or _enriching_) the BigQuery table directly, you add it to its entry in Knowledge Catalog.
    
    
    # Create the BigQuery Dataset in the us-central1 region
    bq --location=$LOCATION mk --dataset \
        --description "Sample retail data for foundational data context tutorial" \
        $PROJECT_ID:retail_data
    
    # Create a temporary CSV file with the sample data
    echo "transaction_id,user_email,gmv,transaction_date
    1001,test@example.com,150.50,2025-08-28
    1002,user@example.com,75.00,2025-08-28" > /tmp/transactions.csv
    
    # Load the data from the temporary CSV file into a BigQuery table
    bq load \
        --source_format=CSV \
        --autodetect \
        retail_data.transactions \
        /tmp/transactions.csv
    
    # (Optional) Clean up the temporary file
    rm /tmp/transactions.csv
    

Run a SELECT query to verify your setup:
    
    
    bq query --nouse_legacy_sql "SELECT * FROM retail_data.transactions"
    

Example output:
    
    
    +----------------+------------------+-------+------------------+
    | transaction_id |    user_email    |  gmv  | transaction_date |
    +----------------+------------------+-------+------------------+
    |           1001 | test@example.com | 150.5 |       2025-08-28 |
    |           1002 | user@example.com |  75.0 |       2025-08-28 |
    +----------------+------------------+-------+------------------+
    

**Note:** You don't have to manually register or import the table into Knowledge Catalog. Knowledge Catalog [automatically ingests technical metadata from BigQuery tables](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview#supported-sources) and creates entries.

## Establish common terms with a business glossary

Good data context relies on clear definitions. For example, a developer shouldn't have to guess whether a column named `gmv` means Gross Merchandise Value or whether it includes taxes and returns. A [_business glossary_](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries) creates a single source of truth for these definitions across your organization. When teammates or AI agents analyze your data, they inherit this precise business context. Shared definitions align metrics across teams such as Finance, Sales, and Operations, and help AI agents avoid hallucinations.

Follow these steps to create a glossary and define your first term:

  1. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

  2. Click **Create Business Glossary**.

  3. Enter the following details:

     * **Display name** : `Retail Business Glossary`
     * **Location** : `us-central1 (Iowa)`
  4. Click **Create**.

  5. Click **Create Category**.

  6. Name the category `Sales Metrics`, and click **Create**.

  7. Select the **Sales Metrics** category and click **Add term**.

  8. Name the term `Gross Merchandise Value` and click **Create**.

  9. Click the **Gross Merchandise Value** term to open its details page.

  10. Click **Add** next to **Overview**. Enter the following details: `The total value of merchandise sold over a given period of time before the deduction of any fees or expenses. This is a key indicator of e-commerce business growth.`

  11. Click **Save**.




You have now created a glossary term that you can link to data entries across your organization.

## Define technical metadata with an aspect type

When you use unstructured metadata tags, you often end up with inconsistent catalog entries. For example, one table might be tagged `owner:bob` and another `steward:alice@example.com`. To keep your metadata organized at scale, you need a consistent schema.

That's where [_aspect types_](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata) come in. An aspect type is a metadata blueprint that lets you set clear rules and required fields. Requiring standard fields like valid email addresses for data stewards lets downstream scripts validate and protect your metadata automatically.

Follow these steps to create an aspect type:

  1. In the Google Cloud console, go to the Knowledge Catalog **Aspect types** tab on the **Metadata types** page.

[Go to Aspect types](https://console.cloud.google.com/dataplex/catalog/aspect-types)

  2. On the **Custom** tab, click **Create**.

  3. Enter the following details:

     * **Display name** : `Data Asset Context`
     * **Location** : `us-central1 (Iowa)`
  4. In the **Template** section, click **Add field** to create the following three fields:

     * **Field 1:**

       * **Display name** : `Data Steward`
       * **Type** : `Text`
       * **Is Required** : Select the checkbox.
       * **Text type** : `Plain text`
     * **Field 2** (click **Add field**):

       * **Display name** : `Data Sensitivity`
       * **Type** : `Enum`
       * **Is Required** : Leave optional.
       * **Values** : Add `Public`, `Internal`, and `Confidential`
     * **Field 3** (click **Add field**):

       * **Display name** : `Last Review Date`
       * **Is Required** : Leave optional.
       * **Type** : `Date and time`
  5. Click **Save**.




You now have an aspect type for data governance-related metadata fields like data steward, sensitivity level, and review date. In the next section, you apply this schema to a table entry by attaching an aspect with specific values for these fields.

## Enrich an entry with business and technical context

Column names are often abbreviated or ambiguous. Linking a column to a term in your business glossary provides a clear and consistent definition. In this step, you enrich the entry for the `retail_data.transactions` table by linking the `Gross Merchandise Value` term to a column named `gmv` and attaching an aspect to the table entry using your aspect type.

### Link a column to a business term

To clarify what the `gmv` column in `retail_data.transactions` is, link it to your `Gross Merchandise Value` term.

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search-nl)

  2. Click **Filters** to open the **Filters** panel.

  3. For **Scope** , select **Current Project**.

  4. Search for `retail_data.transactions` and click the returned transactions table.

  5. Click the **Schema** tab.

  6. Select the checkbox next to the `gmv` column, and click **Add business term**.

  7. Select `Gross Merchandise Value`.




### Attach an aspect to the table entry

In addition to linking business terms to columns, you can attach an _aspect_ to a table entry to capture table-level metadata, such as data ownership and sensitivity.

An aspect is an instance of an aspect type, with specific values for metadata fields. When you attach an aspect to an entry, Knowledge Catalog checks the information you provide against the schema defined in the aspect type to ensure consistency.

To define ownership and sensitivity for the `retail_data.transactions` table, attach the `Data Asset Context` aspect:

  1. On the **Details** tab of the `retail_data.transactions` entry page, click **Add** next to **Optional aspects**.
  2. Select `Data Asset Context` from the list.
  3. Enter values in the fields:

     * **Data Steward:** `finance-team@example.com`
     * **Data Sensitivity:** Select **Internal**.
     * **Last Review Date:** Select today's date.
  4. Click **Save**.




By enriching your sample retail transaction data, you've set up a solid foundation of data context in Knowledge Catalog.

## Search for entries using enriched metadata

You can now use Knowledge Catalog Search to find entries based on the business context that you set up. For example, you can find all assets with a specific sensitivity level, or search for your glossary term to discover the underlying tables.

**Tip:** Knowledge Catalog offers two distinct [search experiences](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets) with different syntaxes: **Natural Language** (AI-assisted) and **Keyword** ([structured/exact match](https://docs.cloud.google.com/knowledge-catalog/docs/search-syntax)). This tutorial focuses on **Natural Language**.

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search-nl)

  2. Click **Filters** to open the **Filters** panel.

  3. For **Scope** , select **Current Project**.

  4. In the search bar, enter `Find tables where the Data Asset Context aspect has Internal sensitivity.`

  5. You should see your `retail_data.transactions` table in the list of results.

  6. Clear the search bar and enter `Find tables with the Gross Merchandise Value term attached.`

  7. You should again see the `retail_data.transactions` table in the results, as its `gmv` column is directly linked to this business term.




When you [connect an AI agent to Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/mcp-overview), it inherits this enriched metadata automatically. For example, when you ask an agent to retrieve internal sales metrics, it reads the Data Sensitivity aspect (which you set to Internal) and the linked Gross Merchandise Value glossary term. This shared context helps the agent verify its data sources, respect access policies, and avoid hallucinations.

## Clean up

To avoid incurring charges, delete the resources that you created in this tutorial.

### Delete the sample dataset

To delete the sample BigQuery dataset and all its tables, use the following command. This action is irreversible.

**Warning:** This recursive delete command does not ask for confirmation. To prevent accidental data loss from incorrect environment variables, verify your project ID and dataset name before you run it.
    
    
    # Re-run these exports if your Cloud Shell session timed out
    export PROJECT_ID=$(gcloud config get-value project)
    
    # Manually type this command to confirm you are deleting the correct dataset
    bq rm -r -f --dataset $PROJECT_ID:retail_data
    

### Delete Knowledge Catalog artifacts

  1. In the Google Cloud console, go to the Knowledge Catalog **Aspect types** tab on the **Metadata types** page.

[Go to Aspect types](https://console.cloud.google.com/dataplex/catalog/aspect-types)

  2. Select the `Data Asset Context` aspect type and click **Delete**.

  3. In the Google Cloud console, go to the Knowledge Catalog **Glossaries** page.

[Go to Glossaries](https://console.cloud.google.com/dataplex/dp-glossaries)

**Note:** You must delete all terms and categories before you can delete the glossary itself.
  4. Select the `Gross Merchandise Value` term and click **Delete**.

  5. Select the `Sales Metrics` category and click **Delete**.

  6. Select the `Retail Business Glossary` and click **Delete**.




## What's next

To learn more about catalog curation and building agents with Knowledge Catalog, see the following resources:

  * **Manage aspects and enrich metadata:** Learn how to define custom schemas and attach structured metadata in [Manage aspects and enrich metadata](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata).
  * **Manage business glossaries:** Learn how to establish a standardized vocabulary for your organization in [Manage a business glossary](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries).
  * **Govern with Terraform:** Learn how to provision custom aspect types and glossaries using [Terraform](https://docs.cloud.google.com/knowledge-catalog/docs/terraform).
  * **Work with glossary terms at scale:** Perform bulk metadata enrichment using JSON files in [About importing and exporting glossaries and entry links](https://docs.cloud.google.com/knowledge-catalog/docs/import-export-glossaries-entrylinks-overview).
  * **Enrich metadata with agents:** Build an AI agent to extract context and enrich your data assets in [Build an agent to enrich your metadata](https://docs.cloud.google.com/knowledge-catalog/docs/build-agent-to-enrich-metadata).
  * **Explore more use cases:** Discover additional customizable workflows and scenarios in [Use cases](https://docs.cloud.google.com/knowledge-catalog/docs/use-cases).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
