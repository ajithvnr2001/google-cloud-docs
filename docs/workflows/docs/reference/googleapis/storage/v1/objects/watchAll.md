---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/storage/v1/objects/watchAll/
title: Method: googleapis.storage.v1.objects.watchAll \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:23.986134+00:00
---

# Method: googleapis.storage.v1.objects.watchAll  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/storage/v1/objects/watchAll/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.storage.v1.objects.watchAll Stay organized with collections  Save and categorize content based on your preferences. 

Watch for changes on all objects in a bucket.

## Arguments

Parameters  
---  
`bucket` |  `string` Required. Name of the bucket in which to look for objects.  
`delimiter` |  `string` Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.  
`endOffset` |  `string` Filter results to objects whose names are lexicographically before endOffset. If startOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).  
`includeTrailingDelimiter` |  `boolean` If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes.  
`maxResults` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Maximum number of items plus prefixes to return in a single page of responses. As duplicate prefixes are omitted, fewer total results may be returned than requested. The service will use this parameter or 1,000 items, whichever is smaller.  
`pageToken` |  `string` A previously-returned page token representing part of the larger set of results to view.  
`prefix` |  `string` Filter results to objects whose names begin with this prefix.  
`projection` |  `enum` Set of properties to return. Defaults to noAcl.  
Enum type. Can be one of the following:  
`full` | Include all properties.  
`noAcl` | Omit the owner, acl property.  
`startOffset` |  `string` Filter results to objects whose names are lexicographically equal to or after startOffset. If endOffset is also set, the objects listed will have names between startOffset (inclusive) and endOffset (exclusive).  
`userProject` |  `string` The project to be billed for this request. Required for Requester Pays buckets.  
`versions` |  `boolean` If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning.  
`body` |  `object ([Channel](https://cloud.google.com/workflows/docs/reference/googleapis/storage/v1/Overview#Channel))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`Channel`](https://cloud.google.com/workflows/docs/reference/googleapis/storage/v1/Overview#Channel).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/storage/docs/json_api/v1/objects/watchAll).

### YAML
    
    
    - watchAll:
        call: googleapis.storage.v1.objects.watchAll
        args:
            bucket: ...
            delimiter: ...
            endOffset: ...
            includeTrailingDelimiter: ...
            maxResults: ...
            pageToken: ...
            prefix: ...
            projection: ...
            startOffset: ...
            userProject: ...
            versions: ...
            body:
                address: ...
                expiration: ...
                id: ...
                kind: ...
                params: ...
                payload: ...
                resourceId: ...
                resourceUri: ...
                token: ...
                type: ...
        result: watchAllResult

### JSON
    
    
    [
      {
        "watchAll": {
          "call": "googleapis.storage.v1.objects.watchAll",
          "args": {
            "bucket": "...",
            "delimiter": "...",
            "endOffset": "...",
            "includeTrailingDelimiter": "...",
            "maxResults": "...",
            "pageToken": "...",
            "prefix": "...",
            "projection": "...",
            "startOffset": "...",
            "userProject": "...",
            "versions": "...",
            "body": {
              "address": "...",
              "expiration": "...",
              "id": "...",
              "kind": "...",
              "params": "...",
              "payload": "...",
              "resourceId": "...",
              "resourceUri": "...",
              "token": "...",
              "type": "..."
            }
          },
          "result": "watchAllResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
