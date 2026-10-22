---
url: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/understand-error-codes/
title: Understand error codes \u00a0|\u00a0 Firestore with MongoDB compatibility \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:36.165515+00:00
---

# Understand error codes  |  Firestore with MongoDB compatibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/understand-error-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore with MongoDB compatibility ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand error codes

This page lists error codes that you might encounter and provides suggestions for how to fix each of them.

### DeadlineExceeded (262)

The following can increase `DeadlineExceeded (262)` errors:

  * An increase in latency caused an operation to take longer than the deadline (60 seconds by default) to complete.


    
    
    DeadlineExceeded (262): Deadline exceeded.
    

To resolve this issue, see the [guide to troubleshooting latency](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/resolve-latency).

### Aborted (112)

The following situations can increase `Aborted (112)` errors:

  * A document receiving too many updates per second.
  * Contention from overlapping transactions.
  * Traffic that increases rapidly or encounters hot-spots.


    
    
    Aborted (112): Too much contention on these documents. Please try again
    

Or
    
    
    Aborted (112): Aborted due to cross-transaction contention. This occurs when
    multiple transactions attempt to access the same data, requiring at least one
    to be aborted in order to enforce serializability.
    

To resolve this issue:

  * For rapid traffic increases, Firestore with MongoDB compatibility attempts to automatically scale to meet the increased demand. When Firestore with MongoDB compatibility scales, latency begins to decrease.
  * Hot-spots limit the ability of Firestore with MongoDB compatibility to scale up. Review [designing for scale](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/understand-reads-writes-scale#avoid_hotspots) to identify hot-spots.
  * Review [data contention in transactions](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/understand-reads-writes-scale#high-level_steps_in_a_write_transaction) and your usage of transactions.
  * Reduce the write rate to individual documents.



### InvalidArgument (2)

The following situations can cause `InvalidArgument (2)` errors:

  * Attempting to commit a document with that exceeds the 7.5 KiB limit for an index entry.



7.5 KiB is a [limit](https://docs.cloud.google.com/firestore/mongodb-compatibility/quotas) for index entries. You cannot exceed this limit and it's not a quota that can be adjusted.
    
    
    InvalidArgument (2): Index entry on field_name is larger than 7680 bytes.
    

To resolve this issue:

For indexed field values, split the field into multiple fields. If possible, create an un-indexed field and move data that doesn't need to be indexed into the un-indexed field.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
