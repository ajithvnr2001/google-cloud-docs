---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/MultiRpc/
title: google.appengine.datastore.datastore_rpc.MultiRpc \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:18:40.576684+00:00
---

# google.appengine.datastore.datastore_rpc.MultiRpc  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/MultiRpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_rpc.MultiRpc Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L786-L971) A wrapper around multiple UserRPC objects. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_rpc.MultiRpc(
        rpcs, extra_hook=None
    )
    

This provides an API similar to that of UserRPC, but wraps multiple RPCs such that e.g. .wait() blocks until all wrapped RPCs are complete, and .get_result() returns the combined results from all wrapped RPCs.

#### Class methods:

flatten(rpcs): Expand a list of UserRPCs and MultiRpcs into a list of UserRPCs. wait_any(rpcs): Call UserRPC.wait_any(flatten(rpcs)). wait_all(rpcs): Call UserRPC.wait_all(flatten(rpcs)).

#### Instance methods:

wait(): Wait for all RPCs. check_success(): Wait and then check success for all RPCs. get_result(): Wait for all, check successes, then merge all results.

#### Instance attributes:

  * **`rpcs`** : The list of wrapped RPCs (returns a copy).
  * **`state`** : The combined state of all RPCs.

| 

## Args  
  
---  
  
`rpcs` |  A list of UserRPC and MultiRpc objects; it is flattened before being stored.   
`extra_hook` |  Optional function to be applied to the final result or list of results.   
  
## Attributes  
  
---  
  
`rpcs` |  Get a flattened list containing the RPCs wrapped. This returns a copy to prevent users from modifying the state.   
`state` |  Get the combined state of the wrapped RPCs. This mimics the UserRPC.state property. If all wrapped RPCs have the same state, that state is returned; otherwise, RUNNING is returned (which here really means 'neither fish nor flesh').   
  
## Methods

### `check_success`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L855-L865)
    
    
    check_success()
    

Check success of all wrapped RPCs, failing if any of the failed.

This mimics the UserRPC.check_success() method.

NOTE: This first waits for all wrapped RPCs to finish before checking the success of any of them. This makes debugging easier.

### `flatten`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L920-L946)
    
    
    @classmethod
    flatten(
        rpcs
    )
    

Return a list of UserRPCs, expanding MultiRpcs in the argument list.

For example: given 4 UserRPCs rpc1 through rpc4, flatten(rpc1, MultiRpc([rpc2, rpc3], rpc4) returns [rpc1, rpc2, rpc3, rpc4].

Args  
---  
  
`rpcs` |  A list of UserRPC and MultiRpc objects.   
  
Returns  
---  
A list of UserRPC objects.   
  
### `get_result`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L867-L918)
    
    
    get_result()
    

Return the combined results of all wrapped RPCs.

This mimics the UserRPC.get_results() method. Multiple results are combined using the following rules:

  1. If there are no wrapped RPCs, an empty list is returned.

  2. If exactly one RPC is wrapped, its result is returned.

  3. If more than one RPC is wrapped, the result is always a list, which is constructed from the wrapped results as follows:

a. A wrapped result equal to None is ignored;

b. A wrapped result that is a list (but not any other type of sequence!) has its elements added to the result list.

c. Any other wrapped result is appended to the result list.




After all results are combined, if __extra_hook is set, it is called with the combined results and its return value becomes the final result.

NOTE: This first waits for all wrapped RPCs to finish, and then checks all their success. This makes debugging easier.

### `wait`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L848-L853)
    
    
    wait()
    

Wait for all wrapped RPCs to finish.

This mimics the UserRPC.wait() method.

### `wait_all`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L962-L971)
    
    
    @classmethod
    wait_all(
        rpcs
    )
    

Wait until all RPCs passed in are finished.

This mimics UserRPC.wait_all().

Args  
---  
  
`rpcs` |  A list of UserRPC and MultiRpc objects.   
  
### `wait_any`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L948-L960)
    
    
    @classmethod
    wait_any(
        rpcs
    )
    

Wait until one of the RPCs passed in is finished.

This mimics UserRPC.wait_any().

Args  
---  
  
`rpcs` |  A list of UserRPC and MultiRpc objects.   
  
Returns  
---  
A UserRPC object or None.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
