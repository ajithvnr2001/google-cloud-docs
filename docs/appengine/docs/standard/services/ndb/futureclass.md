---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass/
title: NDB Future Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:41.463847+00:00
---

# NDB Future Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  NDB Future Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

A `Future` represents the result of an [asynchronous operation](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/async). When created, it probably doesn't have any result data. When the operation finishes, the `Future` gets the result. An application can call a `Future` object's `get_result()` method; if the result has arrived, the method returns it; otherwise, it waits for the result to arrive and _then_ returns it. 

**Note:** There is no 1:1 mapping between RPCs and Futures. Multiple futures might be tied to a result from a single RPC.

## Instance Methods

check_success() 
    Check to see if the operation succeeded. Waits if necessary. Raises an exception if there was a problem; returns `None` if there was no problem. 
done() 
    Returns `True` if the result (or exception) has arrived; otherwise, returns `False`. This function does not wait. 
get_exception() 
    Waits if necessary; then returns the exception (or `None` if there was no exception). _Returns_ the exception, doesn't raise it. 
get_result() 
    Waits if necessary; then returns the result or raises the exception. 
get_traceback() 
    Waits if necessary; then returns the exception's traceback object (or `None` if there was no traceback object). Python's `[ traceback](http://docs.python.org/library/traceback.html)` module has functions to print and work with traceback objects. 
wait() 
    Waits until a result or exception arrives. Always returns `None`. 

## Class Methods

wait_all(futures) 
    Wait until all `Futures` in the passed iterable are done. 

**Arguments**

futures
    Iterable of `Future` objects. 

Returns `None`. 

wait_any(futures) 
    Wait until at least one of a iterable of `Futures` is done. 

**Arguments**

futures
    Iterable of `Future` objects. 

Returns one `Future` that is done. (Returns `None` if the `futures` iterable is empty.) 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
