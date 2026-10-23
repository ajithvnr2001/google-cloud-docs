---
url: https://docs.cloud.google.com/solutions/sequence-generation-in-cloud-spanner/
title: Sequence generation in Spanner \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:46:18.701530+00:00
---

# Sequence generation in Spanner  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/sequence-generation-in-cloud-spanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Sequence generation in Spanner Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Spanner now supports [automatically generated primary key values](https://docs.cloud.google.com/spanner/docs/primary-key-default-value). We strongly recommend using this built-in sequence. For more information, see [Simplifying best practices at scale with auto-generated keys in Spanner](https://cloud.google.com/blog/products/databases/announcing-support-for-auto-generated-keys-in-spanner). Only use the methods described in this document after careful investigation that the built-in sequence doesn't work for your needs. These methods require more effort to orchestrate, might impact your database performance, and their monotonically increasing values increase risks of hotspotting when used as primary keys.

This document describes methods for database administrators and application developers to generate unique numeric sequences in applications that use Spanner.

## Introduction

There are often situations where a business requires a simple, unique numerical ID. for example, an employee number or an invoice number. Conventional relational databases often include a feature for generating unique, monotonically increasing sequences of numbers. These sequences are used to generate unique identifiers (row keys) for objects stored in the database.

However, using monotonically increasing (or decreasing) values as row keys might not follow [best practices](https://docs.cloud.google.com/spanner/docs/schema-design#choose_a_primary_key_to_prevent_hotspots) in Spanner because it creates hotspots in the database, leading to a reduction in performance. This document proposes mechanisms for implementing a sequence generator by using a Spanner database table and application layer logic.

Alternatively, Spanner supports a built-in bit-reversed sequence generator. For more information on the Spanner sequence generator, see [Create and manage sequences](https://docs.cloud.google.com/spanner/docs/sequence-tasks).

### Requirements for a sequence generator

Every sequence generator must generate a unique value for each transaction.

Depending on the use case, a sequence generator might also need to create sequences with the following characteristics:

  * Ordered: Lower values in the sequence must not be issued after higher values.
  * Gapless: There must be no gaps in the sequence.



The sequence generator must also generate values at the frequency required by the application.

It can be difficult to meet all of these requirements, especially in a distributed system. If necessary to meet your performance objectives, you can make compromises in the requirements that the sequence be ordered and gapless.

Other database engines have ways of handling these requirements. For example, sequences in PostgreSQL and AUTO_INCREMENT columns in MySQL can generate unique values for separate transactions, but can't produce gapless values if transactions are rolled back. For more information, see [Notes in PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-createsequence.html)) and [AUTO_INCREMENT implications in MySQL](https://dev.mysql.com/doc/refman/8.0/en/innodb-auto-increment-handling.html#innodb-auto-increment-lock-mode-usage-implications)).

### Sequence generators using database table rows

Your application can implement a sequence generator by using a database table to store the sequence names and the next value in the sequence.

Reading and incrementing the sequence's `next_value` cell inside a database transaction generates unique values, without requiring any further synchronization between application processes.

First, define the table as follows:
    
    
    CREATE TABLE sequences (
        name STRING(64) NOT NULL,
        next_value INT64 NOT NULL,
    ) PRIMARY KEY (name)
    

You can create sequences by inserting a row in the table with the new sequence name and the starting value—for example, `("invoice_id", 1)`. However, because the `next_value` cell is incremented for every sequence value generated, the performance is limited by how frequently the row can be updated.

[Spanner Client Libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries) uses [retryable transactions](https://docs.cloud.google.com/spanner/docs/transactions#rw_transaction_interface) to resolve conflicts. If any cells (column values) read during a read-write transaction are modified elsewhere, the transaction will be blocked until the other transaction completes, then will abort and be retried so that it reads the updated values. This minimizes the duration of write locks, but also means that a transaction might be attempted multiple times before it successfully commits.

Because only one transaction can occur on a row at a time, the maximum frequency of issuing sequence values is inversely proportional to the total latency of the transaction.

This total transaction latency depends on several factors, such as the latency between the client application and the Spanner nodes, the latency between the Spanner nodes, and the [TrueTime](https://docs.cloud.google.com/spanner/docs/true-time-external-consistency) uncertainty. For example, multi-regional configuration has a higher transaction latency because it must wait for a quorum of write confirmations from the nodes in different regions in order to complete.

For example, if a read-update transaction on a single cell (one column in a single row) has a latency of 10 milliseconds (ms), then the maximum _theoretical_ frequency of issuing of sequence values is 100 per second. This maximum applies to the entire database, regardless of the number of client application instances, or the number of nodes in the database. This is because a single row is always managed by a single node.

The following section describes ways to work around this limitation.

### Application-side implementation

The application code needs to read and update the `next_value` cell in the database. There are multiple ways of doing this, each of which have different performance characteristics and drawbacks.

#### Simple within-transaction sequence generator

The simplest way to handle sequence generation is to increment the column value within the transaction whenever the application needs a new sequential value.

In a single transaction, the application does the following:

  * Reads the `next_value` cell for the sequence name to be used in the application.
  * Increments and updates the `next_value` cell for the sequence name.
  * Uses the retrieved value for whatever column value the application needs.
  * Completes the rest of the application's transaction.



This process generates a sequence that's in order and gapless. If nothing updates the `next_value` cell in the database to a lower value, the sequence will also be unique.

Because the sequence value is retrieved as part of the broader application transaction, the maximum frequency of sequence generation depends on how complex the overall application transaction is. A complex transaction will have a higher latency and, therefore, a lower maximum possible frequency.

In a distributed system, many transactions might be attempted at the same time, leading to high contention on the sequence value. Because the `next_value` cell is updated within the application's transaction, any other transactions attempting to increment the `next_value` cell at the same time will be blocked by the first transaction and [will be re-tried](https://docs.cloud.google.com/spanner/docs/transactions#rw_transaction_interface). This leads to large increases in the time required for the application to successfully complete the transaction, which can cause performance issues.

The following code provides an example of a simple in-transaction sequence generator that returns only a single sequence value per transaction. This restriction exists because writes within a transaction using the [Mutation API](https://docs.cloud.google.com/spanner/docs/modify-mutation-api) aren't visible until after the transaction commits, even to reads in the same transaction. Therefore, calling this function multiple times in the same transaction will always return the same sequence value.

The following example code shows how to implement a synchronous `getNext()` function: 
    
    
    /**
     * Returns the next value from this sequence.
     *
     * <p>Should only be called once per transaction.
     */
    long getNext(TransactionContext txn) {
      Struct result =
          txn.readRow(
              SEQUENCES_TABLE, Key.of(sequenceName), Collections.singletonList(NEXT_VALUE_COLUMN));
      if (result == null) {
        throw new NoSuchElementException(
            "Sequence " + sequenceName + " not found in table " + SEQUENCES_TABLE);
      }
      long value = result.getLong(0);
      txn.buffer(
          Mutation.newUpdateBuilder(SEQUENCES_TABLE)
              .set(SEQUENCE_NAME_COLUMN)
              .to(sequenceName)
              .set(NEXT_VALUE_COLUMN)
              .to(value + 1)
              .build());
      return value;
    }

The following example code shows how the synchronous `getNext()` function is used in a transaction:
    
    
    // Simple Sequence generator created outside transaction, eg as field.
    private SimpleSequenceGenerator simpleSequence = new SimpleSequenceGenerator("my Sequence");
    
    public void usingSimpleSequenceGenerator() {
      dbClient
          .readWriteTransaction()
          .run(
              new TransactionCallable<Void>() {
                @Nullable
                @Override
                public Void run(TransactionContext txn) {
                  // Get a sequence value
                  long nextValue = simpleSequence.getNext(txn);
                  // Use nextValue in the transaction
                  // ...
                  return null;
                }
              });
    }

#### Improved within-transaction, synchronous sequence generator

You can modify the preceding abstraction to produce multiple values within a single transaction by keeping track of the sequence values issued within a transaction.

In a single transaction, the application does the following:

  * Reads the `next_value` cell for the sequence name to use in the application.
  * Stores this value as a variable internally.
  * Each time a new sequence value is requested, increments the stored `next_value` variable and buffers a write that sets the updated cell value in the database.
  * Completes the rest of the application's transaction.



If you're using an abstraction, the object for this abstraction must be created within the transaction. The object performs a single read when the first value is requested. The object keeps track internally of the `next_value` cell, so that more than one value can be generated.

The same caveats regarding latency and contention that applied to the previous version also apply to this version.

The following example code shows how to implement a synchronous `getNext()` function:
    
    
    private final TransactionContext txn;
    @Nullable private Long nextValue;
    
    /** Creates a sequence generator for this transaction. */
    public SynchronousSequenceGenerator(String sequenceName, TransactionContext txn) {
      super(sequenceName);
      this.txn = txn;
    }
    
    /**
     * Returns the next value from this sequence.
     *
     * <p>Can be called multiple times in a transaction.
     */
    public long getNext() {
      if (nextValue == null) {
        // nextValue is unknown - read it.
        Struct result =
            txn.readRow(
                SEQUENCES_TABLE, Key.of(sequenceName), Collections.singletonList(NEXT_VALUE_COLUMN));
        if (result == null) {
          throw new NoSuchElementException(
              "Sequence " + sequenceName + " not found in table " + SEQUENCES_TABLE);
        }
        nextValue = result.getLong(0);
      }
      long value = nextValue;
      // increment and write nextValue to the database.
      nextValue++;
      txn.buffer(
          Mutation.newUpdateBuilder(SEQUENCES_TABLE)
              .set(SEQUENCE_NAME_COLUMN)
              .to(sequenceName)
              .set(NEXT_VALUE_COLUMN)
              .to(nextValue)
              .build());
      return value;
    }

The following example code shows how to use the synchronous `getNext()` function in a request for two sequence values:
    
    
    public void usingSynchronousSequenceGenerator() {
      dbClient
          .readWriteTransaction()
          .run(
              new TransactionCallable<Void>() {
                @Nullable
                @Override
                public Void run(TransactionContext txn) {
                  // Create the sequence generator object within the transaction
                  SynchronousSequenceGenerator syncSequence =
                      new SynchronousSequenceGenerator("my_sequence", txn);
                  // Get two sequence values
                  long key1 = syncSequence.getNext();
                  long key2 = syncSequence.getNext();
                  // Use the 2 key values in the transaction
                  // ...
                  return null;
                }
              });
    }

#### Out-of-transaction (asynchronous) sequence generator

In the previous two implementations, the performance of the generator depends on the latency of the application's transaction. You can improve maximum frequency—at the expense of tolerating gaps in the sequence—by incrementing the sequence in a _separate_ transaction. (This is the approach used by [PostgreSQL](https://www.postgresql.org/).) You should retrieve the sequence values to be used first, before the application starts its transaction.

The application does the following:

  * Creates a first transaction to get and update the sequence value: 
    * Reads the `next_value` cell for the sequence name to use in the application.
    * Stores this value as a variable.
    * Increments and updates the `next_value` cell in the database for the sequence name.
    * Completes the transaction.
  * Uses the returned value in a separate transaction.



The latency of this separate transaction will be close to the minimum latency, with performance approaching the maximum theoretical frequency of 100 values per second (assuming a 10 ms transaction latency). Because the sequence values are retrieved separately, the latency of the application's transaction itself isn't changed, and contention is minimized.

However, if a sequence value is requested and not used, then a gap is left in the sequence because it's not possible to roll back requested sequence values. This can occur if the application aborts or fails during the transaction after requesting a sequence value.

The following example code shows how to implement a function that retrieves and increments the `next_value` cell in the database:
    
    
    /**
     * Gets the next sequence value from the database, and increments the database value by the amount
     * specified in a single transaction.
     */
    protected Long getAndIncrementNextValueInDB(long increment) {
      return dbClient
          .readWriteTransaction()
          .run(
              txn -> {
                Struct result =
                    txn.readRow(
                        SEQUENCES_TABLE,
                        Key.of(sequenceName),
                        Collections.singletonList(NEXT_VALUE_COLUMN));
                if (result == null) {
                  throw new NoSuchElementException(
                      "Sequence " + sequenceName + " not found in table " + SEQUENCES_TABLE);
                }
                long value = result.getLong(0);
                txn.buffer(
                    Mutation.newUpdateBuilder(SEQUENCES_TABLE)
                        .set(SEQUENCE_NAME_COLUMN)
                        .to(sequenceName)
                        .set(NEXT_VALUE_COLUMN)
                        .to(value + increment)
                        .build());
                return value;
              });
    }

You can easily use this function to retrieve a single new sequence value, as shown in the following implementation of an asynchronous `getNext()` function:
    
    
    /**
     * Returns the next value from this sequence.
     *
     * Uses a separate transaction so must be used <strong>outside</strong>any other transactions.
     * See {@link #getNextInBackground()} for an alternative version that uses a background thread
     */
    public long getNext() throws SpannerException {
      return getAndIncrementNextValueInDB(1);
    }

The following example code shows how to use the asynchronous `getNext()` function in a request for two sequence values:
    
    
    // Async Sequence generator created outside transaction as a long-lived object.
    private AsynchronousSequenceGenerator myAsyncSequence =
        new AsynchronousSequenceGenerator("my Sequence", dbClient);
    
    public void usingAsynchronousSequenceGenerator() {
      // Get two sequence values
      final long key1 = myAsyncSequence.getNext();
      final long key2 = myAsyncSequence.getNext();
      dbClient
          .readWriteTransaction()
          .run(
              new TransactionCallable<Void>() {
                @Nullable
                @Override
                public Void run(TransactionContext txn) {
                  // Use the 2 key values in the transaction
                  // ...
                  return null;
                }
              });
    }

In the preceding code example, you can see that the sequence values are requested outside of the application's transaction. This is because Cloud Spanner does not support running a transaction inside another transaction in the same thread (also known as nested transactions).

You can work around this restriction by requesting the sequence value by using a background thread and waiting for the result:
    
    
    protected static final ExecutorService executor = Executors.newCachedThreadPool();
    
    /**
     * Gets the next value using a background thread - to be used when inside a transaction to avoid
     * Nested Transaction errors.
     */
    public long getNextInBackground() throws Exception {
      return executor.submit(this::getNext).get();
    }

#### Batch sequence generator

You can gain significant performance improvement if you also drop the requirement that sequence values must be in order. This lets the application reserve a batch of sequence values and issue them internally. Individual application instances have their own separate batch of values, so the values being issued aren't in order. In addition, application instances that don't use their entire batch of values (for example, if the application instance is shut down) will leave gaps of unused values in the sequence.

The application will do the following:

  * Maintain an internal state for each sequence that contains the starting value and the size of the batch, and the next value available.
  * Request a sequence value from the batch.
  * If there are no remaining values in the batch, do the following: 
    * Create a transaction to read and update the sequence value.
    * Read the `next_value` cell for the sequence.
    * Store this value internally as the starting value of the new batch.
    * Increment the `next_value` cell in the database by an amount equal to the batch size.
    * Complete the transaction.
  * Return the next available value and increment the internal state.
  * Use the returned value in the transaction.



With this method, transactions that use a sequence value will experience an increase in latency only when a new batch of sequence values needs to be reserved.

The advantage is that by increasing the batch size, performance can be increased to any level, because the limiting factor becomes the number of batches issued per second.

For example, with a batch size of 100—assuming a 10 ms latency to get a new batch, and therefore a maximum of 100 batches per second—10,000 sequence values per second can be issued.

The following example code shows how to implement a `getNext()` function by using batches. Notice that the code reuses the `getAndIncrementNextValueInDB()` function defined previously to retrieve new batches of sequence values from the database.
    
    
    /**
     * Gets a new batch of sequence values from the database.
     *
     * <p>Reads next_value, increments it by batch size, then writes the updated next_value back.
     */
    private synchronized void getBatch() throws SpannerException {
      if (next_value <= last_value_in_batch) {
        // already have some values left in the batch - maybe this has been refreshed by another
        // thread.
        return;
      }
      next_value = getAndIncrementNextValueInDB(batchSize);
      last_value_in_batch = next_value + batchSize - 1;
    }
    
    /**
     * Returns the next value from this sequence, getting a new batch of values if necessary.
     *
     * When getting a new batch, it creates a separate transaction, so this must be called
     * <strong>outside</strong> any other transactions. See {@link #getNextInBackground()} for an
     * alternative version that uses a background thread
     */
    
    public synchronized long getNext() throws SpannerException {
      if (next_value > last_value_in_batch) {
        getBatch();
      }
      long value = next_value;
      next_value++;
      return value;
    }

The following example code shows how to use the asynchronous `getNext()` function in a request for two sequence values:
    
    
    // Batch Sequence generator created outside transaction, as a long-lived object.
    private BatchSequenceGenerator myBatchSequence =
        new BatchSequenceGenerator("my Sequence", /* batchSize= */ 100, dbClient);
    
    public void usingBatchSequenceGenerator() {
      // Get two sequence values
      final long key1 = myBatchSequence.getNext();
      final long key2 = myBatchSequence.getNext();
      dbClient
          .readWriteTransaction()
          .run(
              new TransactionCallable<Void>() {
                @Nullable
                @Override
                public Void run(TransactionContext txn) {
                  // Use the 2 key values in the transaction
                  // ...
                  return null;
                }
              });
    }

Again, the values must be requested outside of the transaction (or by using a background thread) because Spanner doesn't support nested transactions.

#### Asynchronous batch sequence generator

For high-performance applications where any increase in latency isn't acceptable, you can improve the performance of the previous batch generator by having a new batch of values ready for when the current batch of values is exhausted.

You can achieve this by setting a threshold that indicates when the number of sequence values remaining in a batch is too low. When the threshold is reached, the sequence generator starts requesting a new batch of values in a background thread.

As with the previous version, values are not issued in order, and there will be gaps of unused values in the sequence if transactions fail or if application instances are shut down.

The application will do the following:

  * Maintain an internal state for each sequence, containing the starting value of the batch and the next value available.
  * Request a sequence value from the batch.
  * If the remaining values in the batch are fewer than the threshold, then do the following in a background thread: 
    * Create a transaction to read and update the sequence value.
    * Read the `next_value` cell for the sequence name to be used in the application.
    * Store this value internally as the starting value of the _next_ batch.
    * Increment the `next_value` cell in the database by an amount equal to the batch size
    * Complete the transaction.
  * If there are no remaining values in the batch, then retrieve the starting value of the next batch from the background thread (waiting for it to complete if necessary), and create a new batch using the retrieved start value as the next value.
  * Return the next value and increment the internal state.
  * Use the returned value in the transaction.



For optimal performance, the background thread should be started and complete before you run out of sequence values in the current batch. Otherwise, the application will need to wait for the next batch, and latency will be increased. Therefore, you'll need to adjust the batch size and low threshold, depending on the frequency of sequence values issued.

For example, assume a 20 ms transaction time to retrieve a new batch of values, a batch size of 1000, and a maximum sequence issuing frequency of 500 values per second (one value every 2 ms). During the 20 ms when a new batch of values is issued, 10 sequence values will be issued. Therefore, the threshold for the number of sequence values remaining should be greater than 10, so that the next batch is available when needed.

The following example code shows how to implement a `getNext()` function by using batches. Notice that the code uses the `getAndIncrementNextValueInDB()` function defined previously to retrieve a batch of sequence values by using a background thread.
    
    
    /**
     * Gets a new batch of sequence values from the database.
     *
     * <p>Reads nextValue, increments it by batch size, then writes the updated nextValue back.
     * Stores the resulting value in  nextBatchStartValue, ready for when the existing pool of values
     * is exhausted.
     */
    private Long readNextBatchFromDB() {
      return getAndIncrementNextValueInDB(batchSize);
    }
    
    /**
     * Returns the next value from this sequence.
     *
     * If the number of remaining values is below the low watermark, this triggers a background
     * request for new batch of values if necessary. Once the current batch is exhausted, then a the
     * new batch is used.
     */
    public synchronized long getNext() throws SpannerException {
      // Check if a batch refresh is required and is not already running.
      if (nextValue >= (lastValueInBatch - lowWaterMarkForRefresh) && pendingNextBatchStart == null) {
        // Request a new batch in the background.
        pendingNextBatchStart = executor.submit(this::readNextBatchFromDB);
      }
    
      if (nextValue > lastValueInBatch) {
        // batch is exhausted, we should have received a new batch by now.
        try {
          // This will block if the transaction to get the next value has not completed.
          long nextBatchStart = pendingNextBatchStart.get();
          lastValueInBatch = nextBatchStart + batchSize - 1;
          nextValue = nextBatchStart;
        } catch (InterruptedException | ExecutionException e) {
          if (e.getCause() instanceof SpannerException) {
            throw (SpannerException) e.getCause();
          }
          throw new RuntimeException("Failed to retrieve new batch in background", e);
        } finally {
          pendingNextBatchStart = null;
        }
      }
      // return next value.
      long value = nextValue;
      nextValue++;
      return value;
    }

The following example code shows how the asynchronous batch `getNext()`function is used in a request for two values to use in the transaction:
    
    
    // Async Batch Sequence generator created outside transaction, as a long-lived object.
    private AsyncBatchSequenceGenerator myAsyncBatchSequence =
        new AsyncBatchSequenceGenerator("my Sequence", /* batchSize= */ 1000, 200, dbClient);
    
    public void usingAsyncBatchSequenceGenerator() {
      dbClient
          .readWriteTransaction()
          .run(
              new TransactionCallable<Void>() {
                @Nullable
                @Override
                public Void run(TransactionContext txn) {
                  // Get two sequence values
                  final long key1 = myBatchSequence.getNext();
                  final long key2 = myBatchSequence.getNext();
                  // Use the 2 key values in the transaction
                  // ...
                  return null;
                }
              });
    }

Notice that in this case the values can be requested inside the transaction, because the retrieval of a new batch of values occurs in a background thread.

#### Summary

The following table compares the characteristics of the four types of sequence generators:

| Synchronous | Asynchronous | Batch | Asynchronous batch  
---|---|---|---|---  
Unique values | Yes | Yes | Yes | Yes  
Globally ordered values | Yes | Yes | No   
But with a high enough load and small enough batch size, values will be close to each other | No   
But with a high enough load and small enough batch size, values will be close to each other  
Gapless | Yes | No | No | No  
Performance | 1/transaction latency,   
(~25 values per second) | 50-100 values per second | 50-100 _batches_ of values per second | 50-100 _batches_ of values per second  
Latency increase | > 10 ms  
Significantly higher with high contention (when a transaction takes a significant amount of time) | 10 ms on every transaction  
Significantly higher with high contention | 10 ms, but only when a new batch of values is retrieved | Zero, if the batch size and low threshold are set to appropriate values  
  
The preceding table also illustrates the fact that you might need to compromise on requirements for globally ordered values and gapless series of values in order to generate unique values, while meeting overall performance requirements.

### Performance testing

You can use a [performance test/analysis](https://github.com/GoogleCloudPlatform/solutions-spanner-sequences/blob/master/src/main/java/com/google/cloud/solutions/spanner/PerformanceTest.java) tool, which is located in the same GitHub repository as the preceding sequence generator classes, to test each of these sequence generators and demonstrate performance and latency characteristics. The tool simulates an application transaction latency of 10 ms and runs several threads simultaneously that request sequence values.

Performance tests need only a single-node Spanner instance to test on because only a single row is being modified.

For example, the following output shows a comparison of performance versus latency in synchronous mode with 10 threads:
    
    
    $ ITERATIONS=2000
    $ MODE=SYNC
    $ NUMTHREADS=10
    $ java -jar sequence-generator.jar \
       $INSTANCE_ID $DATABASE_ID $MODE $ITERATIONS $NUMTHREADS
    2000 iterations (10 parallel threads) in 58739 milliseconds: 34.048928 values/s
    Latency: 50%ile 27 ms
    Latency: 75%ile 31 ms
    Latency: 90%ile 1189 ms
    Latency: 99%ile 2703 ms
    

The following table compares the results for various modes and numbers of parallel threads, including the number of values that can be issued per second, and latency at the 50th, 90th, and 99th percentiles:

Mode and parameters | Num threads | Values/sec | 50th percentile latency (ms) | 90th percentile latency (ms) | 99th percentile  
latency (ms)  
---|---|---|---|---|---  
SYNC | 10 | 34 | 27 | 1189 | 2703  
SYNC | 50 | 30.6 | 1191 | 3513 | 5982  
ASYNC | 10 | 66.5 | 28 | 611 | 1460  
ASYNC | 50 | 78.1 | 29 | 1695 | 3442  
BATCH   
(size 200) | 10 | 494 | 18 | 20 | 38  
BATCH (batch size 200) | 50 | 1195 | 27 | 55 | 168  
ASYNC BATCH  
(batch size 200, LT 50) | 10 | 512 | 18 | 20 | 30  
ASYNC BATCH  
(batch size 200, LT 50) | 50 | 1622 | 24 | 28 | 30  
  
You can see that in synchronous (SYNC) mode, with the increased number of threads, there is increased contention. This leads to significantly higher transaction latencies.

In asynchronous (ASYNC) mode, because the transaction to get the sequence is smaller and separate from the application's transaction, there's less contention and the frequency is higher. However, contention can still occur, leading to higher 90th percentile latencies.

In batch (BATCH) mode, latency is significantly reduced—except for the 99th percentile, which corresponds to when the generator needs to synchronously request another batch of sequence values from the database. Performance is many times higher in BATCH mode than in ASYNC mode.

The 50-thread batch mode has higher latency because sequences are issued so fast that the limiting factor is the power of the virtual machine (VM) instance (in this case, a 4 vCPU machine was running at 350% CPU during the test). Using multiple machines and multiple processes would show overall results similar to the 10-thread batch mode.

In ASYNC BATCH mode the variation in latency is minimal and performance is higher—even with large numbers of threads—because the latency of requesting a new batch from the database is completely independent of the application transaction.

### What's next

  * Learn about the [best practices for schema design](https://docs.cloud.google.com/spanner/docs/schema-design) in Spanner.
  * Read about how to choose [keys and indexes](https://docs.cloud.google.com/blog/products/gcp/what-dbas-need-to-know-about-cloud-spanner-part-1-keys-and-indexes) for Spanner tables.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
