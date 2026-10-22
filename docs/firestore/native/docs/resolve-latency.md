---
url: https://docs.cloud.google.com/firestore/native/docs/resolve-latency/
title: Resolve latency issues \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:28:07.450990+00:00
---

# Resolve latency issues  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/resolve-latency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolve latency issues

This page shows you how to resolve latency issues with Firestore.

## Latency

The following table describes possible causes of increased latency:

Latency cause | Types of operations affected | Resolution  
---|---|---  
Sustained traffic exceeding the [500-50-5 rule](https://docs.cloud.google.com/firestore/native/docs/best-practices#ramping_up_traffic).  | read, write |  For rapid traffic increases, Firestore attempts to automatically scale to meet the increased demand. When Firestore scales, latency begins to decrease.  Hot-spots (high read, write, and delete rates to a narrow document range) limit the ability of Firestore to scale. Review [designing for scale](https://docs.cloud.google.com/firestore/native/docs/best-practices#designing_for_scale) and identify hot-spots in your application.   
Contention, either from updating a single document too frequently or from transactions. | read, write |  Reduce the write rate to individual documents.  Review [data contention in transactions](https://docs.cloud.google.com/firestore/native/docs/transaction-data-contention) and how you use transactions.   
Slow merge-join queries. | read |  For example, queries with multiple equality filters (`==`) but not backed by composite indexes can result in slow merge-join queries. To improve performance, add composite indexes for these queries, see Reason #3 in [Why is my Firestore query slow?](https://firebase.googleblog.com/2019/08/why-is-my-cloud-firestore-query-slow.html)  
Large reads that return many documents. | read | Use [pagination](https://docs.cloud.google.com/firestore/docs/query-data/query-cursors) to split large reads.   
Too many recent deletes. | read  
This greatly affects operations that list collections in a database. | If latency is caused by too many recent deletes, the issue should automatically resolve after some time. If the issue does not resolve, [contact support](https://cloud.google.com/support-hub).  
Adding and removing listeners too quickly. | realtime listener queries | See the [best practices for realtime updates.](https://docs.cloud.google.com/firestore/native/docs/real-time_queries_at_scale)  
Listening to large documents or to a query with many results. | realtime listener queries | See the [best practices for realtime updates](https://docs.cloud.google.com/firestore/native/docs/real-time_queries_at_scale)  
Index fanout, especially for array fields and map fields. | write | Review your usage of array fields and map fields. For map fields, you can disable subfields from indexing. You can also use [collection level exemptions](https://docs.cloud.google.com/firestore/docs/query-data/indexing#add_a_collection-level_exemption).  
Large writes and batched writes. | write |  Try reducing the number of writes in each batched write. Batched writes are atomic and many writes in a single batch can increase latency and contention. For example, a batch of 10 writes performs better than a batch of 500 writes.  For bulk data entry where you don't require atomicity, use a [server client library](https://docs.cloud.google.com/firestore/docs/reference/libraries#server_client_libraries) with parallelized individual writes. Batched writes perform better than serialized writes but not better than parallel writes.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
