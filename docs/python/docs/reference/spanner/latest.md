---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/
title: Python Client for Cloud Spanner \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:39:23.290674+00:00
---

# Python Client for Cloud Spanner  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Python Client for Cloud Spanner Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 

[![image](https://img.shields.io/badge/support-stable-gold.svg)](https://github.com/googleapis/google-cloud-python/blob/main/README.rst#stability-levels) [![image](https://img.shields.io/pypi/v/google-cloud-spanner.svg)](https://pypi.org/project/google-cloud-spanner/) [![image](https://img.shields.io/pypi/pyversions/google-cloud-spanner.svg)](https://pypi.org/project/google-cloud-spanner/)

[Cloud Spanner](https://cloud.google.com/spanner/): Cloud Spanner is a managed, mission-critical, globally consistent and scalable relational database service.

  * [Client Library Documentation](https://cloud.google.com/python/docs/reference/spanner/latest/summary_overview)

  * [Product Documentation](https://cloud.google.com/spanner/)




## Quick Start

In order to use this library, you first need to go through the following steps:

  1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)

  2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)

  3. [Enable the Cloud Spanner.](https://cloud.google.com/spanner/)

  4. [Set up Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)




### Installation

Install this library in a virtual environment using [venv](https://docs.python.org/3/library/venv.html). [venv](https://docs.python.org/3/library/venv.html) is a tool that creates isolated Python environments. These isolated environments can have separate versions of Python packages, which allows you to isolate one project’s dependencies from the dependencies of other projects.

With [venv](https://docs.python.org/3/library/venv.html), it’s possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

### Code samples and snippets

Code samples and snippets live in the [samples/](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-spanner/samples) folder.

#### Supported Python Versions

Our client libraries are compatible with all current [active](https://devguide.python.org/devcycle/#in-development-main-branch) and [maintenance](https://devguide.python.org/devcycle/#maintenance-branches) versions of Python.

Python >= 3.10, including 3.14

#### Unsupported Python Versions

Python <= 3.9

If you are using an [end-of-life](https://devguide.python.org/devcycle/#end-of-life-branches) version of Python, we recommend that you update as soon as possible to an actively supported version.

#### Mac/Linux
    
    
    python3 -m venv <your-env>
    source <your-env>/bin/activate
    pip install google-cloud-spanner
    

#### Windows
    
    
    py -m venv <your-env>
    .\<your-env>\Scripts\activate
    pip install google-cloud-spanner
    

## Example Usage

### Executing Arbitrary SQL in a Transaction

Generally, to work with Cloud Spanner, you will want a transaction. The preferred mechanism for this is to create a single function, which executes as a callback to `database.run_in_transaction`:
    
    
    # First, define the function that represents a single "unit of work"
    # that should be run within the transaction.
    def update_anniversary(transaction, person_id, unix_timestamp):
        # The query itself is just a string.
        #
        # The use of @parameters is recommended rather than doing your
        # own string interpolation; this provides protections against
        # SQL injection attacks.
        query = """SELECT anniversary FROM people
            WHERE id = @person_id"""
    
        # When executing the SQL statement, the query and parameters are sent
        # as separate arguments. When using parameters, you must specify
        # both the parameters themselves and their types.
        row = transaction.execute_sql(
            query=query,
            params={'person_id': person_id},
            param_types={
                'person_id': types.INT64_PARAM_TYPE,
            },
        ).one()
    
        # Now perform an update on the data.
        old_anniversary = row[0]
        new_anniversary = _compute_anniversary(old_anniversary, years)
        transaction.update(
            'people',
            ['person_id', 'anniversary'],
            [person_id, new_anniversary],
        )
    
    # Actually run the `update_anniversary` function in a transaction.
    database.run_in_transaction(update_anniversary,
        person_id=42,
        unix_timestamp=1335020400,
    )
    

### Select records using a Transaction

Once you have a transaction object (such as the first argument sent to `run_in_transaction`), reading data is easy:
    
    
    # Define a SELECT query.
    query = """SELECT e.first_name, e.last_name, p.telephone
        FROM employees as e, phones as p
        WHERE p.employee_id == e.employee_id"""
    
    # Execute the query and return results.
    result = transaction.execute_sql(query)
    for row in result.rows:
        print(row)
    

### Insert records using Data Manipulation Language (DML) with a Transaction

Use the `execute_update()` method to execute a DML statement:
    
    
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    
    def insert_singers(transaction):
        row_ct = transaction.execute_update(
            "INSERT Singers (SingerId, FirstName, LastName) "
            " VALUES (10, 'Virginia', 'Watson')"
        )
    
        print("{} record(s) inserted.".format(row_ct))
    
    database.run_in_transaction(insert_singers)
    

### Insert records using Mutations with a Transaction

To add one or more records to a table, use `insert`:
    
    
    transaction.insert(
        'citizens',
        columns=['email', 'first_name', 'last_name', 'age'],
        values=[
            ['phred@example.com', 'Phred', 'Phlyntstone', 32],
            ['bharney@example.com', 'Bharney', 'Rhubble', 31],
        ],
    )
    

### Update records using Data Manipulation Language (DML) with a Transaction
    
    
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    
    def update_albums(transaction):
        row_ct = transaction.execute_update(
            "UPDATE Albums "
            "SET MarketingBudget = MarketingBudget * 2 "
            "WHERE SingerId = 1 and AlbumId = 1"
        )
    
        print("{} record(s) updated.".format(row_ct))
    
    database.run_in_transaction(update_albums)
    

### Update records using Mutations with a Transaction

`Transaction.update` updates one or more existing records in a table. Fails if any of the records does not already exist.
    
    
    transaction.update(
        'citizens',
        columns=['email', 'age'],
        values=[
            ['phred@example.com', 33],
            ['bharney@example.com', 32],
        ],
    )
    

## Connection API

Connection API represents a wrap-around for Python Spanner API, written in accordance with PEP-249, and provides a simple way of communication with a Spanner database through connection objects:
    
    
    from google.cloud.spanner_dbapi.connection import connect
    
    connection = connect("instance-id", "database-id")
    connection.autocommit = True
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM table_name")
    
    result = cursor.fetchall()
    

If using [fine-grained access controls](about:invalid#zCSafez) you can pass a `database_role` argument to connect as that role:
    
    
    connection = connect("instance-id", "database-id", database_role='your-role')
    

### Aborted Transactions Retry Mechanism

In `!autocommit` mode, transactions can be aborted due to transient errors. In most cases retry of an aborted transaction solves the problem. To simplify it, connection tracks SQL statements, executed in the current transaction. In case the transaction aborted, the connection initiates a new one and re-executes all the statements. In the process, the connection checks that retried statements are returning the same results that the original statements did. If results are different, the transaction is dropped, as the underlying data changed, and auto retry is impossible.

Auto-retry of aborted transactions is enabled only for `!autocommit` mode, as in `autocommit` mode transactions are never aborted.

### Next Steps

  * Read the [Client Library Documentation](https://cloud.google.com/python/docs/reference/spanner/latest/summary_overview) for Cloud Spanner to see other available methods on the client.

  * Read the [Cloud Spanner Product documentation](https://cloud.google.com/spanner/) to learn more about the product and see How-to Guides.

  * View this [README](https://github.com/googleapis/google-cloud-python/blob/main/README.rst) to see the full list of Cloud APIs that we cover.




## Logging

This library uses the standard Python `logging` functionality to log some RPC events that could be of interest for debugging and monitoring purposes. Note the following:

  1. Logs may contain sensitive information. Take care to **restrict access to the logs** if they are saved, whether it be on local storage or on Google Cloud Logging.

  2. Google may refine the occurrence, level, and content of various log messages in this library without flagging such changes as breaking. **Do not depend on immutability of the logging events**.

  3. By default, the logging events from this library are not handled. You must **explicitly configure log handling** using one of the mechanisms below.




### Simple, environment-based configuration

To enable logging for this library without any changes in your code, set the `GOOGLE_SDK_PYTHON_LOGGING_SCOPE` environment variable to a valid Google logging scope. This configures handling of logging events (at level `logging.DEBUG` or higher) from this library in a default manner, emitting the logged messages in a structured format. It does not currently allow customizing the logging levels captured nor the handlers, formatters, etc. used for any logging event.

A logging scope is a period-separated namespace that begins with `google`, identifying the Python module or package to log.

  * Valid logging scopes: `google`, `google.cloud.asset.v1`, `google.api`, `google.auth`, etc.

  * Invalid logging scopes: `foo`, `123`, etc.




**NOTE** : If the logging scope is invalid, the library does not set up any logging handlers.

#### Environment-Based Examples

  * Enabling the default handler for all Google-based loggers


    
    
    export GOOGLE_SDK_PYTHON_LOGGING_SCOPE=google
    

  * Enabling the default handler for a specific Google module (for a client library called `library_v1`):


    
    
    export GOOGLE_SDK_PYTHON_LOGGING_SCOPE=google.cloud.library_v1
    

### Advanced, code-based configuration

You can also configure a valid logging scope using Python’s standard logging mechanism.

#### Code-Based Examples

  * Configuring a handler for all Google-based loggers


    
    
    import logging
    
    from google.cloud import library_v1
    
    base_logger = logging.getLogger("google")
    base_logger.addHandler(logging.StreamHandler())
    base_logger.setLevel(logging.DEBUG)
    

  * Configuring a handler for a specific Google module (for a client library called `library_v1`):


    
    
    import logging
    
    from google.cloud import library_v1
    
    base_logger = logging.getLogger("google.cloud.library_v1")
    base_logger.addHandler(logging.StreamHandler())
    base_logger.setLevel(logging.DEBUG)
    

### Logging details

  1. Regardless of which of the mechanisms above you use to configure logging for this library, by default logging events are not propagated up to the root logger from the google-level logger. If you need the events to be propagated to the root logger, you must explicitly set `logging.getLogger("google").propagate = True` in your code.

  2. You can mix the different logging configurations above for different Google modules. For example, you may want use a code-based logging configuration for one library, but decide you need to also set up environment-based logging configuration for another library.

     1. If you attempt to use both code-based and environment-based configuration for the same module, the environment-based configuration will be ineffectual if the code -based configuration gets applied first.
  3. The Google-specific logging configurations (default handlers for environment-based configuration; not propagating logging events to the root logger) get executed the first time _any_ client library is instantiated in your application, and only if the affected loggers have not been previously configured. (This is the reason for 2.i. above.)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
