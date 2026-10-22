---
url: https://docs.cloud.google.com/knowledge-catalog/docs/multi-region-lineage-overview/
title: About multi-region lineage search \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:19.985210+00:00
---

# About multi-region lineage search  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/multi-region-lineage-overview/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About multi-region lineage search Stay organized with collections  Save and categorize content based on your preferences. 

When you manage data across a complex organization, understanding your data lineage is essential for good data governance and effective cloud data management. This guide explains how to use multi-region search in Knowledge Catalog (formerly Dataplex Universal Catalog) to track your data across geographic boundaries.

By default, data lineage in Knowledge Catalog is a regional service. Whenever your data moves or transforms, the resulting lineage data such as links, processes, and events, is stored in the specific region where that action took place.

However, real-world data pipelines frequently span multiple Google Cloud projects and regions. For example, you might have a BigQuery table in `us-central1` that copies data to a storage bucket in `europe-west1`. To trace your data assets across these boundaries and build complete lineage graphs, you need to perform a multi-region search.

Knowledge Catalog gives you two ways to discover and connect these cross-regional lineage graphs:

  * The server-side automation method that uses the [`searchLineageStreaming`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLineageStreaming) API (Preview)—Recommended
  * The client-side fan-out method that uses the [`searchLinks`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks) API



## Core concepts of multi-region lineage search

To understand multi-region lineage discovery, it helps to understand how the system handles graph traversal:

  * Root criteria: The starting point of your lineage search, defined by one or more asset names (such as a BigQuery table or a Pub/Sub topic) or fine-grained column fields.

  * Direction: The orientation of the graph traversal relative to the root criteria. You can search upstream (to see where your data came from) or downstream (to see where your data is going).

  * Breadth-first search: The architectural mechanism used to find connected nodes. The search traverses the lineage graph layer by layer, accurately calculating the execution depth of each connected asset across regional boundaries.




## How do the multi-region search methods compare?

While both methods let you to piece together a cross-regional view of your data, they handle the heavy lifting differently:

Feature | Server-side automation  
[searchLineageStreaming API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLineageStreaming) | Client-side fan-out  
[searchLinks API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/searchLinks)  
---|---|---  
Execution model | Server-side automation: The Google Cloud routing engine traverses multiple regions natively. | Client-side orchestration: Your application script must manually loop and manage requests.  
Request overhead | Single API request: A single HTTP `POST` call starts the multi-region search. | Multiple API requests: Requires a separate HTTP call for every region and every graph layer.  
Response handling | Real-time stream: Results are pushed to the client as they are found, preventing timeouts. | Static payloads: Individual JSON arrays must be received, collected, and merged manually.  
Deep graphs (greater than 2 layers) | Handles deep, nested lineage graphs automatically up to 100 levels. | Suffers from the N+1 query problem; requires iterative, slow round-trips from the client.  
  
## Choose the right multi-region search method

Review the following scenarios to determine which multi-region search method fits your workload.

Choose the streaming API method for the following use cases:

  * Trace deep or complex graphs: Your data moves through multiple intermediate tables, buckets, or pipelines across different regions, requiring multi-level traversal (`maxDepth` greater than 2).

  * Track column-level lineage: You want to track fields across regions or leverage wildcard (`*`) searches to pull all column dependencies at once.

  * Maintain lightweight code: You prefer to make a single API call and let Google Cloud handle the routing, deduplication, and graph assembly.

  * Require pipeline metadata: You want to optionally retrieve structural details about the processes running your pipelines in the same request payload.




Choose the client-side fan-out method for the following scenarios:

  * You only trace shallow, single-hop lineage: Your lineage graph isn't complex, and you only need to look up direct parent or child links (`maxDepth` equals 1) across a small, fixed number of known regions.

  * You are working within strict legacy systems: You have an existing data-governance application built heavily around the standard `SearchLinks` endpoint and want to maintain structural backward compatibility without implementing streaming response consumers.




## What's next

  * Learn how to [search multi-region lineage using server-side automation](https://docs.cloud.google.com/knowledge-catalog/docs/search-lineage-streaming-api).

  * Learn how to [search multi-region lineage using client-side fan-out](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-fetch-multiple-region-links).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
