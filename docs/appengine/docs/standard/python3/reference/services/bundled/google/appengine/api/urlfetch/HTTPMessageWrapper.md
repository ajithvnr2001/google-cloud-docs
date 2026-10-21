---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/HTTPMessageWrapper/
title: google.appengine.api.urlfetch.HTTPMessageWrapper \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:01:14.296977+00:00
---

# google.appengine.api.urlfetch.HTTPMessageWrapper  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/urlfetch/HTTPMessageWrapper/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.urlfetch.HTTPMessageWrapper Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/urlfetch.py#L491-L498) Basic message object. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type) A message object is defined as something that has a bunch of RFC 2822 headers and a payload. It may optionally have an envelope header (a.k.a. Unix-From or From_ header). If the message is a container (i.e. a multipart or a message/rfc822), then the payload is a list of Message objects, otherwise it is a string. Message objects implement part of the `mapping' interface, which assumes there is exactly one occurrence of the header per message. Some headers do in fact appear multiple times (e.g. Received) and for those headers, you must use the explicit API to set or get all the headers. Not all of the mapping methods are implemented. | 

## Attributes  
  
---  
  
`type` |   
  
## Methods

### `getallmatchingheaders`
    
    
    getallmatchingheaders(
        name
    )
    

Find all header lines matching a given header name.

Look through the list of headers and find all lines matching a given header name (and their continuation lines). A list of the lines is returned, without interpretation. If the header does not occur, an empty list is returned. If the header occurs multiple times, all occurrences are returned. Case is not important in the header name.

### `getheaders`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/urlfetch.py#L493-L494)
    
    
    getheaders(
        key
    )
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
