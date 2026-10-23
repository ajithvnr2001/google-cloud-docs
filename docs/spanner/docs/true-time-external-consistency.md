---
url: https://docs.cloud.google.com/spanner/docs/true-time-external-consistency/
title: Spanner: TrueTime and external consistency \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:10.002740+00:00
---

# Spanner: TrueTime and external consistency  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/true-time-external-consistency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Spanner: TrueTime and external consistency Stay organized with collections  Save and categorize content based on your preferences. 

TrueTime is a highly available, distributed clock that is provided to applications on all Google servers1. TrueTime enables applications to generate monotonically increasing timestamps: an application can compute a timestamp T that is guaranteed to be greater than any timestamp T', if T' finished being generated before T started being generated. This guarantee holds across all servers and all timestamps.

This feature of TrueTime is used by Spanner to assign timestamps to transactions. Specifically, every transaction is assigned a timestamp that reflects the instant at which Spanner considers it to have occurred. Because Spanner uses multi-version concurrency control (MVCC), the ordering guarantee on timestamps enables clients of Spanner to perform consistent reads across an entire database (even across multiple Cloud [regions](https://cloud.google.com/about/locations)) without blocking writes.

## External consistency

When the isolation level is unspecified, or when you set the isolation level as serializable isolation, Spanner provides clients with the strictest concurrency-control guarantees for transactions, which is called _external consistency_ 2. Under external consistency, the system behaves as if all transactions run sequentially, even though Spanner actually runs them across multiple servers (and possibly in multiple datacenters) for higher performance and availability. In addition, if one transaction completes before another transaction starts to commit, the system guarantees that clients can never see a state that includes the effect of the second transaction but not the first. Intuitively, Spanner is semantically indistinguishable from a single-machine database. Even though it provides such strong guarantees, Spanner enables applications to achieve performance comparable to databases that provide weaker guarantees (in return for higher performance). By default, Spanner allows writes to proceed without being blocked by read-only transactions, but without exhibiting the anomalies that repeatable read isolation allows.

On the other hand, repeatable read isolation ensures that all read operations within a transaction see a consistent snapshot of the database as it existed at the start of the transaction. This approach is beneficial in high read-write concurrency scenarios where numerous transactions read data that other transactions might be modifying. For more information, see [repeatable read isolation](https://docs.cloud.google.com/spanner/docs/isolation-levels#repeatable-read).

External consistency greatly simplifies application development. For example, suppose that you have created a banking application on Spanner and one of your customers starts with $50 in their checking account and $50 in their savings account. Your application then begins a workflow in which it first commits a transaction T1 to deposit $200 into the savings account, and then issues a second transaction T2 to debit $150 from the checking account. Further, assume that at the end of the day, negative balances in one account are covered automatically from other accounts, and a customer incurs a penalty if the total balance across all their accounts is negative at any time during that day. External consistency guarantees that because T2 starts to commit after T1 finishes, then all readers of the database will observe that the deposit T1 occurred before the debit T2. Put another way, external consistency guarantees that no one will ever see a state where T2 occurs prior to T1; in other words, the debit will never incur a penalty due to insufficient funds.

A traditional database that uses single-version storage and strict two-phase locking provides external consistency. Unfortunately, in such a system, every time your application wants to read the most current data (which we call a "strong read"), the system acquires a read lock on the data, which blocks writes to the data being read.

## Timestamps and MVCC

To read without blocking writes, Spanner and many other database systems keep multiple immutable versions of data (often called _multi-version concurrency control_). A write creates a new immutable version whose timestamp is that of the write's transaction. A "snapshot read" at a timestamp returns the value of the most recent version prior to that timestamp, and doesn't need to block writes. It is therefore important that the timestamps assigned to versions be consistent with the order in which transactions can be observed to commit. We call this property "proper timestamping", which is equivalent to external consistency.

To see why proper timestamping is important, consider the banking example from the previous section. Without proper timestamping, T2 might be assigned a timestamp that is earlier than the timestamp assigned to T1 (for example, if a hypothetical system used local clocks instead of TrueTime, and the clock of the server that processes T2 lagged slightly). A snapshot read might then reflect the debit from T2 but not the deposit T1, even though the customer saw the deposit finish before starting the debit.

Achieving proper timestamping is trivial for a single-machine database (for example, you can just assign timestamps from a global, monotonically increasing counter). Achieving it in a widely distributed system such as Spanner, in which servers all over the world need to assign timestamps, is much more difficult to do efficiently.

Spanner depends on TrueTime to generate monotonically increasing timestamps. Spanner uses these timestamps in two ways. First, it uses them as proper timestamps for write transactions without the need for global communication. Second, it uses them as timestamps for strong reads, which enables strong reads to execute in one round of communication, even strong reads that span multiple servers.

## FAQs

### What consistency guarantees does Spanner provide?

By default, Spanner provides external consistency, which is the strictest consistency property for transaction-processing systems. All transactions in Spanner that use serializability isolation satisfy this consistency property, not just those within a partition. For more information, see [Isolation levels overview](https://docs.cloud.google.com/spanner/docs/isolation-levels).

External consistency states that Spanner executes transactions in a manner that is indistinguishable from a system in which the transactions are executed serially, and furthermore, that the serial order is consistent with the order in which transactions can be observed to commit. Because the timestamps generated for transactions correspond to the serial order, if any client sees a transaction T2 start to commit after another transaction T1 finishes, the system will assign a timestamp to T2 that is higher than T1's timestamp.

### Does Spanner provide linearizability?

Yes. By default, Spanner provides external consistency, which is a stronger property than linearizability, because linearizability doesn't say anything about the behavior of transactions. Linearizability is a property of concurrent objects that support atomic read and write operations. In a database, an "object" would typically be a single row or even a single cell. External consistency is a property of transaction-processing systems, where clients dynamically synthesize transactions that contain multiple read and write operations on arbitrary objects. Linearizability can be viewed as a special case of external consistency, where a transaction can only contain a single read or write operation on a single object.

### Does Spanner provide serializability?

Yes. By default, Spanner provides external consistency, which is a stricter property than serializability. A transaction-processing system is serializable if it executes transactions in a manner that is indistinguishable from a system in which the transactions are executed serially. Spanner also guarantees that the serial order is consistent with the order in which the transactions can be observed to commit.

Consider again the banking example used earlier. In a system that provides serializability but not external consistency, even though the customer executed T1 and then T2 sequentially, the system would be permitted to reorder them, which might cause the debit to incur a penalty due to insufficient funds.

### Does Spanner provide strong consistency?

Yes. Spanner provides external consistency, which is a stronger property than strong consistency. The default mode for [reads](https://docs.cloud.google.com/spanner/docs/reads) in Spanner is "strong", which guarantees that they observe the effects of all transactions that committed before the start of the operation, independent of which replica receives the read.

### What is the difference between strong consistency and external consistency?

A replication protocol exhibits strong consistency if the replicated objects are linearizable. Like linearizability, strong consistency is weaker than external consistency, because it doesn't enforce anything about the behavior of transactions.

### Does Spanner provide eventual (or lazy) consistency?

Spanner provides external consistency, which is a much stronger property than eventual consistency. Eventual consistency trades weaker guarantees for higher performance. Eventual consistency is problematic because it means that readers can observe the database in a state that never existed (for example, a read could observe a state where Transaction B is committed but Transaction A is not, even though A happened before B).

Spanner provides [stale reads](https://docs.cloud.google.com/spanner/docs/timestamp-bounds#bounded_staleness), which offer similar performance benefits as eventual consistency but with much stronger consistency guarantees. A stale read returns data from an earlier timestamp, which can't block writes because previous versions of data are immutable.

## What's next

  * [Spanner transaction semantics](https://docs.cloud.google.com/spanner/docs/transactions#rw_transaction_semantics)
  * [Spanner, TrueTime, and the CAP Theorem](https://research.google/pubs/spanner-truetime-and-the-cap-theorem/)



## Notes

* 1 _J. C. Corbett, J. Dean, M. Epstein, A. Fikes, C. Frost, J. Furman, S. Ghemawat, A. Gubarev, C. Heiser, P. Hochschild, W. Hsieh, S. Kanthak, E. Kogan, H. Li, A. Lloyd, S. Melnik, D. Mwaura, D. Nagle, S. Quinlan, R. Rao, L. Rolig, Y. Saito, M. Szymaniak, C. Taylor, R. Wang, and D. Woodford.[Spanner: Google's Globally-Distributed Database](https://research.google.com/archive/spanner.html). In Tenth USENIX Symposium on Operating Systems Design and Implementation (OSDI 12), pp. 261–264, Hollywood, CA, Oct. 2012._

* 2 _Gifford, D. K. Information Storage in a Decentralized Computer System. PhD thesis, Stanford University, 1981._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
