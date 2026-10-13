---
url: https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.transaction
title: Module transaction (2.27.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:04.464922+00:00
---

# Module transaction (2.27.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.transaction

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module transaction (2.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.27.0 (latest)  2.26.1  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.0  2.16.1  2.15.2  2.14.0  2.13.2  2.12.0  2.11.1  2.10.0  2.9.0  2.8.3  2.7.2  2.6.2  2.5.1  2.4.0  2.3.0  2.2.0  2.1.6  2.0.1  1.15.5  1.14.0  1.13.2  1.12.0  1.11.0  1.10.0  1.9.0 

Create / interact with Google Cloud Datastore transactions.

## Classes 

### [Transaction](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.transaction.Transaction)
    
    
    Transaction(client, read_only=False, read_time=None, begin_later=False)

An abstraction representing datastore Transactions.

Transactions can be used to build up a bulk mutation and ensure all or none succeed (transactionally).

For example, the following snippet of code will put the two `save` operations (either `insert` or `upsert`) into the same mutation, and execute those within a transaction:

.. testsetup:: txn
    
    
    import uuid
    
    from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
    
    unique = str(uuid.uuid4())[0:8]
    client = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html)(namespace='ns{}'.format(unique))
    

.. doctest:: txn
    
    
    >>> entity1 = datastore.Entity(client.key('EntityKind', 1234))
    >>> entity2 = datastore.Entity(client.key('EntityKind', 2345))
    >>> with client.transaction():
    ...     client.put_multi([entity1, entity2])
    

Because it derives from xref_Batch, `Transaction` also provides `put` and `delete` methods:

.. doctest:: txn

> > > with client.transaction() as xact: ... xact.put(entity1) ... xact.delete(entity2.key)

By default, the transaction is rolled back if the transaction block exits with an error:

.. doctest:: txn
    
    
    >>> def do_some_work():
    ...    return
    >>> class SomeException(Exception):
    ...    pass
    >>> with client.transaction():
    ...     do_some_work()
    ...     raise SomeException  # rolls back
    Traceback (most recent call last):
      ...
    SomeException
    

If the transaction block exits without an exception, it will commit by default.

**Warning:** Inside a transaction, automatically assigned IDs for entities will not be available at save time! That means, if you try: .. doctest:: txn

> > > with client.transaction(): ... thing1 = datastore.Entity(key=client.key('Thing')) ... client.put(thing1) 

Once you exit the transaction (or call `commit`), the automatically generated ID will be assigned to the entity:

.. doctest:: txn
    
    
      >>> with client.transaction():
      ...     thing2 = datastore.Entity(key=client.key('Thing'))
      ...     client.put(thing2)
      ...     print(thing2.key.is_partial)  # There is no ID on this key.
      ...
      True
      >>> print(thing2.key.is_partial)  # There *is* an ID.
      False
    

If you don't want to use the context manager you can initialize a transaction manually:

.. doctest:: txn

> > > transaction = client.transaction() transaction.begin()
>>> 
>>> thing3 = datastore.Entity(key=client.key('Thing')) transaction.put(thing3)
>>> 
>>> transaction.commit()

.. testcleanup:: txn
    
    
    with client.batch() as batch:
        batch.delete(client.key('EntityKind', 1234))
        batch.delete(client.key('EntityKind', 2345))
        batch.delete(thing1.key)
        batch.delete(thing2.key)
        batch.delete(thing3.key)
    

**Parameters**  
---  
**Name** | **Description**  
`client` |  `[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client)`   
the client used to connect to datastore.  
`read_only` |  `bool`   
indicates the transaction is read only.  
`read_time` |  `datetime`   
(Optional) Time at which the transaction reads entities. Only allowed when `read_only=True`. This feature is in private preview.  
`begin_later` |  `bool`   
(Optional) If True, the transaction will be started lazily (i.e. when the first RPC is made). If False, the transaction will be started as soon as the context manager is entered. `self.begin()` can also be called manually to begin the transaction at any time. Default is False.  
**Exceptions**  
---  
**Type** | **Description**  
``ValueError` | if read_time is specified when `read_only=False`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
