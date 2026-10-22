---
url: https://docs.cloud.google.com/bigtable/docs/gc-cell-level/
title: Simulate cell-level TTL \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:50.231368+00:00
---

# Simulate cell-level TTL  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/gc-cell-level/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Simulate cell-level TTL

In Bigtable, garbage collection policies are set at the column family level, and you cannot specify a cell-level garbage collection policy. However, you can simulate a time to live (TTL) policy at the cell level by changing your garbage collection settings. This page explains a few different approaches that you can use.

Before you read this page, you should read the [garbage collection overview](https://docs.cloud.google.com/bigtable/docs/garbage-collection). To learn how to send write requests, which include timestamps, see [Bigtable writes](https://docs.cloud.google.com/bigtable/docs/writes).

## One-second expiration

In this approach, set your garbage collection rule to let data expire after one second. Whenever you write data, set the cell's timestamp to the time you want the value to expire. During compaction, Bigtable deletes any cells that have a timestamp that is at least one second in the past. For example, if you set a cell's timestamp to April 30 at 9:00:00 AM, the cell is deleted sometime after April 30 at 9:00:01 AM. This approach enables you to set different expiration values for different cells in the same column family.

### Advantages of one-second expiration

  * The timestamp has a real meaning: the expiration time.



### Disadvantages of one-second expiration

  * Every application that writes data to this Bigtable column family needs to be configured to follow this rule. If you forget and use a default server timestamp on a write, that data expires right away and is deleted during the next compaction.

  * Because your timestamps aren't "real" you cannot use timestamps for any other use case, such as determining when a value was written. As a workaround, you can write the real timestamp to a separate column, but this will increase the amount of data you store.

  * **You cannot implement this strategy on a column family that already has data with real timestamps.** If existing data has real timestamps, or if you accidentally write new data with real timestamps, that data is deleted during the next compaction.

  * You cannot specify that multiple cells for a given row and column should expire at the same time as each other. New data will overwrite old data with the same timestamp.

  * Because garbage collection can take up to a week, you always need to use filters when you read the data.




## Default expiration

Let's say you want most of your data to have a default TTL, but you want to set different per-cell expiration values for some of your data.

For example, you might store click events for ten customers in one table. Most of the click events should expire after 2 days, but you have one customer whose click events should expire after an hour, and you have another customer whose click events should expire after 3 days.

In this approach, create your column family with an age limit for garbage collection set to the default TTL. For data you want to expire sooner than the default, set the timestamp to be earlier than the time the data is actually written. For data you want to expire later, set the timestamp to be later than the time the data is actually written.

### Advantages of default expiration

  * A default TTL is in place for writes that do not have a custom TTL.

  * This approach can safely be applied to a pre-existing table.




### Disadvantages of default expiration

  * The timestamp is not semantically meaningful because a cell's timestamp might be real or artificial. This means you cannot use the cells' timestamps for any other use case, such as determining when a value was written. As a workaround, you can write the real timestamp to a separate column, but this will increase the amount of data you store.

  * You can inadvertently write a custom timestamp that clashes with a real timestamp in a given column.

  * Because garbage collection is asynchronous, you still need to always use filters when you read the data when you use this strategy.




## What's next

  * Read about garbage collection with [timestamps that are sequential numbers](https://docs.cloud.google.com/bigtable/docs/gc-sequence-numbers).
  * Learn a strategy to [always read the most recent value of a column](https://docs.cloud.google.com/bigtable/docs/keep-only-latest-value).
  * Review code samples showing how to [configure garbage collection](https://docs.cloud.google.com/bigtable/docs/configuring-garbage-collection).
  * Learn more about [storage pricing](https://docs.cloud.google.com/bigtable/pricing#storage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
