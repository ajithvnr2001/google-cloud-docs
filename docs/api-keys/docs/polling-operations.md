---
url: https://docs.cloud.google.com/api-keys/docs/polling-operations/
title: Polling long-running operations \u00a0|\u00a0 API Keys API Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:39.641596+00:00
---

# Polling long-running operations  |  API Keys API Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-keys/docs/polling-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ API Keys API Documentation ](https://docs.cloud.google.com/api-keys/docs)
  * [ Guides ](https://docs.cloud.google.com/api-keys/docs/how-to)



Send feedback 

#  Polling long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to determine the completion status of asynchronous methods. These methods return a long-running [operation](https://docs.cloud.google.com/api-keys/docs/reference/rest/v2/operations) that provides information about the progress of the operation and its final status.

The following methods return a long-running operation:

  * `CreateKey`
  * `UpdateKey`
  * `DeleteKey`
  * `UndeleteKey`



When you make a request to one of these methods, on success, the method returns an operation identifier in the `name` field, which represents ongoing work on the server, for example:
    
    
    {
      "name": "operations/akmf.6573437d-47c1-42c4-b817-0562f514f6ff"
    }

To check the status of the operation, use the [`operations.get`](https://docs.cloud.google.com/api-keys/docs/reference/rest/v2/operations/get) method with the value from the `name` field:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         'https://apikeys.googleapis.com/v2/operations/akmf.6573437d-47c1-42c4-b817-0562f514f6ff'

To poll an operation, we recommended that you repeatedly invoke the `operations.get` method with a 10-second backoff until the response includes `"done": true`:
    
    
    {
      "name": "operations/akmf.6573437d-47c1-42c4-b817-0562f514f6ff",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.api.apikeys.v2.Key",
        "name": "projects/103621867718/locations/global/keys/b7ff1f9f-8275-410a-94dd-3855ee9b5dd2",
        "keyString": "----REDACTED----",
        "createTime": "2019-02-04T23:56:28.531Z",
        "uid": "b7ff1f9f-8275-410a-94dd-3855ee9b5dd2",
        "updateTime": "2019-02-04T23:56:28.531Z",
        "restrictions": {
          "browserKeyRestrictions": {
          }
        },
        "etag": "k0bsYGkIvSxDVwNxyw49NQ=="
      }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
