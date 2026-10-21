---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/RunInTransactionOptions/
title: google.appengine.api.datastore.RunInTransactionOptions \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:09:05.642938+00:00
---

# google.appengine.api.datastore.RunInTransactionOptions  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore/RunInTransactionOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore.RunInTransactionOptions Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore.py#L2583-L2654) Runs a function inside a datastore transaction.
    
    
    google.appengine.api.datastore.RunInTransactionOptions(
        options, function, *args, **kwargs
    )
    

Runs the user-provided function inside a full-featured, `ACID` datastore transaction. Every Put, Get, and Delete call in the function is made within the transaction. All entities involved in these calls must belong to the same entity group. Queries are supported as long as they specify an ancestor belonging to the same entity group. The trailing arguments are passed to the function as positional arguments. If the function returns a value, that value will be returned by `RunInTransaction`. Otherwise, it will return None. The function may raise any exception to roll back the transaction instead of committing it. If this happens, the transaction will be rolled back and the exception will be re-raised up to RunInTransaction's caller. If you want to roll back intentionally, but don't have an appropriate exception to raise, you can raise an instance of datastore_errors.Rollback. It will cause a rollback, but will _not_ be re-raised up to the caller. The function may be run more than once, so it should be idempotent. It should avoid side effects, and it shouldn't have _any_ side effects that aren't safe to occur multiple times. This includes modifying the arguments, since they persist across invocations of the function. However, this doesn't include Put, Get, and Delete calls, of course.

#### Example usage:

`> def decrement(key, amount=1):` `> counter = datastore.Get(key)` `> counter['count'] -= amount` `> if counter['count'] < 0: # don't let the counter go negative` `> raise datastore_errors.Rollback()` `> datastore.Put(counter)`

> `> counter = datastore.Query('Counter', {'name': 'foo'})` `> datastore.RunInTransaction(decrement, counter.key(), amount=5)`

Transactions satisfy the traditional `ACID` properties. They are:

  * Atomic. All of a transaction's operations are executed or none of them are.
  * Consistent. The datastore's state is consistent before and after a transaction, whether it committed or rolled back. Invariants such as "every entity has a primary key" are preserved.
  * Isolated. Transactions operate on a snapshot of the datastore. Other datastore operations do not see intermediated effects of the transaction; they only see its effects after it has committed.
  * Durable. On commit, all writes are persisted to the datastore.

Nested transactions are not supported. | 

## Args  
  
---  
  
`options` |  `TransactionOptions` specifying options `(number of retries, etc)` for this transaction   
`function` |  a function to be run inside the transaction on all remaining arguments *args: positional arguments for function. **kwargs: keyword arguments for function.   
  
## Returns  
  
---  
the function's return value, if any   
  
## Raises  
  
---  
`TransactionFailedError`, if the transaction could not be committed.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
