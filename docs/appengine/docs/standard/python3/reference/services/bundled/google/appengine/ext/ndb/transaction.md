---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/transaction/
title: google.appengine.ext.ndb.transaction \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:47.346294+00:00
---

# google.appengine.ext.ndb.transaction  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/transaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.transaction Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/model.py#L3849-L3893) Run a callback in a transaction.
    
    
    google.appengine.ext.ndb.transaction(
        callback, **ctx_options
    )
    

| 

## Args  
  
---  
  
`callback` |  A function or tasklet to be called.   
`**ctx_options` |  Transaction options.   
  
Useful options include: retries=N: Retry up to N times (i.e. try up to N+1 times) propagation=: Determines how an existing transaction should be propagated, where  can be one of the following: TransactionOptions.NESTED: Start a nested transaction (this is the default; but actual nested transactions are not yet implemented, so effectively you can only use this outside an existing transaction). TransactionOptions.MANDATORY: A transaction must already be in progress. TransactionOptions.ALLOWED: If a transaction is in progress, join it. TransactionOptions.INDEPENDENT: Always start a new parallel transaction. xg=True: On the High Replication Datastore, enable cross-group transactions, i.e. allow writing to up to 5 entity groups. read_only=True: Indicates a transaction will not do any writes, which potentially allows for more throughput.

WARNING: Using anything other than NESTED for the propagation flag can have strange consequences. When using ALLOWED or MANDATORY, if an exception is raised, the transaction is likely not safe to commit. When using INDEPENDENT it is not generally safe to return values read to the caller (as they were not read in the caller's transaction).

## Returns  
  
---  
Whatever callback() returns.   
  
## Raises  
  
---  
Whatever callback() raises; datastore_errors.TransactionFailedError if the transaction failed.   
  
#### Note:

To pass arguments to a callback function, use a lambda, e.g. def my_callback(key, inc): ... transaction(lambda: my_callback(Key(...), 1))

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
