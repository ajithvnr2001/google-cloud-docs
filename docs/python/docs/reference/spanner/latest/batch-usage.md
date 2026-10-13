---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/batch-usage/
title: Batching Modifications \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:48.535817+00:00
---

# Batching Modifications  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/batch-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Batching Modifications Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 

A [`Batch`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/batch#google.cloud.spanner_v1.batch.Batch) represents a set of data modification operations to be performed on tables in a database. Use of a `Batch` does not require creating an explicit [`Snapshot`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/snapshot#google.cloud.spanner_v1.snapshot.Snapshot) or [`Transaction`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/transaction#google.cloud.spanner_v1.transaction.Transaction). Until [`commit()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/batch#google.cloud.spanner_v1.batch.Batch.commit) is called on a `Batch`, no changes are propagated to the back-end.

## Use Batch via BatchCheckout

`Database.batch()` creates a [`BatchCheckout`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.BatchCheckout) instance to use as a context manager to handle creating and committing a [`Batch`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/batch#google.cloud.spanner_v1.batch.Batch). The `BatchCheckout` will automatically call [`commit()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/batch#google.cloud.spanner_v1.batch.Batch.commit) if the `with` block exits without raising an exception.
    
    
    from google.cloud.spanner import [KeySet](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.keyset.KeySet.html)
    
    client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
    instance = [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_instance)(INSTANCE_NAME)
    database = instance.database(DATABASE_NAME)
    
    to_delete = KeySet(keys=[
        ('bharney@example.com',)
        ('nonesuch@example.com',)
    ])
    
    with database.batch() as batch:
    
        batch.[insert](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction.html#google_cloud_spanner_v1_transaction_Transaction_insert)(
            'citizens', columns=['email', 'first_name', 'last_name', 'age'],
            values=[
                ['phred@exammple.com', 'Phred', 'Phlyntstone', 32],
                ['bharney@example.com', 'Bharney', 'Rhubble', 31],
            ])
    
        batch.update(
            'citizens', columns=['email', 'age'],
            values=[
                ['phred@exammple.com', 33],
                ['bharney@example.com', 32],
            ])
    
        ...
    
        batch.delete('citizens', to_delete)
    

## Inserting records using a Batch

`Batch.insert()` adds one or more new records to a table. This fails if any of the records already exist.
    
    
    batch.insert(
        'citizens', columns=['email', 'first_name', 'last_name', 'age'],
        values=[
            ['phred@exammple.com', 'Phred', 'Phlyntstone', 32],
            ['bharney@example.com', 'Bharney', 'Rhubble', 31],
        ])
    

**NOTE** : Ensure that data being sent for `STRING` columns uses a text string (`str` in Python 3; `unicode` in Python 2).

Additionally, if you are writing data intended for a `BYTES` column, you must base64 encode it.

## Update records using a Batch

`Batch.update()` updates one or more existing records in a table. This fails if any of the records do not already exist.
    
    
    batch.update(
        'citizens', columns=['email', 'age'],
        values=[
            ['phred@exammple.com', 33],
            ['bharney@example.com', 32],
        ])
    

**NOTE** : Ensure that data being sent for `STRING` columns uses a text string (`str` in Python 3; `unicode` in Python 2).

Additionally, if you are writing data intended for a `BYTES` column, you must base64 encode it.

## Insert or update records using a Batch

`Batch.insert_or_update()` inserts _or_ updates one or more records in a table. Existing rows have values for the supplied columns overwritten; other column values are preserved.
    
    
    batch.insert_or_update(
        'citizens', columns=['email', 'first_name', 'last_name', 'age'],
        values=[
            ['phred@exammple.com', 'Phred', 'Phlyntstone', 31],
            ['wylma@example.com', 'Wylma', 'Phlyntstone', 29],
        ])
    

**NOTE** : Ensure that data being sent for `STRING` columns uses a text string (`str` in Python 3; `unicode` in Python 2).

Additionally, if you are writing data intended for a `BYTES` column, you must base64 encode it.

## Replace records using a Batch

`Batch.replace()` inserts _or_ updates one or more records in a table. Existing rows have values for the supplied columns overwritten; other column values are set to null.
    
    
    batch.replace(
        'citizens', columns=['email', 'first_name', 'last_name', 'age'],
        values=[
            ['bharney@example.com', 'Bharney', 'Rhubble', 30],
            ['bhettye@example.com', 'Bhettye', 'Rhubble', 30],
        ])
    

**NOTE** : Ensure that data being sent for `STRING` columns uses a text string (`str` in Python 3; `unicode` in Python 2).

Additionally, if you are writing data intended for a `BYTES` column, you must base64 encode it.

## Delete records using a Batch

`Batch.delete()` removes one or more records from a table. Attempting to delete rows that do not exist will not cause errors.
    
    
    from google.cloud.spanner import [KeySet](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.keyset.KeySet.html)
    
    to_delete = KeySet(keys=[
        ('bharney@example.com',)
        ('nonesuch@example.com',)
    ])
    
    batch.delete('citizens', to_delete)
    

## Commit changes for a Batch

After describing the modifications to be made to table data via the `Batch.insert()`, `Batch.update()`, `Batch.insert_or_update()`, `Batch.replace()`, and `Batch.delete()` methods above, send them to the back-end by calling `Batch.commit()`, which makes the `Commit` API call.

You do not need to call this yourself as [`BatchCheckout`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.BatchCheckout) will call this method automatically upon exiting the `with` block.
    
    
    batch.commit()
    

## Next Step

Next, learn about [Read-only Transactions via Snapshots](https://docs.cloud.google.com/python/docs/reference/spanner/latest/snapshot-usage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
