---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1beta1/projects.databases.documents/delete/
title: Method: googleapis.firestore.v1beta1.projects.databases.documents.delete \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:32.963831+00:00
---

# Method: googleapis.firestore.v1beta1.projects.databases.documents.delete  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1beta1/projects.databases.documents/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.firestore.v1beta1.projects.databases.documents.delete Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a document.

Every document in Cloud Firestore is uniquely identified by its location within the database. Documents live in collections and the names of documents within a collection are unique. Note that `{document_path}` refers to the fully specified document path and includes the collection ID. For more information, see [Cloud Firestore data model](https://firebase.google.com/docs/firestore/data-model) and the [Cloud Firestore connector sample](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/Overview#firestore-sample).

## Arguments

Parameters  
---  
`name` |  `string` Required. The resource name of the Document to delete. In the format: `projects/{project_id}/databases/{database_id}/documents/{document_path}`.  
`currentDocument.exists` |  `boolean` When set to `true`, the target document must exist. When set to `false`, the target document must not exist.  
`currentDocument.updateTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` When set, the target document must exist and have been last updated at that time.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response will be empty.

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/firestore/docs/reference/rest/v1beta1/projects.databases.documents/delete).

### YAML
    
    
    - delete:
        call: googleapis.firestore.v1beta1.projects.databases.documents.delete
        args:
            name: ...
            currentDocument:
                exists: ...
                updateTime: ...
        result: deleteResult

### JSON
    
    
    [
      {
        "delete": {
          "call": "googleapis.firestore.v1beta1.projects.databases.documents.delete",
          "args": {
            "name": "...",
            "currentDocument": {
              "exists": "...",
              "updateTime": "..."
            }
          },
          "result": "deleteResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
