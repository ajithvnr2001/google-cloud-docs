---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-sap-bdc-metadata/
title: Manage SAP BDC metadata in Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:03.873263+00:00
---

# Manage SAP BDC metadata in Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-sap-bdc-metadata/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage SAP BDC metadata in Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Catalog lets you discover, inspect, and manage Core Schema Notation (CSN) metadata for your SAP Business Data Cloud (BDC) data assets. You can use this semantic layer to govern data, search schemas by business context, and ground AI models without accessing the SAP backend system.

## Overview of SAP CSN metadata

Core Schema Notation (CSN) is an open specification format for declaring Cloud Application Programming (CAP) model definitions and domain schemas. When you connect SAP BDC to borderless Lakehouse and share SAP BDC Data Products with Google Cloud, Knowledge Catalog automatically ingests the underlying CSN metadata as system-managed aspects.

This metadata provides a semantic layer over your SAP data assets and includes:

  * Entity descriptions, titles, and labels.
  * Element (column) display names, tech names, and descriptions.
  * Semantic annotations (for example, key indicators, aggregation behaviors, and foreign key relations).



Importing CSN metadata lets data governance teams and AI tools understand the business context and semantic structure of your SAP data without needing direct access to the SAP backend system.

## View SAP CSN metadata in Knowledge Catalog

To view ingested CSN metadata in Knowledge Catalog:

  1. In the Google Cloud console, go to the **Knowledge Catalog** page.

[Go to Knowledge Catalog](https://console.cloud.google.com/dataplex/catalog)

  2. In the search bar, enter your catalog, share, or table name, or search using aspect filters.

  3. Select the SAP table entry from the search results.

  4. Click the **Aspects** tab.

  5. Look for the **SAP CSN Metadata** aspect type to inspect the full CSN schema definitions and annotations for the entry.




## Search and filter by SAP CSN metadata

You can search for SAP assets using CSN metadata filters:

  * To find all assets with CSN metadata, search using aspect type: `aspect:sap-csn-metadata`
  * To search for specific entity titles or element names, enter terms matching the CSN annotations in the search bar.



## Automated AI semantic grounding

Because CSN metadata provides standardized semantic definitions, AI applications and agents built on Google Cloud can consume this metadata to ground models on SAP business definitions. This enables natural language querying over SAP schemas with precise context awareness.

## What's next

  * [About SAP BDC integration](https://docs.cloud.google.com/lakehouse/docs/sap-bdc-overview).
  * [Set up cross-cloud connection for SAP Business Data Cloud](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-sap-bdc).
  * [Query SAP Business Data Cloud data](https://docs.cloud.google.com/lakehouse/docs/query-sap-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
