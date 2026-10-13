---
url: https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.batch
title: Module batch (3.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:53.098968+00:00
---

# Module batch (3.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.batch

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module batch (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.1  3.14.1  3.13.1  3.12.1  3.11.0  3.10.1  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.1  3.3.1  3.2.0  3.1.1  3.0.0  2.19.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.0  1.44.0  1.43.0  1.42.3  1.41.1  1.40.0  1.39.0  1.38.0  1.37.1  1.36.2  1.35.1  1.34.0  1.33.0  1.32.0  1.31.2  1.30.0  1.29.0  1.28.1  1.27.0  1.26.0  1.25.0  1.24.1  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0 

Batch updates / deletes of storage buckets / blobs.

A batch request is a single standard HTTP request containing multiple Cloud Storage JSON API calls. Within this main HTTP request, there are multiple parts which each contain a nested HTTP request. The body of each part is itself a complete HTTP request, with its own verb, URL, headers, and body.

Note that Cloud Storage does not support batch operations for uploading or downloading. Additionally, the current batch design does not support library methods whose return values depend on the response payload. See more details in the [Sending Batch Requests official guide](https://cloud.google.com/storage/docs/batch).

Examples of situations when you might want to use the Batch module: `blob.patch()` `blob.update()` `blob.delete()` `bucket.delete_blob()` `bucket.patch()` `bucket.update()`

## Classes 

### [Batch](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.batch.Batch)
    
    
    Batch(client, raise_exception=True)

Proxy an underlying connection, batching up change operations.

**Warning:** Cloud Storage does not support batch operations for uploading or downloading. Additionally, the current batch design does not support library methods whose return values depend on the response payload. 

**Parameters**  
---  
**Name** | **Description**  
`client` |  `[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client)`   
The client to use for making connections.  
`raise_exception` |  `bool`   
(Optional) Defaults to True. If True, instead of adding exceptions to the list of return responses, the final exception will be raised. Note that exceptions are unwrapped after all operations are complete in success or failure, and only the last exception is raised.  
  
### [MIMEApplicationHTTP](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.batch.MIMEApplicationHTTP)
    
    
    MIMEApplicationHTTP(method, uri, headers, body)

MIME type for `application/http`.

Constructs payload from headers and body

**Parameters**  
---  
**Name** | **Description**  
`method` |  `str`   
HTTP method  
`uri` |  `str`   
URI for HTTP request  
`headers` |  `dict`   
HTTP headers  
`body` |  `str`   
(Optional) HTTP payload  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
