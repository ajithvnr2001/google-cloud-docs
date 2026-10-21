---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/make_fetch_call/
title: google.appengine.api.urlfetch.make_fetch_call \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:07:13.786641+00:00
---

# google.appengine.api.urlfetch.make_fetch_call  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/make_fetch_call/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.urlfetch.make_fetch_call Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/urlfetch.py#L295-L366) Executes the RPC call to fetch a given `HTTP` URL.
    
    
    google.appengine.api.urlfetch.make_fetch_call(
        rpc,
        url,
        payload=None,
        method=GET,
        headers={},
        allow_truncated=False,
        follow_redirects=True,
        validate_certificate=None
    )
    

The first argument is a `UserRPC` instance. See [`urlfetch.fetch`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/Fetch) for a thorough description of the remaining arguments. | 

## Raises  
  
---  
  
`InvalidMethodError` |  If the requested method is not in `_VALID_METHODS`.   
`ResponseTooLargeError` |  If the response payload is too large.   
`InvalidURLError` |  If there are issues with the content or size of the requested `url`.   
  
## Returns  
  
---  
The `rpc` object that was passed into the function.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
