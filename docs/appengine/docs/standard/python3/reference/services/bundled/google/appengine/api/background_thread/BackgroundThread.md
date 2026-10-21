---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/background_thread/BackgroundThread/
title: google.appengine.api.background_thread.BackgroundThread \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:41:47.451297+00:00
---

# google.appengine.api.background_thread.BackgroundThread  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/background_thread/BackgroundThread/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.background_thread.BackgroundThread Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/background_thread/background_thread.py#L96-L151) A threading.Thread-like interface for background threads. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.background_thread.background_thread.BackgroundThread`
    
    
    google.appengine.api.background_thread.BackgroundThread(
        group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None
    )
    

| 

## Attributes  
  
---  
  
`daemon` |  A boolean value indicating whether this thread is a daemon thread. This must be set before start() is called, otherwise RuntimeError is raised. Its initial value is inherited from the creating thread; the main thread is not a daemon thread and therefore all threads created in the main thread default to daemon = False. The entire Python program exits when only daemon threads are left.   
`ident` |  Thread identifier of this thread or None if it has not been started. This is a nonzero integer. See the get_ident() function. Thread identifiers may be recycled when a thread exits and another thread is created. The identifier is available even after the thread has exited.   
`name` |  A string used for identification purposes only. It has no semantics. Multiple threads may be given the same name. The initial name is set by the constructor.   
`native_id` |  Native integral thread ID of this thread, or None if it has not been started. This is a non-negative integer. See the get_native_id() function. This represents the Thread ID as reported by the kernel.   
  
## Methods

### `getName`
    
    
    getName()
    

Return a string used for identification purposes only.

This method is deprecated, use the name attribute instead.

### `isDaemon`
    
    
    isDaemon()
    

Return whether this thread is a daemon.

This method is deprecated, use the daemon attribute instead.

### `is_alive`
    
    
    is_alive()
    

Return whether the thread is alive.

This method returns True just before the run() method starts until just after the run() method terminates. See also the module function enumerate().

### `join`
    
    
    join(
        timeout=None
    )
    

Wait until the thread terminates.

This blocks the calling thread until the thread whose join() method is called terminates -- either normally or through an unhandled exception or until the optional timeout occurs.

When the timeout argument is present and not None, it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof). As join() always returns None, you must call is_alive() after join() to decide whether a timeout happened -- if the thread is still alive, the join() call timed out.

When the timeout argument is not present or None, the operation will block until the thread terminates.

A thread can be join()ed many times.

join() raises a RuntimeError if an attempt is made to join the current thread as that would cause a deadlock. It is also an error to join() a thread before it has been started and attempts to do so raises the same exception.

### `run`
    
    
    run()
    

Method representing the thread's activity.

You may override this method in a subclass. The standard run() method invokes the callable object passed to the object's constructor as the target argument, if any, with sequential and keyword arguments taken from the args and kwargs arguments, respectively.

### `setDaemon`
    
    
    setDaemon(
        daemonic
    )
    

Set whether this thread is a daemon.

This method is deprecated, use the .daemon property instead.

### `setName`
    
    
    setName(
        name
    )
    

Set the name string for this thread.

This method is deprecated, use the name attribute instead.

### `start`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/background_thread/background_thread.py#L136-L151)
    
    
    start()
    

Starts this background thread.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
