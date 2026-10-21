---
url: https://docs.cloud.google.com/knowledge-catalog/docs/import-export-glossaries-entrylinks-overview/
title: About importing and exporting glossaries and entry links \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:02.221340+00:00
---

# About importing and exporting glossaries and entry links  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/import-export-glossaries-entrylinks-overview/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About importing and exporting glossaries and entry links Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you import and export business glossaries and entry links in bulk to manage your business vocabulary at scale. As your catalog grows, bulk operations help you update terms and their relationships without managing them individually in the Google Cloud console.

## Terminology

Knowledge Catalog business glossary lets you define a common business vocabulary and associate those terms with physical data assets. Before working with the import and export utilities, familiarize yourself with the following key components:

  * **Glossary resources:** Consist of categories and terms that establish your business vocabulary.
  * **Entry links:** The relationships or associations between resources, such as between glossary terms and data assets. Knowledge Catalog supports three types of entry links:

    * `definition`: associates a glossary term with a specific data asset (for example, a BigQuery column)
    * `related`: establishes a relationship between two related glossary terms
    * `synonym`: establishes a relationship between two synonymous glossary terms



## Methods for importing and exporting glossaries and entry links

Knowledge Catalog supports two primary methods for bulk glossary management. Choose the method that best aligns with your automation needs and preferred interface:

  * JSON-based metadata import
  * Google Sheets-based utilities for import and export



### JSON-based metadata import

This is the built-in, fully-managed Knowledge Catalog mechanism. You use the Dataplex API to import glossary terms and their associations defined in JSON-formatted metadata files.

**Example use case:** Automatically update your Knowledge Catalog metadata as part of a daily scheduled data pipeline—such as synchronize terms directly from an external enterprise database.

For more information, see [Import glossaries and entry links using JSON files](https://docs.cloud.google.com/knowledge-catalog/docs/import-glossaries-entrylinks-json).

### Google Sheets-based utilities for import and export

This is an open-source, script-based approach provided in the `dataplex-labs` repository. It uses a Python script to sync glossary metadata between a Google Sheet and Knowledge Catalog.

**Example use case:** A data governance team wants to collaboratively draft and review dozens of new business terms with non-technical business stakeholders. The team uses this spreadsheet-based method so everyone can edit, comment on, and approve the terms in Google Sheet before an administrator runs the script to upload them to Knowledge Catalog in bulk.

For more information, see the following documents:

  * [Import business glossaries from a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/import-glossaries-sheets)
  * [Import entry links from a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/import-entrylinks-sheets)
  * [Export business glossaries to a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/export-glossaries-sheets)
  * [Export entry links to a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/export-entrylinks-sheets)



## Common use case: round-trip editing with Google Sheets

A common administrative workflow is to perform round-trip editing. This involves exporting your existing catalog setup, making bulk modifications, and applying those changes back to Knowledge Catalog.

The following workflow illustrates how to execute this process:

  1. Export existing metadata from Knowledge Catalog to Google Sheets.

Use the [glossary export](https://docs.cloud.google.com/knowledge-catalog/docs/export-glossaries-sheets) and [entry links export](https://docs.cloud.google.com/knowledge-catalog/docs/export-entrylinks-sheets) utilities to extract your existing glossary structure and entry links into a Google Sheet.

  2. Modify the metadata within Google Sheets.

Make the required changes in the Google Sheet. Because symmetric links (such as `synonym` and `related` entry links) are simplified to a single direction during export to avoid duplicate rows, you only need to manage them once.

You can add new rows to the respective sheet following the required column schema. You can also modify details such as descriptions or display names directly in the rows.

  3. Stage and import changes from Google Sheets back to Knowledge Catalog.

Run the [glossary import](https://docs.cloud.google.com/knowledge-catalog/docs/import-glossaries-sheets) utility first. This ensures that any new terms or categories are successfully created in the business glossary before you attempt to link them.

Run the [entry links import](https://docs.cloud.google.com/knowledge-catalog/docs/import-entrylinks-sheets) utility. This utility reads your updated associations, stages them in your Cloud Storage bucket, and applies the `definition`, `related`, and `synonym` links to your newly updated glossary.




## What's next

  * Learn more about [managing business glossaries](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries).
  * Learn how to [import business glossaries and entry links using JSON files](https://docs.cloud.google.com/knowledge-catalog/docs/import-glossaries-entrylinks-json).
  * Learn how to [import business glossaries from a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/import-glossaries-sheets).
  * Learn how to [import entry links from a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/import-entrylinks-sheets).
  * Learn how to [export business glossaries to a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/export-glossaries-sheets).
  * Learn how to [export entry links to a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/export-entrylinks-sheets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
