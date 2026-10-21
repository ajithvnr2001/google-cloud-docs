---
url: https://docs.cloud.google.com/blog/products/gcp/what-dbas-need-to-know-about-cloud-spanner-part-1-keys-and-indexes/
title: What DBAs need to know about Cloud Spanner: Keys and indexes | Google Cloud Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:06:07.371571+00:00
---

# What DBAs need to know about Cloud Spanner: Keys and indexes | Google Cloud Blog

> Source: https://docs.cloud.google.com/blog/products/gcp/what-dbas-need-to-know-about-cloud-spanner-part-1-keys-and-indexes/

Google Cloud

# 

What DBAs need to know about Cloud Spanner, part 1: Keys and indexes

June 8, 2018

  * [](https://x.com/intent/tweet?text=What%20DBAs%20need%20to%20know%20about%20Cloud%20Spanner,%20part%201:%20Keys%20and%20indexes%20@googlecloud&url=https://cloud.google.com/blog/products/gcp/what-dbas-need-to-know-about-cloud-spanner-part-1-keys-and-indexes)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://cloud.google.com/blog/products/gcp/what-dbas-need-to-know-about-cloud-spanner-part-1-keys-and-indexes&title=What%20DBAs%20need%20to%20know%20about%20Cloud%20Spanner,%20part%201:%20Keys%20and%20indexes)
  * [](https://www.facebook.com/sharer/sharer.php?caption=What%20DBAs%20need%20to%20know%20about%20Cloud%20Spanner,%20part%201:%20Keys%20and%20indexes&u=https://cloud.google.com/blog/products/gcp/what-dbas-need-to-know-about-cloud-spanner-part-1-keys-and-indexes)
  * [](mailto:?subject=What%20DBAs%20need%20to%20know%20about%20Cloud%20Spanner,%20part%201:%20Keys%20and%20indexes&body=Check%20out%20this%20article%20on%20the%20Cloud%20Blog:%0A%0AWhat%20DBAs%20need%20to%20know%20about%20Cloud%20Spanner,%20part%201:%20Keys%20and%20indexes%0A%0ALearn%20the%20dos-and-don%27ts,%20best%20practices%20and%20why%20things%20are%20different%20in%20Cloud%20Spanner.%0A%0Ahttps://cloud.google.com/blog/products/gcp/what-dbas-need-to-know-about-cloud-spanner-part-1-keys-and-indexes)



##### Niel Markwick

Solutions Architect

##### Robert Saxby

Product Manager

[Cloud Spanner](https://cloud.google.com/spanner/) is a relational and horizontally scalable database service, built from a cloud/distributed design perspective. It brings efficiency and high availability for developers and database administrators (DBAs), and differs structurally from typical databases you’re used to. In this blog series, we’ll explore some of the key differences that DBAs and developers will encounter as you migrate from traditional vertically-scaling (scale-up) relational database management systems (RDBMS) and move to Cloud Spanner. We will discuss some of the dos-and-don'ts, best practices and why things are different in Cloud Spanner.

In this series, we will explore a range of topics, including:   


  * Selection of keys and use of indexes
  * How to approach business logic
  * Importing and exporting data
  * Migrating from your existing RDBMS
  * Optimizing performance
  * Access control and logging 

You’ll gain an understanding of how to best use Cloud Spanner and release its potential to achieve linearly scalable performance over massive databases. In this first installment, let’s start with a closer look at how the concepts of keys and indexes work in Cloud Spanner.

###  Choosing keys in Cloud Spanner

Just like in other databases, the choice of key is vitally important to optimize the performance of the database. It’s even more important in Cloud Spanner, due to the way its mechanisms distribute database load. Unlike traditional RDBMS, you’ll need to take care when choosing the primary keys for the tables and choosing which columns to index. 

Using well-distributed keys results in a table whose size and performance can scale linearly with the number of Cloud Spanner nodes, while using poorly distributed keys can result in hotspots, where a single node is responsible for the majority of reads and writes to the table.

In a traditional vertically scaled RDBMS, there is a single node that manages all of the tables. (Depending on the installation, there may be replicas that can be used for reading or for failover). This single node therefore has full control over the table row locks, and the issuing of unique keys from a numeric sequence.

Cloud Spanner is a distributed system, with many nodes reading and writing to the database at any one time. However, to achieve scalability, along with global ACID transactions and strong consistency, only one node at any one time can have write responsibility for a given row.

Cloud Spanner distributes management of rows across multiple nodes by breaking up each table into several [splits](https://cloud.google.com/spanner/docs/schema-and-data-model#database-splits), using ranges of the lexicographically sorted primary key. 

This enables Cloud Spanner to achieve high availability and scalability, but it also means that using any continuously increasing or decreasing sequence as a key is detrimental to performance. To explain why, let’s explore how Cloud Spanner creates and manages its table splits.

###  Table splits and key choice

Cloud Spanner manages splits using [Paxos](https://en.wikipedia.org/wiki/Paxos_\(computer_science\)) (you can learn more about how in this detailed documentation: [Life of Cloud Spanner Reads & Writes](https://cloud.google.com/spanner/docs/whitepapers/life-of-reads-and-writes) and [Spanner: Google's Globally Distributed Database](https://research.google.com/archive/spanner.html)). In a regional instance of Cloud Spanner, the responsibility for reading/writing each split is distributed across a group of three nodes, one in each of the three availability zones of the Cloud Spanner instance.

  


One node in this group of three is elected Split Leader and manages the writes and locks for all the rows in the split. All three nodes in the group can perform reads.

To create a visual example, consider a table with 600 rows that uses a simple, continuous, monotonically increasing integer key (as is common in traditional RDBMS), broken into six splits, running on a two-node (per zone) Cloud Spanner instance. In an ideal situation, the table will have six splits, the leaders of which will be the six individual nodes available in the instance.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/gcp-split-leaderndlc.max-700x700.PNG](https://storage.googleapis.com/gweb-cloudblog-publish/images/gcp-split-leaderndlc.max-700x700.PNG)![https://storage.googleapis.com/gweb-cloudblog-publish/images/gcp-split-leaderndlc.max-700x700.PNG](https://storage.googleapis.com/gweb-cloudblog-publish/images/gcp-split-leaderndlc.max-700x700.PNG)

This distribution would result in ideal performance when reading/updating the rows, provided that the reads and updates are evenly distributed across the key range.

###  Problems with hotspots

The problem arises when new rows are appended to the database. Every new row will have an incrementing ID and will be added to the last split, meaning that out of the six available nodes, only one node will be handling all of the writes. In the example above, node 2c would be handling all writes. This node then becomes a hotspot, limiting the overall write performance of the database. In addition, the row distribution becomes unbalanced, with the last split becoming significantly larger, so it’s then handling more row reads than the others. 

Cloud Spanner does try to compensate for uneven load by [adding and removing splits in the background](https://cloud.google.com/spanner/docs/schema-and-data-model#database-splits) according to read and write load, and by creating a new split once the split size crosses a set threshold. However, in a frequently appended table, this will not happen quickly enough to avoid creating a hotspot.

Along with monotonically increasing or decreasing keys, this issue also affects tables that are indexed by any deterministic key—for example, an increasing timestamp in an event log table. Timestamp-keyed tables are also more likely to have a read hotspot because, in most cases, recently timestamped rows are accessed more frequently than the others. (Check out [Cloud Spanner — Choosing the right primary keys](https://medium.com/google-cloud/cloud-spanner-choosing-the-right-primary-keys-cd2a47c7b52d) for detailed information on detecting and avoiding hotspots.)

###  Problems with sequence generators

The concept of sequence generators, or lack thereof, is an important area to explore further. Traditional vertical RDBMS have integrated sequence generators, which create new integer keys from a sequence during a transaction. Cloud Spanner cannot have this due to its distributed architecture, as there would either be race conditions between the split leader nodes when inserting new keys, or the table would have to be globally locked when generating a new key, both of which would reduce performance.

One workaround could be that the key is generated by the application (for example, by storing the next key value in a separate table in the database, or by getting the current maximum key value from the table). However, you’ll run into the same performance problems. Consider that as the application is also likely to be distributed, there may be multiple database clients trying to append a row at the same time, with two potential results depending on how the new key is generated:   


  * If the SELECT for the existing key is performed in the transaction, one application instance trying to append would block all other application instances trying to append due to row locking.
  * If the SELECT for the existing key is done outside of the transaction, then there is a race between each of the application instances trying to append the new row. One will succeed, while others would have to retry (including generating a new key) after the append fails, since the key already exists. 



###  What makes a good key

So if sequential keys will limit database performance in Cloud Spanner, what’s a good key to use? Ideally, the high-order bits should be evenly and semi-randomly distributed when keys are generated. 

One simple way to generate such a key is to use random numbers, such as a random universally unique identifier (UUID). Note that there are several classes of [UUID](http://go/wiki/Universally_unique_identifier#Versions). Versions 1 and 2 use deterministic prefixes, such as timestamps or MAC addresses. Ensure that the UUID generation method you use is truly randomly distributed, i.e., v4, at least over the higher order bytes. This will ensure that the keys are evenly distributed among the keyspace, and hence that the load is distributed evenly over the spanner nodes. 

Although another approach might be to use some real-world attributes of the data that are immutable and evenly distributed over the key range, this is quite a challenge since most uniformly distributed attributes are discrete and not continuous. For example, the random result of a dice roll is uniformly distributed and has six finite values. A continuous distribution could rely on an irrational number, for example π.

###  What if I really need an integer sequence as a key?

Though it’s not recommended, in some circumstances an integer sequence key is necessary, either for legacy or for external reasons, e.g., an employee ID.

To use an integer sequence key, you’ll first need a sequence generator that’s safe across a distributed system. One way of doing this is to have a table in Cloud Spanner contain a row for each required sequence that contains the next value in the sequence—so it would look something like this: 

Loading...

CREATE TABLE Sequences ( Sequence_ID STRING(MAX) NOT NULL, -- The name of the sequence Next_Value INT64 NOT NULL ) PRIMARY KEY (Sequence_ID)

When a new ID value is required, the next value of the sequence is read, incremented and updated in the same transaction as the insert for the new row.

Note that this will limit performance when many rows are inserted, as each insert will block all other inserts due to the update of the Sequences table that we created above.

This performance issue can be reduced—though at the cost of possible gaps in the sequence—if each application instance reserves a block of, for example, 100 sequence values at once by incrementing Next_Value by 100, and then manages issuing individual IDs from that block internally.

In the table using the sequence, the key cannot simply be the numeric sequence value itself, as that will cause the last split to become a hotspot (as explained previously). So the application must generate a complex key that randomly distributes the rows among the splits.

This is known as _application-level sharding_ and is achieved by prefixing the sequential ID with an additional column containing a value that’s evenly distributed among the key space—e.g., a hash of the original ID, or bit-reversing the ID. That looks something like this: 

Loading...

CREATE TABLE Table1 ( Hashed_Id INT64 NOT NULL, ID INT64 NOT NULL, \-- other columns with data values follow.... ) PRIMARY KEY (Hashed_Id, Id)

Even a simple cyclic redundancy check (CRC)32 checksum is good enough to provide a suitably pseudo-random Hashed_Id. It does not have to be secure, just enough to randomize the row order of the sequentially numbered keys, as in the following table:

![https://storage.googleapis.com/gweb-cloudblog-publish/images/gcp-cyclic-redundancy-checka224.max-400x400.PNG](https://storage.googleapis.com/gweb-cloudblog-publish/images/gcp-cyclic-redundancy-checka224.max-400x400.PNG)![https://storage.googleapis.com/gweb-cloudblog-publish/images/gcp-cyclic-redundancy-checka224.max-400x400.PNG](https://storage.googleapis.com/gweb-cloudblog-publish/images/gcp-cyclic-redundancy-checka224.max-400x400.PNG)

Note that whenever a row is read directly, both the ID and Hashed_Id must be specified to prevent a table scan, as in this example: 

Loading...

SELECT * FROM Table1 WHERE t1.Hashed_Id = 0xDEADBEEF AND t1.Id = 1234

Similarly, whenever this table is joined with other tables in the query by Id, the join must also use both the ID and the Hashed_Id. Otherwise, you’ll lose performance, since a table scan will be required to find the row. This means that the table that references the ID must also include the Hashed_Id, like this: 

Loading...

CREATE TABLE Table2 ( Id String(MAX), -- UUID Table1_Hashed_Id INT64 NOT NULL, Table1_Id INT64 NOT NULL, \-- other columns with data values follow.... ) PRIMARY KEY (Id) SELECT * from Table2 t2 INNER JOIN Table1 t1 ON t1.Hashed_Id = t2.Table1_Hashed_Id AND t1.Id = t2.Table1_Id WHERE ... -- some criteria

###  What if I really need to use a timestamp as a key?

In many cases, the row using the timestamp as a key also refers to some other table data. For example, the transactions on a bank account will refer to the source account. In this case, assuming that the source account number is already reasonably evenly distributed, you can use a complex key containing the account number first and then the timestamp: 

Loading...

CREATE TABLE Transactions ( account_number INT64 NOT NULL, timestamp TIMESTAMP NOT NULL, transaction_info ..., ) PRIMARY KEY (account_number, timestamp DESC)

The splits will be made primarily using the account number and not the timestamp, thus distributing the newly added rows over various splits.

Note that in this table, the timestamp is sorted by descending order. That’s because in most cases you want to read the most recent transactions—which will be first in the table—so you won’t need to scan through the entire table to find the most recent rows.

If you do not, or cannot have an external reference, or have any other data that you can use in the key in order to distribute the order, then you will need to perform application-level sharding, which is shown in the integer sequence example above. 

Note, however, that using a simple hash will make queries by timestamp range extremely slow, since retrieving a range of timestamps will require a full table scan to cover all the hashes. Instead, we recommend generating a ShardId from the timestamp. So, for example, 

Loading...

TimestampShardId = CRC32(Timestamp) % 100

will return a pseudo-random value between 0 and 99 from the timestamp. Then, you can use this ShardId in the table key so that sequential timestamps are distributed across multiple splits, like so: 

Loading...

CREATE TABLE Events ( TimestampShardId INT64 NOT NULL Timestamp TIMESTAMP NOT NULL, event_info... ) PRIMARY KEY (TimestampShardId, Timestamp DESC)

For example, a table with dates of the first 10 days of 2018 (which without ShardId would be stored in the table in date order) will give the following ordering:

![https://storage.googleapis.com/gweb-cloudblog-publish/images/gcp-TimestampShardId1ek6.max-400x400.PNG](https://storage.googleapis.com/gweb-cloudblog-publish/images/gcp-TimestampShardId1ek6.max-400x400.PNG)![https://storage.googleapis.com/gweb-cloudblog-publish/images/gcp-TimestampShardId1ek6.max-400x400.PNG](https://storage.googleapis.com/gweb-cloudblog-publish/images/gcp-TimestampShardId1ek6.max-400x400.PNG)

When a query is made, you must use a BETWEEN clause to be able to select across all shards without performing a table scan: 

Loading...

Select * from Events WHERE TimestampShardId BETWEEN 0 AND 99 AND Timestamp > @lower_bound AND Timestamp < @upper_bound;

Note that the ShardId is only a way of improving key distribution so that Cloud Spanner can use multiple splits to store sequential timestamps. It does not identify an actual database split, and rows in different tables with the same ShardId may well be in different splits.

###  Migration implications

When you’re migrating from an existing RDBMS that uses keys that are not optimal for Cloud Spanner, take the above considerations into account. If necessary, add key hashes to tables or change the key ordering.

###  Deciding on indexes in Cloud Spanner

In a traditional RDBMS, indexes are very efficient ways of looking up rows in a table by a value that is not the primary key. Under most circumstances, a row lookup via an index will take approximately the same time as a row lookup via its key. That’s because the table and the index are managed by a single node, so the index can point directly to the on-disk row of the table. 

In Cloud Spanner, indexes are actually implemented using tables, which allows them to be distributed and enables the same degree of scalability and performance as normal tables. 

However, because of this type of implementation, using indexes to read the data from the table row is less efficient than in a traditional RDBMS. It’s effectively an inner join with the original table, so reading from a table using an indexed key turns into this process:   


  * Look up split for index key
  * Read index row from split to get table key
  * Look up split for table key
  * Read table row from split to get row values
  * Return row values

Note that there is no guarantee that the split for the index key is on the same node as the split for the table key, so a simple index query may require cross-node communication just to read one row.

Similarly, updating an indexed table will most likely require a multi-node write to update the table row and the index row. So using an index in Cloud Spanner is always a trade-off between improved read performance and reduced write performance. 

###  Index keys and hotspots

Because indexes are implemented as tables in Cloud Spanner, you’ll encounter the same issues with the indexed columns as you did with the table keys: An index on a column with poorly distributed values (such as a timestamp) will lead to the creation of a hotspot, even if the underlying table is using well-distributed keys. That’s because when rows are appended to the table, the index will also have new rows appended, and writes for these new rows will always be sent to the same split.

Therefore, care must be taken when creating indexes, and we recommend that you create indexes only using columns which have a well-distributed set of values, just like when choosing a table key. 

In some cases, you’ll need to do application-level sharding for the indexed columns in order to create a synthetic ShardId column, which can be used in the index to distribute values over the splits.

For example, this configuration below will create a hotspot when appending events due to the index, even if UserId is randomly distributed. 

Loading...

CREATE TABLE Events ( UserId String(MAX), Timestamp TIMESTAMP, EventData) PRIMARY KEY (UserId, Timestamp DESC); CREATE INDEX EventsByTimestamp ON Events (Timestamp DESC);

As with a table keyed by timestamp only, a synthetic ShardId column will need to be added to the table, and then used as the first indexed column to help the distribution of the index among the splits.

A simple ShardId generator could be: 

Loading...

TimestampShardId = CRC32(Timestamp) % 100

which will give a hash value between 0 and 99 from the timestamp. You’ll need to add this to the original table as a new column, then use it as the first index key, like this: 

Loading...

CREATE TABLE Events ( UserId String(MAX), Timestamp TIMESTAMP, TimestampShardId INT64, EventData) PRIMARY KEY (UserId, Timestamp DESC); CREATE INDEX EventsByTimestamp ON Events (TimestampShardId,Timestamp);

This will remove the hotspot on index update, but will slow down range queries on timestamp, since you’ll have to run the query for each ShardId value (0-99) to get the timestamp range from all shards: 

Loading...

Select * from Events@{FORCE_INDEX=EventsByTimestamp} WHERE TimestampShardId BETWEEN 0 AND 99 AND Timestamp > @lower_bound AND Timestamp < @upper_bound;

Using this type of index and sharding strategy must strike a balance between the additional complexity when reading and the increase in performance of an indexed query.   


###  Other indexes you should know

When you’re migrating to Cloud Spanner, you’ll also want to understand how these other index types function and when you might need to use them:   


###  NULL_FILTERED indexes

By default, Cloud Spanner will index rows using NULL indexed column values. A NULL is considered to be the smallest possible value, so these values will appear at the start of the index.

It’s also possible to disable this behavior by using the [CREATE NULL_FILTERED INDEX](https://cloud.google.com/spanner/docs/secondary-indexes#indexing_of_nulls) syntax, which will create an index ignoring rows with NULL indexed column values.

This index will be smaller than the complete index, as it will effectively be a materialized filtered view on the table, and will be faster to query than the full table when a table scan is necessary. 

###  UNIQUE indexes

You can use a [UNIQUE](https://cloud.google.com/spanner/docs/secondary-indexes#unique_indexes) index to enforce that a column of a table has unique values. This constraint will be applied at transaction commit time (and at index creation).

###  Covering Indexes and STORING clause

To optimize performance when reading from indexes, Cloud Spanner can store the column values of the table row in the index itself, removing the need to read the table. This is known as a Covering Index. This is achieved by using the STORING clause when defining the index. The values of the column can then be read directly from the index, so reading from the index performs as well as reading from the table. For example, this table contains employee data: 

Loading...

CREATE TABLE Employees ( CompanyUUID INT64, EmployeeUUID INT64, FullName STRING(MAX) ... ) PRIMARY KEY (CompanyUUID,EmployeeUUID)

If you often need to look up an employee’s full name, for example, you can create an index on employeeUUID, storing the full name for rapid lookups: 

Loading...

CREATE INDEX EmployeesById ON Employees (EmployeeUUID) STORING (FullName);

###  Forcing index use

Cloud Spanner’s query engine will only automatically use indexes in rare circumstances (when it is a query fully covered by the index), so it is important to use a FORCE_INDEX directive in the SQL SELECT statement to ensure that Cloud Spanner looks up values from the index. (You can find more details in the [documentation](https://cloud.google.com/spanner/docs/secondary-indexes#index_directive).) 

Loading...

Select * from Employees@{FORCE_INDEX=EmployeesById} Where EmployeeUUID=xxx;

Note that when using the Cloud Spanner Read APIs, you can only perform fully covered queries—i.e., queries where the index stores all of the columns requested. To read the columns from the original table using an index, you must use an SQL query. See Use a Secondary Index section of the Getting Started docs for examples.

###  Continuing your Cloud Spanner education

There are some big conceptual differences when you’re using a cloud-built, horizontally scalable database like Cloud Spanner in contrast with the RDBMS you’ve been using for years. Once you’re familiar with the way keys and indexes work, you can start to take advantage of the benefits of Cloud Spanner for faster scalability.

In the next episode of this series, we will look at how to deal with business logic that would previously be implemented by triggers and stored procedures, neither of which exist in Cloud Spanner.

Want to learn more about Cloud Spanner in person? We’ll be discussing data migration and more [in this session](https://cloud.withgoogle.com/next18/sf/sessions/session/156790) at Next 2018 in July. For more information, and to register, visit the [Next ‘18 website](https://goo.gl/fo1kgH).

###  Related content:

[How we used Cloud Spanner to build our email personalization system—from “Soup” to nuts](https://cloudplatform.googleblog.com/2018/03/how-we-used-Cloud-Spanner-to-build-our-email-personalization-system-from-Soup-to-nuts.html)  
[Why you should pick strong consistency, whenever possible](https://cloudplatform.googleblog.com/2018/01/why-you-should-pick-strong-consistency-whenever-possible.html)

[Sharding of timestamp-ordered data in Cloud Spanner](https://cloudplatform.googleblog.com/2018/05/Sharding-of-timestamp-ordered-data-in-Cloud-Spanner.html)

Posted in

  * [Google Cloud](https://cloud.google.com/blog/products/gcp)
  * [Databases](https://cloud.google.com/blog/products/databases)
  * [Solutions and How-to's](https://cloud.google.com/blog/topics/solutions-how-tos)
  * [Spanner](https://cloud.google.com/blog/products/spanner)



##### Related articles

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/whats_new_2026_CfhxFWX.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/whats_new_2026_CfhxFWX.max-700x700.jpg)Inside Google CloudWhat’s new with Google CloudBy Google Cloud Content & Editorial • 44-minute read](https://cloud.google.com/blog/topics/inside-google-cloud/whats-new-google-cloud)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/latam-midsize-biz-hero.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/latam-midsize-biz-hero.max-700x700.png)CustomersHow growing Latin American midsize businesses are building in the AI eraBy Andre Alves • 8-minute read](https://cloud.google.com/blog/topics/customers/how-midsize-latam-companies-build-with-ai)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/google_ai_this_month.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/google_ai_this_month.max-700x700.jpg)AI & Machine LearningWhat Google Cloud announced in AI this monthBy Andrea Morange • 29-minute read](https://cloud.google.com/blog/products/ai-machine-learning/what-google-cloud-announced-in-ai-this-month)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/monthly_ai_news.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/monthly_ai_news.max-700x700.png)AI & Machine LearningWhat Google Cloud announced in AI this month - 2025By Andrea Morange • 43-minute read](https://cloud.google.com/blog/products/ai-machine-learning/what-google-cloud-announced-in-ai-this-month-2025)
