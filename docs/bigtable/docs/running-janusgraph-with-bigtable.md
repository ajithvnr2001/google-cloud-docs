---
url: https://docs.cloud.google.com/bigtable/docs/running-janusgraph-with-bigtable/
title: JanusGraph on GKE with Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:20.219899+00:00
---

# JanusGraph on GKE with Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/running-janusgraph-with-bigtable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback 

#  JanusGraph on GKE with Bigtable Stay organized with collections  Save and categorize content based on your preferences. 

Graph databases can help you to discover insights by modeling your data entities and the relationships between them. [JanusGraph](http://janusgraph.org/) is a graph database that supports working with large amounts of data. This page presents concepts that can help you run JanusGraph on Google Cloud with Google Kubernetes Engine as the orchestration platform and Bigtable as the storage backend.

The document is for system architects, database administrators, and DevOps professionals who are interested in running the JanusGraph graph database on Google Cloud using a Bigtable as the storage backend. It assumes that you are familiar with [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine), Kubernetes Pods, [Bigtable](https://docs.cloud.google.com/bigtable/docs/overview), and [Elasticsearch](https://www.elastic.co/elasticsearch/).

## Overview

In graph terminology, entities are known as _nodes_ or _vertices_ and relationships are known as _edges_. In JanusGraph, both vertices and edges can have additional associated data that is made available through properties.

![Example of a property graph.](https://docs.cloud.google.com/static/bigtable/img/janusgraph-property-graph.svg)

The preceding illustration is an example of a property graph.

Graph databases help you model a variety of domains and activities:

  * Social networks
  * Financial transactions (for fraud analysis)
  * Physical or virtual system networks



When you create graph databases, you sometimes create millions or even billions of vertices and edges. When you use JanusGraph with Bigtable as the underlying storage layer, you can both execute fast queries (known as _graph traversals_) and scale your storage layer independently according to the size and throughput that you need. JanusGraph also uses a pluggable indexing backend to provide full-text indexing for vertex and edge properties.

You can deploy a scalable JanusGraph infrastructure on GKE, using Elasticsearch as the indexing backend running in Pods in a StatefulSet, and using Bigtable as the storage backend. When you're done, you can traverse the relationships that exist in your graph data.

The following diagram shows how these elements fit together.

![JanusGraph deployment with Bigtable on GKE.](https://docs.cloud.google.com/static/bigtable/img/janusgraph-bigtable-gke-deployment.svg)

The prceeding diagram shows the JanusGraph deployment on GKE with Elasticsearch andBigtable.

## JanusGraph data in Bigtable

Graph data is stored by JanusGraph as an adjacency list. Each row represents a vertex, any adjacent vertices (edges), and property metadata about the vertices and edges. The row key is the unique identifier for the vertex. Each relationship between the vertex and another vertex and any properties that further define the relationship are stored as an edge or edge-property column. Both the column qualifier and column value store data that defines the edge, in accordance with [Bigtable best practices](https://docs.cloud.google.com/bigtable/docs/schema-design#row-keys). Each vertex property is stored as a separate column, again using both the column qualifier and the column value to define the property.

The following diagram shows this storage structure.

![JanusGraph adjancency list storage structure.](https://docs.cloud.google.com/static/bigtable/img/janusgraph-bigtable-gke-adjacency-list.svg)

The diagram shows the logical storage structure for a small graph fragment with logical details for two vertex rows. In the diagram, the two example rows represent two vertices. The first vertex is labeled with a single vertex property and is related to two other vertices by two separate edges. The second vertex holds columns containing two properties and one edge.

The following illustration of the vertex edge logical data model provides some detail about the column qualifiers and values for an edge or edge-property column.

![JanusGraph edge and edge property column.](https://docs.cloud.google.com/static/bigtable/img/janusgraph-bigtable-gke-edge-and-edge-property-column.svg)

For each adjacent vertex, a column stores the metadata about that edge. The column qualifier contains metadata about the edge relationship and about the edge direction, and a pointer to the adjacent vertex. The column value contains the edge label and any additional edge properties. Because traversals can be followed in either direction, edges are stored twice, once for each end of the edge relationship. Bidirectional edge storage significantly increases traversal performance, but comes with some trade-offs due to the redundancy of additional storage space and non-atomic edge mutations.

The following diagram is the logical data model of a vertex property column.

![JanusGraph column values for a property column.](https://docs.cloud.google.com/static/bigtable/img/janusgraph-bigtable-gke-column-values-property-column.svg)

The previous illustration provides details about the column qualifiers and values for an edge column.

Each vertex property is stored as a separate column. The column qualifier is a unique identifier for the property key. The column value contains both an identifier for the property and the value of the property.

JanusGraph also relies on Bigtable's lexicographical ordering of rows and column qualifiers to enhance query performance.

## What's next

  * Read more about [JanusGraph](http://janusgraph.org/) and [graph databases](https://wikipedia.org/wiki/Graph_database).
  * Learn about [Apache TinkerPop](http://tinkerpop.apache.org/) graph computing framework and explore the [Gremlin](http://tinkerpop.apache.org/gremlin.html) graph traversal language.
  * Learn more about how [JanusGraph stores data in Bigtable](https://docs.janusgraph.org/advanced-topics/data-model).
  * Dive deeper into graph use cases by deploying an [example JanusGraph application](https://cloud.google.com/blog/products/gcp/developing-a-janusgraph-backed-service-on-google-cloud-platform).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
