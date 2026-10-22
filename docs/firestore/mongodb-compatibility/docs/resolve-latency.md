---
url: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/resolve-latency/
title: Resolve latency issues \u00a0|\u00a0 Firestore with MongoDB compatibility \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:39.130883+00:00
---

# Resolve latency issues  |  Firestore with MongoDB compatibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/resolve-latency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore with MongoDB compatibility ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolve latency issues

This page shows you how to resolve latency issues with Firestore with MongoDB compatibility.

## Latency

The following table describes possible causes of increased latency:

Latency cause | Types of operations affected | Resolution  
---|---|---  
Sustained, increasing traffic.  | read, write |  For rapid traffic increases, Firestore with MongoDB compatibility attempts to automatically scale to meet the increased demand. When Firestore with MongoDB compatibility scales, latency begins to decrease.  Hot-spots (high read, write, and delete rates to a narrow document range) limit the ability of Firestore with MongoDB compatibility to scale. Review [Avoid hot-spots](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/understand-reads-writes-scale#avoid_hotspots) and identify hot-spots in your application.   
Contention, either from updating a single document too frequently or from transactions. | read, write |  Reduce the write rate to individual documents.  Reduce the number of documents updated in a single write transaction.   
Large reads that return many documents. | read | Use pagination to split large reads.   
Too many recent deletes. | read  
This greatly affects operations that list collections in a database. | If latency is caused by too many recent deletes, the issue should automatically resolve after some time. If the issue does not resolve, [contact support](https://cloud.google.com/support-hub).  
Index fanout, especially for array fields and embedded document fields. | write | Review your indexing of array fields and embedded document fields.  
Large writes. | write |  Try reducing the number of writes in each operation.  For bulk data entry where you don't require atomicity, use parallelized individual writes.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
