---
url: https://docs.cloud.google.com/firestore/native/docs/understand-error-codes/
title: Understand error codes \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:52.597847+00:00
---

# Understand error codes  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/understand-error-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand error codes

This page lists error codes that you might encounter and provides suggestions for how to fix each of them.

### DEADLINE_EXCEEDED

The following can increase `DEADLINE_EXCEEDED` errors:

  * An increase in latency caused an operation take longer than the deadline (60 seconds by default) to complete.


    
    
    DEADLINE_EXCEEDED
    
    A deadline was exceeded on the server.
    

To resolve this issue, see the [guide to troubleshooting latency](https://docs.cloud.google.com/firestore/docs/resolve-latency).

### ABORTED

The following situations can increase `ABORTED` errors:

  * A document receiving too many updates per second.
  * Contention from overlapping transactions.
  * Traffic increases that exceed the 500-50-5 rule or encounter hot-spots.


    
    
    ABORTED
    
    Too much contention on these datastore entities. Please try again.
    

Or
    
    
    ABORTED
    
    Aborted due to cross-transaction contention. This occurs when multiple
    transactions attempt to access the same data, requiring Firestore to abort at
    least one in order to enforce serializability.
    

To resolve this issue:

  * For rapid traffic increases, Firestore attempts to automatically scale to meet the increased demand. When Firestore scales, latency begins to decrease.
  * Hot-spots limit the ability of Firestore to scale up, review [designing for scale](https://docs.cloud.google.com/firestore/native/docs/best-practices#designing_for_scale) to identify hot-spots.
  * Review [data contention in transactions](https://docs.cloud.google.com/firestore/native/docs/transaction-data-contention) and your usage of transactions.
  * Reduce the write rate to individual documents.



### RESOURCE_EXHAUSTED

The following situations can lead to `RESOURCE_EXHAUSTED` errors:

  * You exceeded the [free tier quota](https://cloud.google.com/firestore/quotas#free-quota) and billing is not enabled for your project.

  * Traffic increases not following best practices



    
    
    RESOURCE_EXHAUSTED
    
    Some resource has been exhausted, perhaps a per-user quota.
    

Or
    
    
    RESOURCE_EXHAUSTED
    
    This database has exceeded their daily quota or the ramp up limit for writes, please retry with exponential backoff. To learn more about limits, see 'Usage and limits' section of the support documentation.
    

To resolve this issue:

  * If you are at your free tier quota, wait for the daily reset of your free tier quota or [enable billing for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project).

  * For rapid traffic increases, Firestore attempts to automatically scale to meet the increased demand. When Firestore scales errors might decrease.

  * Hot-spots limit the ability of Firestore to scale up. Review [designing for scale](https://docs.cloud.google.com/firestore/native/docs/best-practices#designing_for_scale) to identify hot-spots.

  * For real-time listener queries, make sure the queries are not unnecessarily broad. Use filters to reduce the number of updates.




### INVALID_ARGUMENT

The following situations can cause `INVALID_ARGUMENT` errors:

  * Attempting to commit a document with an **indexed** field value greater than 1,500 bytes. This limits applies to the UTF-8 encoding of the field value.
  * Attempting to commit a document with **un-indexed** field values greater than 1,048,487 bytes (1 MiB - 89 bytes). This limit applies to the sum of the field values in a document. For example, four fields of 256 KiB each exceed the limit.



1,500 bytes (indexed) and 1,048,487 bytes (un-indexed) are [limits](https://docs.cloud.google.com/datastore/docs/concepts/limits) for field values. You cannot exceed these limits and they are not quotas that can be adjusted.
    
    
    INVALID_ARGUMENT: The value of property field-name is longer than 1500 bytes
    

or
    
    
    INVALID_ARGUMENT: The value of property field_name is longer than 1048487 bytes
    

To resolve this issue:

  * For indexed field values, split the field into multiple fields. If possible, create an un-indexed field and move data that doesn't need to be indexed into the un-indexed field.
  * For un-indexed field values, split the field into multiple fields or implement compression for the field value.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
