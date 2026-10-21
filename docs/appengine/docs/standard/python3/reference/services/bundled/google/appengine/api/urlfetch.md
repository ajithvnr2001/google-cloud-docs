---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/
title: Module: google.appengine.api.urlfetch \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:03:20.017858+00:00
---

# Module: google.appengine.api.urlfetch  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.urlfetch Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/urlfetch.py) URL downloading API.

## Classes

[`class ConnectionClosedError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/ConnectionClosedError): The target server prematurely closed the connection. [`class DNSLookupFailedError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/DNSLookupFailedError): The DNS lookup for a URL failed. [`class DeadlineExceededError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/DeadlineExceededError): The URL was not fetched because the deadline was exceeded. [`class DownloadError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/DownloadError): The URL could not be retrieved. [`class Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/Error): Base URL fetcher error type. [`class HTTPMessageWrapper`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/HTTPMessageWrapper): Basic message object. [`class InternalTransientError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/InternalTransientError): An internal transient error occurred. [`class InvalidMethodError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/InvalidMethodError): An invalid value was provided for `method`. [`class InvalidURLError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/InvalidURLError): The URL given was empty or invalid. [`class MalformedReplyError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/MalformedReplyError): The target server returned an invalid HTTP response. [`class PayloadTooLargeError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/PayloadTooLargeError): The request payload exceeds the limit. [`class SSLCertificateError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/SSLCertificateError): An invalid server certificate was presented. [`class TooManyRedirectsError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/TooManyRedirectsError): `follow_redirects` was set to `True`, and the redirect limit was hit.

## Functions

[`CreateHTTPHeaders(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/CreateHTTPHeaders): Creates `HTTPHeaders` that are compatible with both Python 2 or Python 3. [`Fetch(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/Fetch): Fetches the given HTTP `url`, blocking until the result is returned. [`create_rpc(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/create_rpc): Creates an RPC object for use with the URL Fetch API. [`fetch(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/Fetch): Fetches the given HTTP `url`, blocking until the result is returned. [`get_default_fetch_deadline(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/get_default_fetch_deadline): Gets the default value for `create_rpc()`'s `deadline` parameter. [`make_fetch_call(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/make_fetch_call): Executes the RPC call to fetch a given `HTTP` URL. [`set_default_fetch_deadline(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/set_default_fetch_deadline): Sets the default value for `create_rpc()`'s `deadline` parameter. | 

## Other Members  
  
---  
  
DELETE |  `5`  
GET |  `1`  
HEAD |  `3`  
MAX_REDIRECTS |  `5`  
PATCH |  `6`  
POST |  `2`  
PUT |  `4`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
