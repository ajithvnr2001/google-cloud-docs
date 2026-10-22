---
url: https://docs.cloud.google.com/bigtable/docs/garbage-collection/
title: Garbage collection overview \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:13.894649+00:00
---

# Garbage collection overview  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/garbage-collection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Garbage collection overview

Garbage collection in Bigtable lets you automatically remove expired and obsolete data from your tables. Configuring these policies helps you manage storage costs and maintain read performance.

_Garbage collection_ is the automatic, ongoing process of removing expired and obsolete data from Bigtable tables. A _garbage collection policy_ is a set of rules you create that state when data in a specific column family is no longer needed.

Garbage collection is a built-in, asynchronous background process that takes place during [compaction](https://docs.cloud.google.com/bigtable/docs/overview#compactions). Garbage collection occurs on a fixed schedule that doesn't vary based on how much data needs to be deleted. Until the data is deleted, it appears in read results. You can filter your reads to exclude this data.

**Key Point:** You don't need to filter values from reads if the values have been deleted by you or your application. When you delete a value, it immediately stops appearing in read results. On the other hand, if you want to exclude values that are marked for deletion as part of garbage collection, always apply a filter to your read requests that excludes the same values as your garbage collection rules.

For more information, see the When data is deleted section of this document.

The benefits of garbage collection policies include the following:

  * **Minimize row size** \- You always want to prevent rows from growing indefinitely. Large rows negatively affect performance. Ideally, you should never let a row grow beyond 100 MB in size, and the limit is 256 MB. If you don't need to keep historical data, or earlier versions of your current data, using garbage collection can help you minimize the size of each row.
  * **Keep costs down** \- Garbage collection ensures that you don't pay to store data that is no longer required or used. You are charged for storage of expired or obsolete data until compaction occurs and data eligible for garbage collection is deleted. This process typically takes a few days but might take up to a week.



You can set garbage collection policies either programmatically or with the [ `cbt` CLI ](https://docs.cloud.google.com/bigtable/docs/cbt-overview). Garbage collection policies are set at the column family level.

Each column family in a table has its own garbage collection policy. The garbage collection process looks up the current garbage collection policy for each column family, then deletes data according to the rules in the policy.

## Timestamps

In Bigtable, the intersection of a row and a column can have multiple cells, which contain timestamped versions of the value for that intersection. Each cell has a timestamp. A timestamp is the number of microseconds since the [Unix epoch](https://wikipedia.org/wiki/Unix_time), `1970-01-01 00:00:00 UTC`. You can use default timestamps or set them when you send [write requests](https://docs.cloud.google.com/bigtable/docs/writes).

A timestamp that you send to Bigtable must be a microsecond value with at most millisecond precision. A timestamp with microsecond precision, such as `3023483279876543`, is rejected. In this example, the acceptable timestamp value is `3023483279876000`. 

The timestamp property of a cell can be a "real" timestamp, reflecting the actual time the value for the cell is written, or it can be an "artificial" timestamp. Artificial timestamps include sequential numbers, zeroes, or timestamp-formatted values that are not the actual time the cell was written. Before you use artificial timestamps, review the use cases for artificial timestamps, including the risks of using them:

  * [Simulating cell-level TTL](https://docs.cloud.google.com/bigtable/docs/gc-cell-level)
  * [Storing sequential numbers in timestamps](https://docs.cloud.google.com/bigtable/docs/gc-sequence-numbers)



Make sure that you set a default timestamp when sending write requests unless you need to support a use case with artificial timestamps.

**Caution:** Using artificial timestamps, including zeroes, prevents you from being able to use cells' timestamps for [time-series data](https://docs.cloud.google.com/bigtable/docs/schema-design-time-series). It can take up to a week for garbage collection to remove cells with artificial timestamps.

## Types of garbage collection

This section describes the types of garbage collection available in Bigtable. Code samples for each type of garbage collection are at [Configuring garbage collection](https://docs.cloud.google.com/bigtable/docs/configuring-garbage-collection).

### Expiring values (age-based)

You can set a garbage collection rule based on the timestamp for each cell. For example, you might not want to keep any cells with timestamps more than 30 days before the current date and time. With this type of garbage collection rule, you set the time to live (TTL) for data. Bigtable looks at each column family during garbage collection and deletes any cells that have expired.

### Number of versions

You can set a garbage collection rule that explicitly states the maximum number of cells to keep for all columns in a column family.

For example, if you want to keep only the latest username and email address for a customer, you can create a column family containing those two columns and set the maximum number of values to `1` for that column family.

In another case, you might want to keep the last five versions of a user's password hash to make sure they don't reuse the password, so you would set the maximum number of versions for the column family containing the password column to `5`. When Bigtable looks at the column family during garbage collection, if a sixth cell has been written to the password column, the oldest cell is deleted to keep the number of cells to five.

### Combinations of expiration and version number rules

You can use a combination of expiration and version number rules for garbage collection. The types of combinations are **intersection** , **union** , and **nested**. For configuration examples, see [Garbage collection based on multiple criteria](https://docs.cloud.google.com/bigtable/docs/configuring-garbage-collection#combining).

#### Intersection

An _intersection_ garbage collection policy marks data for deletion when it meets **all** the criteria in a given set of rules. For example, you might want to delete profiles older than 30 days but always keep at least one for each user. In this case, your intersection policy for the column family containing the profile column would consist of a rule for an expiring value **and** a rule for the number of versions.

#### Union

A _union_ garbage collection policy marks data for deletion when it meets **any** item in a given set of rules. For example, you might want to make sure that you retain a maximum of two page-view records per user but only if they are less than 30 days old. In this case, your union policy is set for an expiring value **or** a number of versions.

#### Nested

A _nested_ garbage collection policy has a combination of union and intersection rules.

## Default settings for garbage collection

There is no default TTL for a column family. The number of cells retained for a column depends on how you create the column family that the column is in, as explained in the following sections.

### HBase policy

If you create the column family with the HBase client for Java, the HBase shell, or another tool that uses the HBase client for Java, Bigtable retains only **the most recent cell** in each column in the column family, unless you change the rule. This default setting is consistent with HBase.

### All other client libraries or tools

If you create the column family with any other client library or tool, Bigtable retains an **infinite number** of cells in each column in the column family. This includes column families created with `gcloud` and the `cbt` CLI . You must change the garbage collection policy for the column family if you want to limit the number of versions.

## When data is deleted

Garbage collection is a continuous process in which Bigtable checks the rules for each column family and deletes expired and obsolete data accordingly. In general, it can take up to a week from the time that data matches the criteria in the rules for the data to actually be deleted. You are not able to change the timing of garbage collection.

**Note:** Garbage collection and deletes written to the table by your application are both executed during compaction, but they work differently and independently of each other. A key difference is that if your application deletes a piece of data, a read request for that data immediately afterward returns an empty response. On the other hand, when a piece of data becomes eligible for garbage collection, you can continue to read it until the next compaction occurs.

Because it can take up to a week for expired data to be deleted, you should never rely solely on garbage collection policies to ensure that read requests return the selected data. **Always apply a filter to your read requests that excludes the same values as your garbage collection rules.** You can filter by limiting the number of [cells per column](https://docs.cloud.google.com/bigtable/docs/using-filters#cell-section) or by specifying a [timestamp range](https://docs.cloud.google.com/bigtable/docs/using-filters#timestamp-range).

For example, assume that a column family's garbage collection rule is set to keep only the five most recent versions of a profile, and five versions are already stored. After a new version of the profile is written, it might take up to a week for the oldest cell to be deleted. Therefore, to avoid reading the sixth value, you should always filter out everything except the five most recent versions.

You are charged for storage of expired data until compaction occurs and the data is deleted.

Garbage collection is retroactive: when a new garbage collection policy is set, over the next few days it is applied to all data in the table. If the new policy is more restrictive than the previous policy, old data is deleted as the background work happens, including data that was written before the policy change.

If you want to make sure that data marked for garbage collection is being deleted, you can query your table and compare the data with expected results. You can also [monitor table size in the Google Cloud console](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-monitoring). A table that never gets smaller might reflect a garbage collection policy that is not working as expected, but remember that garbage collection is executed on a delay.

## Replication and garbage collection

[Replication](https://docs.cloud.google.com/bigtable/docs/replication-overview) can affect garbage collection in a few ways.

### Version-based garbage collection and CPU usage

In an instance that uses replication, deletes from version-based garbage collection are replicated to all clusters in the instance in the same way that application requests are replicated. If you rapidly write new cells that cause older cells to become marked for deletion, you might see increased CPU utilization when Bigtable deletes the stale cells and replicates those deletes to other clusters in the instance. Be prepared for this increase in CPU usage if you add a cluster to an instance containing tables that use version-based garbage collection.

Age-based garbage collection, on the other hand, does not increase CPU usage in replicated instances.

### Changing version-based garbage collection policies

You can modify a column family's maximum number of versions in a replicated table. However, if you lower the number of versions for a column family, it can take up to a week for all replicated clusters to reflect the new, lower number. Therefore, you should always use filters when reading the data.

### Changing age-based garbage collection policies

You can increase or decrease the retention time specified in garbage collection policies regardless of whether the instance uses replication. If the instance doesn't use replication, you can also delete an age-based garbage collection policy.

#### Decreasing the retention time

If you decrease the retention time in an age-based policy, it can take up to a week for all clusters to synchronize and use the new policy.

#### Increasing the retention time

In a replicated table, you can increase a garbage collection policy's retention time by a maximum of 90 days.

If you increase the retention period for a column family, be aware that your clusters might be out of sync for longer than a week. To see why, consider a hypothetical case where you have a table in a two-cluster instance and you change a column family's retention period from 30 days to 50 days:

  1. A write request for row key `ip#685` is sent to cluster A with a value of `2023-01-02` for column `click-through` in column family `profile`. The data is replicated to cluster B.
  2. Thirty-one days later, garbage collection occurs on cluster A, and the value in the `click-through` column is recognized as expired and deleted.
  3. You change the garbage collection policy for column family `profile`, increasing the TTL from 30 days to 50 days.
  4. A day later, garbage collection runs on cluster B. Because the TTL is 50 days, the value `2023-01-02` is retained.
  5. The clusters are now out of sync and remain so for almost 20 days until the value that exists in cluster B but not cluster A is finally deleted.



## What's next

  * Explore strategies to [simulate cell-level TTL](https://docs.cloud.google.com/bigtable/docs/gc-cell-level).
  * Read about how [timestamps that are sequential numbers](https://docs.cloud.google.com/bigtable/docs/gc-sequence-numbers) affect garbage collection.
  * Learn more about [storage pricing](https://docs.cloud.google.com/bigtable/pricing#storage).
  * Look at [garbage collection code samples](https://docs.cloud.google.com/bigtable/docs/configuring-garbage-collection) in your preferred programming language.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
