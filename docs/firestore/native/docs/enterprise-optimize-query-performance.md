---
url: https://docs.cloud.google.com/firestore/native/docs/enterprise-optimize-query-performance/
title: Optimize query performance \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:51.458321+00:00
---

# Optimize query performance  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/enterprise-optimize-query-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Optimize query performance

To troubleshoot slow queries, use [Query Explain](https://docs.cloud.google.com/firestore/native/docs/enterprise-query-explain) to obtain the query execution plan and the runtime execution profile. The following section describe steps you can take to optimize query performance depending on the execution profile:

## Limit the number of results

Use the records returned field in the execution tree to identify if the query is returning many documents. Consider limiting the number of documents returned by using the `limit(...)` stage. This reduces the serialized byte size of the results when returned to the clients over the network. In cases where the `Limit` node is preceded by a `MajorSort` node, the query engine can coalesce the `Limit` and the `MajorSort` nodes and replaces a full in-memory materialization and sort with a TopN sort, reducing the memory requirement for the query.

## Limit the Result Document Size

Consider limiting the size of the document returned by using by using a `select(...)` to only return the fields required or `remove_fields(...)` to discard overly large fields. This helps reduce the compute and memory cost of processing intermediate results and the serialized byte size of the results when returned to the clients over the network. In cases where all fields referenced in the query are covered by a regular index, this also allows the query to be fully covered by the index scan, avoiding the need to fetch documents from the primary storage.

## Use indexes

Use the following instructions to set up and optimize indexes.

### Identify if the query is using an index

You can identify if the query is using an index by checking the leaf nodes in the execution tree. If the leaf node of the execution tree is a [TableScan node](https://docs.cloud.google.com/firestore/native/docs/enterprise-query-explain-reference#tablescan), that means the query is not using an index and is scanning documents from primary storage. If an index is being used, the leaf node of the execution tree will display the index ID and index fields of the index.

### Identify a better index

An index is useful for a query if it can reduce the number of documents that the query engine needs to fetch from primary storage or if its field ordering can deliver the Sort requirement of the query.

If an index is used for a query, but the query engine is still fetching and discarding many documents, as identified by a Scan node that returns many records followed by a [Filter node](https://docs.cloud.google.com/firestore/native/docs/enterprise-query-explain-reference#filter) that returns few records, this is a sign that the query predicate satisfied using the index is not selective. To create a more suitable index, see Create indexes.

If an index is used for a query, but the query engine is still performing an in-memory reordering of the result set, as identified by a [MajorSort node](https://docs.cloud.google.com/firestore/native/docs/enterprise-query-explain-reference#majorsort) in the query execution tree, this is a sign that the index used can't be used to deliver the Sort requirement of the query. To create a more suitable index, see the next section.

### Create Indexes

Follow the index management documentation to [create indexes](https://docs.cloud.google.com/firestore/native/docs/enterprise-indexing). To ensure your query can use indexes, create regular (not Multikey) indexes with fields in the following order:

  1. All fields that will be used in equality operators. To maximize chance of reuse across queries, order fields in decreasing order of occurrence of the fields in equality operators among queries.
  2. All fields that will be sorted on (in the same order).
  3. Fields that will be used in range or inequality operators in decreasing order of query constraint selectivity.
  4. Fields that will be returned as part of a query in the index: including such fields in the index allows the index to cover the query and avoid having to fetch document from the primary storage.



### Force an index or table scan

When you query Firestore in Native Mode, it automatically uses any indexes that are likely to make the query more efficient. As a result, you don't need to specify an index for your queries. However, for queries that are critical for your workload, we recommend that you use the `forceIndex` option for more consistent performance.

In a few cases, Firestore in Native Mode might choose an index that causes query latency to increase. If you've followed the troubleshooting steps for performance regressions and confirmed that it makes sense to try a different index for the query, you can specify the index using the `forceIndex` option.

You can use the `forceIndex` option on any input stage in Pipeline operations to override Firestore in Native Mode's default query plan and specify an index to use, or to force a table scan.

#### Force a specific index

To force the query to use a specific index, provide the index ID as a string to the `forceIndex` option. You can find the index ID from the console or from error messages.

The following example forces the planner to use index with ID `CICAgOi36pgK`:

##### Node.js
    
    
    // Force Planner to use Index ID CICAgOi36pgK
    await db.pipeline()
      .collectionGroup({ collectionId: "customers", forceIndex: "CICAgOi36pgK" })
      .limit(100)
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2319-L2323)

##### Java
    
    
    // Force Planner to use Index ID CICAgOi36pgK
    Pipeline.Snapshot results1 =
        firestore.pipeline()
          .collectionGroup("customers", new CollectionGroupOptions()
              .withHints(new CollectionHints().withForceIndex("CICAgOi36pgK")))
          .limit(100)
          .execute().get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/8edd723bfd9e683eb3b29c069de8ccc91bc1d847/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L3308-L3314)

##### Go
    
    
    // Force Planner to use Index ID CICAgOi36pgK
    snapshot1 := client.Pipeline().
    	CollectionGroup("customers", firestore.WithForceIndex("CICAgOi36pgK")).
    	Limit(100).
    	Execute(ctx)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_general.go#L1497-L1501)

Here are some use cases for forcing a specific index:

  * Testing the performance of different indexes.
  * Ensuring a specific, known-optimal index is used for a query.
  * Overriding the optimizer when its default choice is suboptimal for a particular query.



If the specified index is not found, the query fails.

#### Force a table scan

A table scan reads documents in the collection or collection group without using any secondary indexes. To force a table scan, set `forceIndex` to `primary`.

The following example forces a table scan:
    
    
    // Force Planner to only do a Full-Table Scan
    db.pipeline()
      .collectionGroup({ collectionId: "customers", forceIndex: "primary" })
      .limit(100)
    

You might use a table scan in the following cases:

  * For very small collections where index overhead is not justified.
  * For queries that access most of the documents in a collection.
  * For debugging and performance comparisons.

**Caution:** Table scans on large collections are slow and don't scale. They read all documents in the collection, which significantly increases read operation costs. For most production scenarios, we recommend relying on indexes instead of forcing table scans.

#### Use `forceIndex` with Query Explain

You can use [Query Explain](https://docs.cloud.google.com/firestore/native/docs/enterprise-query-explain) in the `explain` or `analyze` modes to observe the effects of `forceIndex`:

  * Verify that Firestore in Native Mode used the specified index in `forceIndex` by checking the leaf nodes of the execution tree for the index ID.
  * Confirm that a `TableScan` node appears in the plan when using `forceIndex: "primary"`.
  * With `analyze` mode, compare the performance metrics—such as latency, documents scanned, and index entries scanned—with and without `forceIndex` to fine-tune query performance.



#### Best practices for `forceIndex`

While `forceIndex` provides more control over query execution, Firestore in Native Mode's query optimizer is generally efficient for most use cases. Consider the following best practices when using `forceIndex`:

  * Use `forceIndex` judiciously. If you observe suboptimal performance with the default query plan, use [Query Explain](https://docs.cloud.google.com/firestore/native/docs/enterprise-query-explain) to diagnose the issue before forcing an index.
  * When using `forceIndex`, make sure to test your queries with realistic data volumes to understand their performance and cost characteristics.
  * Avoid using `forceIndex: "primary"` on large collections in production environments.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
