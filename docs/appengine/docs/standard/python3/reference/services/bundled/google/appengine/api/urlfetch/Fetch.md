---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/Fetch/
title: google.appengine.api.urlfetch.Fetch \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:40:43.615622+00:00
---

# google.appengine.api.urlfetch.Fetch  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/Fetch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.urlfetch.Fetch Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/urlfetch.py#L232-L292) Fetches the given HTTP `url`, blocking until the result is returned.

#### View aliases

**Main aliases** `google.appengine.api.urlfetch.fetch`
    
    
    google.appengine.api.urlfetch.Fetch(
        url,
        payload=None,
        method=GET,
        headers={},
        allow_truncated=False,
        follow_redirects=True,
        deadline=None,
        validate_certificate=None
    )
    

URLs are fetched using one of the following HTTP methods:
    
    
    - `GET`
    - `POST`
    - `HEAD`
    - `PUT`
    - `DELETE`
    - `PATCH`
    

To fetch the result, a HTTP/1.1-compliant proxy is used. | 

## Args  
  
---  
  
`method` |  The constants `GET`, `POST`, `HEAD`, `PUT`, `DELETE`, or `PATCH` or the same `HTTP` methods as strings.   
`payload` |  `POST`, `PUT`, or `PATCH` payload (implies method is not `GET`, `HEAD`, or `DELETE`). This argument is ignored if the method is not `POST`, `PUT`, or `PATCH`.   
`headers` |  Dictionary of `HTTP` headers to send with the request.   
`allow_truncated` |  If set to `True`, truncates large responses and returns them without raising an error. Otherwise, a `ResponseTooLargeError` is raised when a response is truncated.   
`follow_redirects` |  If set to `True` (the default), redirects are transparently followed. If there are less than five redirects, the response contains the final destination's payload, and the response status is `200`. You lose, however, the redirect chain information. If set to `False`, you see the `HTTP` response yourself, including the `Location` header, and redirects are not followed.   
`deadline` |  Deadline in seconds for the operation.   
`validate_certificate` |  If set to `True`, requests are not sent to the server unless the certificate is valid, signed by a trusted `CA`, and the host name matches the certificate. A value of `None` (default) indicates that the behavior will be chosen by the underlying `urlfetch` implementation.   
  
## Returns  
  
---  
  
`object` |  An object containing following fields: 

  * `content`: A `string` that contains the response from the server.
  * `status_code`: The `HTTP` status code that was returned by the server.
  * `headers`: The `dict` of headers that was returned by the server. 

  
  
## Raises  
  
---  
  
`urlfetch_errors.Error` |  If an error occurs. See the `urlfetch_errors` module for more information.   
  
#### Note:

`HTTP` errors are returned as a part of the return structure. `HTTP` errors like `404` do not result in an exception. See `urlfetch_errors` for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
