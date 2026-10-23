---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview/
title: Enterprise Knowledge Graph overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:42.476805+00:00
---

# Enterprise Knowledge Graph overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Guides ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview)



Send feedback 

#  Enterprise Knowledge Graph overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this product as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Enterprise Knowledge Graph organizes siloed information into organizational knowledge, which involves consolidating, standardizing, and reconciling data in an efficient and useful way.

## Entity Reconciliation API

Entity Reconciliation API is a lightweight, AI-powered, semantic clustering and deduplication service for tabular data. It is a standalone API that wraps around the Google core entity resolution engine. It helps customers to reconcile and join their data together, or to join their data with one or multiple third-party datasets.

Key features include:

  * State-of-the-art quality pretrained model with Google data.
  * Built-in entity enrichment, including geocoding.
  * Google-scale clustering and reconciliation that handles a graph with a size up to billions of nodes and trillions of edges.
  * Stable Machine ID (MID) is a unique identifier for each of the entity clusters.
  * Natively support up to 10 BigQuery tables.



### How does it work

![Enterprise Knowledge Graph concept](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/ekg-recon-api-concept.png)

In relational databases, matching is primarily done through tightly managed keys, for example, customer IDs. Some support fuzzy matching, for example, "Robert Smith" versus "Bob Smith". In Graphs, matching occurs through the use of any combination of fuzzy text, common relationships, entity types, and its attributes. This works well when joining data across a heterogeneous mix of systems.

The Entity Reconciliation API reads data from source BigQuery tables given a set of entity types and files mapped to common schema. Then it performs knowledge extraction to turn the input relational data into [RDF triples](https://en.wikipedia.org/wiki/Semantic_triple) like a knowledge graph representation. The Google Entity Reconciliation engine then builds a graph to cluster entities into different groups (entities in the same group are considered as matched). The last step is to output the linking result (matched and not-matched) to the customer-specified BigQuery tables in the form of a new unique identifier column (MID).

## Google Knowledge Graph Search API

Search by keyword or lookup entities with an ID in the Google Knowledge Graph uses the Google Knowledge Graph Search API. The API uses standard `schema.org` types and is compliant with the JSON-LD specification.

Use the API to do the following:

  * Perform entity resolution on an organization, a product, a location, a book, a movie, and many more entities.
  * Link your private entity to a globally unique Cloud Knowledge Graph machine ID (MID).
  * Get a ranked list of the most notable entities that match certain criteria.
  * Annotate and organize content using the Google Knowledge Graph entities.
  * Connect to the broader data ecosystem with additional IDs returned by the Google Knowledge Graph Search API, such as Google Place ID.
  * Search for entities from MIDs returned by other Google Cloud APIs, such as [Cloud Vision API](https://cloud.google.com/vision), [Cloud Natural Language API](https://cloud.google.com/natural-language) and [Cloud Video Intelligence API](https://cloud.google.com/video-intelligence)



### Google Knowledge Graph Search API editions

Google Knowledge Graph Search API offers two editions:

  * `Basic`
  * `Advanced`



Both editions support entity search and lookup. They also serve the same base knowledge graph entities built by Google Cloud. The Enterprise edition includes additional features such as linking to Google Place ID and additional data coverage.

If you're planning a new project, build your application with Cloud Knowledge Graph [Advanced edition](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/editions#-_advanced) to take advantage of new features and service improvements. The [Basic edition](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/editions#-_basic) remains available, but doesn't support new features, high QPS, or additional security and compliance standards. 

For a comparison between the two editions, see [Compare Basic and Advanced editions](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/editions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
