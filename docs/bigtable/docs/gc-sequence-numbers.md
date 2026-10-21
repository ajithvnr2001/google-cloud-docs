---
url: https://docs.cloud.google.com/bigtable/docs/gc-sequence-numbers/
title: Garbage collection for sequential numbers in timestamps \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:11.775432+00:00
---

# Garbage collection for sequential numbers in timestamps  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/gc-sequence-numbers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Garbage collection for sequential numbers in timestamps 

You may have a reason, not related to garbage collection, to assign sequential numbers to the timestamp property for a cell, rather than assigning a date and time. This page describes Bigtable garbage collection for data with this type of artificial timestamps.

Before you read this page, you should read the overview of garbage collection, including the description of [real and artificial timestamps](https://docs.cloud.google.com/bigtable/docs/garbage-collection#timestamps).

## Number of versions

If timestamps are sequence numbers, your garbage collection policy should be based on the number of versions. This means that you specify the number of cells to retain. **An age-based garbage collection policy is unsafe** if you use sequential numbers instead of real timestamps, because age-based policies remove data based on the timestamp.

#### Advantages of storing sequential numbers in timestamps

  * You are able to use monotonically increasing timestamps if you need to.



#### Disadvantages of storing sequential numbers in timestamps

  * You cannot switch to age-based garbage collection.

  * Because your timestamps aren't an actual date and time, you cannot use the cells' timestamps for any other use case, such as determining how old a value is. As a workaround, you can write a real timestamp to a separate column, but this will increase the amount of data you store.

  * Because garbage collection is asynchronous, you still should always use filters when you read the data.




## What's next

  * Read an [overview of Bigtable garbage collection](https://docs.cloud.google.com/bigtable/docs/garbage-collection).
  * Explore strategies to [simulate cell-level TTL](https://docs.cloud.google.com/bigtable/docs/gc-cell-level).
  * Review code samples showing how to [configure garbage collection](https://docs.cloud.google.com/bigtable/docs/configuring-garbage-collection).
  * Learn more about [storage pricing](https://docs.cloud.google.com/bigtable/pricing#storage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
