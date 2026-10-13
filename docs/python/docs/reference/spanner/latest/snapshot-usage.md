---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/snapshot-usage/
title: Read-only Transactions via Snapshots \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:49.332038+00:00
---

# Read-only Transactions via Snapshots  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/snapshot-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Read-only Transactions via Snapshots Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 

A [`Snapshot`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/snapshot#google.cloud.spanner_v1.snapshot.Snapshot) represents a read-only transaction: when multiple read operations are performed via a Snapshot, the results are consistent as of a particular point in time.

## Beginning a Snapshot

To begin using a snapshot using the default “bound” (which is “strong”), meaning all reads are performed at a timestamp where all previously-committed transactions are visible:
    
    
    with database.snapshot() as snapshot:
        ...
    

You can also specify a weaker bound, which can either be to perform all reads as of a given timestamp:
    
    
    import datetime
    TIMESTAMP = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    
    with database.snapshot(read_timestamp=TIMESTAMP) as snapshot:
        ...
    

or as of a given duration in the past:
    
    
    import datetime
    DURATION = datetime.timedelta(seconds=5)
    
    with database.snapshot(exact_staleness=DURATION) as snapshot:
        ...
    

## Single Use and Multiple Use Snapshots

In the context of read only transactions, `read` and `execute_sql` methods can be used multiple times if you specify `multi_use=True` in the constructor of the snapshot. However, `multi_use=True` is incompatible with either `max_staleness` and/or `min_read_timestamp`.

Otherwise `multi_use` defaults to `False` and the snapshot cannot be reused.
    
    
    with database.snapshot(multi_use=True) as snapshot:
        ...
    

[`begin()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/snapshot#google.cloud.spanner_v1.snapshot.Snapshot.begin) can only be used on a snapshot with `multi_use=True`. In which case it is also necessary to call if you need to have multiple pending operations.

## Read Table Data

To read data for selected rows from a table in the database, call [`read()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/snapshot#google.cloud.spanner_v1.snapshot.Snapshot.read) which will return all rows specified in `keyset`, or fail if the result set is too large,
    
    
    with database.snapshot() as snapshot:
        result = snapshot.read(
            table='table-name', columns=['first_name', 'last_name', 'age'],
            keyset=spanner.KeySet([['phred@example.com'], ['bharney@example.com']]))
    
        for row in result:
            print(row)
    

**NOTE** : Perform all iterations within the context of the `with database.snapshot()` block.

## Execute a SQL Select Statement

To read data from tables in the database using a query, call [`execute_sql()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/snapshot#google.cloud.spanner_v1.snapshot.Snapshot.execute_sql) which will return all rows matching the query, or fail if the result set is too large,
    
    
    with database.snapshot() as snapshot:
        QUERY = (
            'SELECT e.first_name, e.last_name, p.telephone '
            'FROM employees as e, phones as p '
            'WHERE p.employee_id == e.employee_id')
        result = snapshot.execute_sql(QUERY)
    
        for row in result:
            print(row)
    

**NOTE** : Perform all iteration within the context of the `with database.snapshot()` block.

## Next Step

Next, learn about [Read-write Transactions](https://docs.cloud.google.com/python/docs/reference/spanner/latest/transaction-usage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
