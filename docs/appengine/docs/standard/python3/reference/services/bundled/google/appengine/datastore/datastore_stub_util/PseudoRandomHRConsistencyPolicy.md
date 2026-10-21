---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/PseudoRandomHRConsistencyPolicy/
title: google.appengine.datastore.datastore_stub_util.PseudoRandomHRConsistencyPolicy \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:57:27.895208+00:00
---

# google.appengine.datastore.datastore_stub_util.PseudoRandomHRConsistencyPolicy  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/PseudoRandomHRConsistencyPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_stub_util.PseudoRandomHRConsistencyPolicy Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2095-L2147) A policy that always gives the same sequence of consistency decisions. Inherits From: [`BaseHighReplicationConsistencyPolicy`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseHighReplicationConsistencyPolicy), [`BaseConsistencyPolicy`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseConsistencyPolicy), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_stub_util.PseudoRandomHRConsistencyPolicy(
        probability=None, seed=0
    )
    

| 

## Args  
  
---  
  
`probability` |  A number between 0 and 1 that is the likelihood of a transaction applying before a global query is executed.   
`seed` |  A hashable object to use as a seed. Use None to use the current timestamp.   
  
## Attributes  
  
---  
  
`probability` |  Return the probability of applying a job.   
`random_seed` |  Return the random seed.   
  
## Methods

### `SetProbability`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2115-L2127)
    
    
    SetProbability(
        probability
    )
    

Change the probability of a transaction applying.

Args  
---  
  
`probability` |  A number between 0 and 1 that determines the probability of a transaction applying before a global query is run.   
  
### `SetSeed`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2129-L2134)
    
    
    SetSeed(
        seed
    )
    

Reset the seed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
