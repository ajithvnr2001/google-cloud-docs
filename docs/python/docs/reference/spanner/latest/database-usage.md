---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/database-usage/
title: Database Admin Usage \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:48.636419+00:00
---

# Database Admin Usage  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/database-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Database Admin Usage Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 

After creating an [`Instance`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance), you can interact with individual databases for that instance.

## List Databases

To iterate over all existing databases for an instance, use its [`list_databases()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance.list_databases) method:
    
    
    for database in instance.list_databases():
        # `database` is a `Database` object.
    

This method yields [`Database`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database) objects.

## Database Factory

To create a [`Database`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database) object:
    
    
    database = instance.database(database_id, ddl_statements)
    

  * `ddl_statements` is a list of strings containing DDL statements for the new database.



You can also use the [`database()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance.database) method on an [`Instance`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance) object to create a local wrapper for a database that has already been created:
    
    
    database = instance.database(existing_database_id)
    

## Create a new Database

After creating the database object, use its [`create()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database.create) method to trigger its creation on the server:
    
    
    operation = database.create()
    

**NOTE** : Creating a database triggers a “long-running operation” and returns a [`Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future)-like object. Use the [`result()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.result) method to wait for and inspect the result.

## Update an existing Database

After creating the database object, you can apply additional DDL statements via its [`update_ddl()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database.update_ddl) method:
    
    
    operation = database.update_ddl(ddl_statements, operation_id)
    

  * `ddl_statements` is a list of strings containing DDL statements to be applied to the database.

  * `operation_id` is a string ID for the long-running operation.




**NOTE** : Updating a database triggers a “long-running operation” and returns an `Operation` object. See Check on Current Database Operation for polling to find out if the operation is completed.

## Drop a Database

Drop a database using its [`drop()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database.drop) method:
    
    
    database.drop()
    

## Check on Current Database Operation

The [`create()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database.create) and [`update_ddl()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database.update_ddl) methods of the [`Database`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database) object trigger long-running operations on the server, and return operations conforming to the [`Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future) class.
    
    
    >>> operation = database.create()
    >>> operation.result()
    

# Non-Admin Database Usage

## Use a Snapshot to Read / Query the Database

A snapshot represents a read-only point-in-time view of the database.

Calling [`snapshot()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database.snapshot) with no arguments creates a snapshot with strong concurrency:
    
    
    with database.snapshot() as snapshot:
        do_something_with(snapshot)
    

See [`Snapshot`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/snapshot#google.cloud.spanner_v1.snapshot.Snapshot) for the other options which can be passed.

**NOTE** : [`snapshot()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database.snapshot) returns an object intended to be used as a Python context manager (i.e., as the target of a `with` statement). Perform all iterations within the context of the `with database.snapshot()` block.

See [Read-only Transactions via Snapshots](https://docs.cloud.google.com/python/docs/reference/spanner/latest/snapshot-usage) for more complete examples of snapshot usage.

## Use a Batch to Modify Rows in the Database

A batch represents a bundled set of insert/upsert/update/delete operations on the rows of tables in the database.
    
    
    with database.batch() as batch:
         batch.insert_or_update(table, columns, rows)
         batch.delete(table, keyset_to_delete)
    

**NOTE** : [`batch()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database.batch) returns an object intended to be used as a Python context manager (i.e., as the target of a `with` statement). It applies any changes made inside the block of its `with` statement when exiting the block, unless an exception is raised within the block. Use the batch only inside the block created by the `with` statement.

See [Batching Modifications](https://docs.cloud.google.com/python/docs/reference/spanner/latest/batch-usage) for more complete examples of batch usage.

## Use a Transaction to Query / Modify Rows in the Database

A transaction represents the union of a “strong” snapshot and a batch: it allows `read` and `execute_sql` operations, and accumulates insert/upsert/update/delete operations.

Because other applications may be performing concurrent updates which would invalidate the reads / queries, the work done by a transaction needs to be bundled as a retryable “unit of work” function, which takes the transaction as a required argument:
    
    
    def unit_of_work(transaction):
        result = transaction.execute_sql(QUERY)
    
        for emp_id, hours, pay in _compute_pay(result):
            transaction.insert_or_update(
                table='monthly_hours',
                columns=['employee_id', 'month', 'hours', 'pay'],
                values=[emp_id, month_start, hours, pay])
    
    database.run_in_transaction(unit_of_work)
    

**NOTE** : [`run_in_transaction()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database.run_in_transaction) commits the transaction automatically if the “unit of work” function returns without raising an exception.

**NOTE** : [`run_in_transaction()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database.run_in_transaction) retries the “unit of work” function if the read / query operations or the commit are aborted due to concurrent updates.

See [Read-write Transactions](https://docs.cloud.google.com/python/docs/reference/spanner/latest/transaction-usage) for more complete examples of transaction usage.

## Configuring a session pool for a database

Under the covers, the `snapshot`, `batch`, and `run_in_transaction` methods use a pool of [`Session`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/session#google.cloud.spanner_v1.session.Session) objects to manage their communication with the back-end. You can configure one of the pools manually to control the number of sessions, timeouts, etc., and then pass it to the [`Database`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database) constructor:
    
    
    from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
    
    # Instantiate the Spanner client, and get the appropriate instance.
    client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
    instance = [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_instance)(INSTANCE_NAME)
    
    # Create a database with a pool of a fixed size.
    pool = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[FixedSizePool](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.FixedSizePool.html)(size=10, default_timeout=5)
    database = instance.database(DATABASE_NAME, pool=pool)
    

Note that creating a database with a pool will require the database to already exist if the pool implementation needs to pre-create sessions (rather than creating them on demand, as the default implementation does).

You can supply your own pool implementation, which must satisfy the contract laid out in [`AbstractSessionPool`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/session#google.cloud.spanner_v1.pool.AbstractSessionPool):
    
    
    from google.cloud.spanner import [AbstractSessionPool](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.AbstractSessionPool.html)
    
    class MyCustomPool(AbstractSessionPool):
    
         def __init__(self, database, custom_param):
             super(MyCustomPool, self).__init__(database)
             self.custom_param = custom_param
    
         def get(self, read_only=False):
             ...
    
         def put(self, session, discard_if_full=True):
             ...
    
    database = instance.database(DATABASE_NAME, pool=pool)
    pool = MyCustomPool(database, custom_param=42)
    

See [Advanced Session Pool Topics](https://docs.cloud.google.com/python/docs/reference/spanner/latest/advanced-session-pool-topics) for more advanced coverage of session pools.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
