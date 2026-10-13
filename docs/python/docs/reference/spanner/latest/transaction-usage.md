---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/transaction-usage/
title: Read-write Transactions \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:49.424526+00:00
---

# Read-write Transactions  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/transaction-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Read-write Transactions Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 

A [`Transaction`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/transaction#google.cloud.spanner_v1.transaction.Transaction) represents a transaction: when the transaction commits, it will send any accumulated mutations to the server.

To understand more about how transactions work, visit [Transaction](https://cloud.google.com/spanner/docs/reference/rest/v1/Transaction). To learn more about how to use them in the Python client, continue reading.

## Read Table Data

Read data for selected rows from a table in the database. Calls the `Read` API, which returns all rows specified in `key_set`, or else fails if the result set is too large,
    
    
    result = transaction.read(
        table='table-name', columns=['first_name', 'last_name', 'age'],
        key_set=['phred@example.com', 'bharney@example.com'])
    
    for row in list(result):
        print(row)
    

**NOTE** : If streaming a chunk fails due to a “resumable” error, `Snapshot.read()` retries the `StreamingRead` API request, passing the `resume_token` from the last partial result streamed.

## Execute a SQL Select Statement

Read data from a query against tables in the database. Calls the `ExecuteSql` API, which returns all rows matching the query, or else fails if the result set is too large,
    
    
    QUERY = (
        'SELECT e.first_name, e.last_name, p.telephone '
        'FROM employees as e, phones as p '
        'WHERE p.employee_id == e.employee_id')
    result = transaction.execute_sql(QUERY)
    
    for row in list(result):
        print(row)
    

## Execute a SQL DML Statement

Modify data from a query against tables in the database. Calls the `ExecuteSql` API, and returns the number of rows affected,
    
    
    QUERY = 'DELETE from Table WHERE 1=1'
    row_count = transaction.execute_sql(QUERY)
    

## Insert records using a Transaction

`Transaction.insert()` adds one or more new records to a table. Fails if any of the records already exists.
    
    
    transaction.insert(
        'citizens', columns=['email', 'first_name', 'last_name', 'age'],
        values=[
            ['phred@exammple.com', 'Phred', 'Phlyntstone', 32],
            ['bharney@example.com', 'Bharney', 'Rhubble', 31],
        ])
    

**NOTE** : Ensure that data being sent for `STRING` columns uses a text string (`str` in Python 3; `unicode` in Python 2).

Additionally, if you are writing data intended for a `BYTES` column, you must base64 encode it.

## Update records using a Transaction

`Transaction.update()` updates one or more existing records in a table. Fails if any of the records does not already exist.
    
    
    transaction.update(
        'citizens', columns=['email', 'age'],
        values=[
            ['phred@exammple.com', 33],
            ['bharney@example.com', 32],
        ])
    

**NOTE** : Ensure that data being sent for `STRING` columns uses a text string (`str` in Python 3; `unicode` in Python 2).

Additionally, if you are writing data intended for a `BYTES` column, you must base64 encode it.

## Insert or update records using a Transaction

`Transaction.insert_or_update()` inserts _or_ updates one or more records in a table. Existing rows have values for the supplied columns overwritten; other column values are preserved.
    
    
    transaction.insert_or_update(
        'citizens', columns=['email', 'first_name', 'last_name', 'age'],
        values=[
            ['phred@exammple.com', 'Phred', 'Phlyntstone', 31],
            ['wylma@example.com', 'Wylma', 'Phlyntstone', 29],
        ])
    

**NOTE** : Ensure that data being sent for `STRING` columns uses a text string (`str` in Python 3; `unicode` in Python 2).

Additionally, if you are writing data intended for a `BYTES` column, you must base64 encode it.

## Replace records using a Transaction

`Transaction.replace()` inserts _or_ updates one or more records in a table. Existing rows have values for the supplied columns overwritten; other column values are set to null.
    
    
    transaction.replace(
        'citizens', columns=['email', 'first_name', 'last_name', 'age'],
        values=[
            ['bharney@example.com', 'Bharney', 'Rhubble', 30],
            ['bhettye@example.com', 'Bhettye', 'Rhubble', 30],
        ])
    

**NOTE** : Ensure that data being sent for `STRING` columns uses a text string (`str` in Python 3; `unicode` in Python 2).

Additionally, if you are writing data intended for a `BYTES` column, you must base64 encode it.

## Delete records using a Transaction

`Transaction.delete()` removes one or more records from a table. Non-existent rows do not cause errors.
    
    
    transaction.delete(
        'citizens', keyset=['bharney@example.com', 'nonesuch@example.com'])
    

## Using `run_in_transaction()`

Rather than calling `commit()` or `rollback()` manually, you should use `run_in_transaction()` to run the function that you need. The transaction’s `commit()` method will be called automatically if the `with` block exits without raising an exception. The function will automatically be retried for [`Aborted`](https://googleapis.dev/python/google-api-core/latest/exceptions.html#google.api_core.exceptions.Aborted) errors, but will raise on [`GoogleAPICallError`](https://googleapis.dev/python/google-api-core/latest/exceptions.html#google.api_core.exceptions.GoogleAPICallError) and `rollback()` will be called on all others.
    
    
    def _unit_of_work(transaction):
        transaction.insert(
            'citizens',
            columns=['email', 'first_name', 'last_name', 'age'],
            values=[
                ['phred@exammple.com', 'Phred', 'Phlyntstone', 32],
                ['bharney@example.com', 'Bharney', 'Rhubble', 31],
            ]
        )
    
        transaction.update(
            'citizens',
            columns=['email', 'age'],
            values=[
                ['phred@exammple.com', 33],
                ['bharney@example.com', 32],
            ]
        )
    
        ...
    
        transaction.delete(
            'citizens',
            keyset=['bharney@example.com', 'nonesuch@example.com']
        )
    
    db.run_in_transaction(_unit_of_work)
    

## Use a Transaction as a Context Manager

Alternatively, you can use the `Transaction` instance as a context manager. The transaction’s `commit()` method will be called automatically if the `with` block exits without raising an exception.

If an exception is raised inside the `with` block, the transaction’s `rollback()` method will automatically be called.
    
    
    with session.transaction() as transaction:
    
        transaction.insert(
            'citizens', columns=['email', 'first_name', 'last_name', 'age'],
            values=[
                ['phred@exammple.com', 'Phred', 'Phlyntstone', 32],
                ['bharney@example.com', 'Bharney', 'Rhubble', 31],
            ])
    
        transaction.update(
            'citizens', columns=['email', 'age'],
            values=[
                ['phred@exammple.com', 33],
                ['bharney@example.com', 32],
            ])
    
        ...
    
        transaction.delete('citizens',
            keyset=['bharney@example.com', 'nonesuch@example.com'])
    

## Begin a Transaction

**NOTE** : Normally, applications will not construct transactions manually. Rather, consider using `run_in_transaction()` or the context manager as described above.

To begin using a transaction manually:
    
    
    transaction = session.transaction()
    

## Commit changes for a Transaction

**NOTE** : Normally, applications will not commit transactions manually. Rather, consider using `run_in_transaction()` or the context manager as described above.

After modifications to be made to table data via the `Transaction.insert()`, `Transaction.update()`, `Transaction.insert_or_update()`, `Transaction.replace()`, and `Transaction.delete()` methods above, send them to the back-end by calling `Transaction.commit()`, which makes the `Commit` API call.
    
    
    transaction.commit()
    

## Roll back changes for a Transaction

**NOTE** : Normally, applications will not roll back transactions manually. Rather, consider using `run_in_transaction()` or the context manager as described above.

After describing the modifications to be made to table data via the `Transaction.insert()`, `Transaction.update()`, `Transaction.insert_or_update()`, `Transaction.replace()`, and `Transaction.delete()` methods above, cancel the transaction on the the back-end by calling `Transaction.rollback()`, which makes the `Rollback` API call.
    
    
    transaction.rollback()
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
