---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/transactions/
title: NDB Transactions \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:26.934466+00:00
---

# NDB Transactions  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/transactions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  NDB Transactions Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

A transaction is an operation or set of operations that are guaranteed to be atomic, which means that transactions are never partially applied. Either all of the operations in the transaction are applied, or none of them are applied. Transactions have a maximum duration of 60 seconds with a 10 second idle expiration time after 30 seconds.

Using the [NDB asynchronous API](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/async), an application can manage multiple transactions simultaneously if they are independent. The synchronous API offers a simplified API using the `@ndb.transactional()` decorator. The decorated function is executed in the context of the transaction.
    
    
    @ndb.transactional
    def insert_if_absent(note_key, note):
        fetch = note_key.get()
        if fetch is None:
            note.put()
            return True
        return False
    
    
    note_key = ndb.Key(Note, note_title, parent=parent)
    note = Note(key=note_key, content=note_text)
    
    
    inserted = insert_if_absent(note_key, note)

If the transaction "collides" with another, it fails; NDB automatically retries such failed transactions a few times. The function may be called multiple times if the transaction is retried. There is a limit (default 3) to the number of retries attempted; if the transaction still does not succeed, NDB raises `TransactionFailedError`. You can change the retry count by passing `retries=N` to the `transactional()` decorator. A retry count of 0 means the transaction is attempted once but not retried if it fails; a retry count of N means that the transaction may be attempted a total of N+1 times. Example: 
    
    
    @ndb.transactional(retries=1)
    def insert_if_absent_2_retries(note_key, note):
        # do insert

In transactions, only ancestor queries are allowed. By default, a transaction can only work with entities in the same entity group (entities whose keys have the same "ancestor"). 

You can specify cross-group ("XG") transactions (which allow up to twenty-five entity groups), by passing `xg=True`: 
    
    
    @ndb.transactional(xg=True)
    def insert_if_absent_xg(note_key, note):
        # do insert

Cross-group transactions operate across multiple entity groups, and behave like single-group transactions, but don't fail if code tries to update entities from more than one entity group. 

If the function raises an exception, the transaction is immediately aborted and NDB re-raises the exception so that the calling code sees it. You can force a transaction to fail silently by raising the `ndb.Rollback` exception (the function call returns `None` in this case). There is no mechanism to force a retry. 

You might have a function that you don't always want to run in a transaction. Instead of decorating such a function with `@ndb.transactional`, pass it as a callback function to `ndb.transaction()`
    
    
    def insert_if_absent_sometimes(note_key, note):
        # do insert
    
    
    inserted = ndb.transaction(lambda:
                               insert_if_absent_sometimes(note_key, note))

To test whether some code is running inside a transaction, use the `[in_transaction()](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#in_transaction)` function. 

You can specify how a "transactional" function should behave if invoked by code that's already in a transaction. The `@ndb.non_transactional` decorator specifies that a function should not run in a transaction; if called in a transaction, it runs outside the transaction. The `@ndb.transactional` decorator and `ndb.transaction` function take a `propagation` keyword argument. For example, if a function should start a new, independent transaction, decorate it like so: 
    
    
    @ndb.transactional(propagation=ndb.TransactionOptions.INDEPENDENT)
    def insert_if_absent_indep(note_key, note):
        # do insert

The propagation types are listed with the other [Context Options and Transaction Options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options)

Transaction behavior and NDB's caching behavior can combine to confuse you if you don't know what's going on. If you modify an entity inside a transaction but have not yet committed the transaction, then NDB's context cache has the modified value but the underlying datastore still has the unmodified value. 

## Transactional task enqueuing

You can enqueue a task as part of a Datastore transaction, so that the task is only enqueued if the transaction is committed successfully. If the transaction does not get committed, the task is not enqueued. If the transaction does get committed, the task is enqueued. Once enqueued, the task will not execute immediately, so the task is not atomic with the transaction. Still, once enqueued, the task will retry until it succeeds. This applies to any task enqueued during a decorated function. 

Transactional tasks are useful because they allow you to combine non-Datastore actions to a transaction that depends on the transaction succeeding (such as sending an email to confirm a purchase). You can also tie Datastore actions to the transaction, such as to commit changes to entity groups outside of the transaction if and only if the transaction succeeds. 

An application cannot insert more than five [transactional tasks](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue#Python_Tasks_within_transactions) into [task queues](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue#Python_Queue_concepts) during a single transaction. Transactional tasks must not have user-specified names. 
    
    
    from google.appengine.api import taskqueue
    from google.appengine.ext import ndb
    
    
    @ndb.transactional
    def insert_if_absent_taskq(note_key, note):
        taskqueue.add(url=flask.url_for('taskq_worker'), transactional=True)
        # do insert

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
