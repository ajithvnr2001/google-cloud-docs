---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/projects.databases.collectionGroups.fields/patch/
title: Method: googleapis.firestore.v1.projects.databases.collectionGroups.fields.patch \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:03.441172+00:00
---

# Method: googleapis.firestore.v1.projects.databases.collectionGroups.fields.patch  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/projects.databases.collectionGroups.fields/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.firestore.v1.projects.databases.collectionGroups.fields.patch Stay organized with collections  Save and categorize content based on your preferences. 

Updates a field configuration. Currently, field updates apply only to single field index configuration. However, calls to FirestoreAdmin.UpdateField should provide a field mask to avoid changing any configuration that the caller isn't aware of. The field mask should be specified as: `{ paths: "index_config" }`. This call returns a google.longrunning.Operation which may be used to track the status of the field update. The metadata for the operation will be the type FieldOperationMetadata. To configure the default field settings for the database, use the special `Field` with resource name: `projects/{project_id}/databases/{database_id}/collectionGroups/__default__/fields/*`.

This method waits—the workflow execution is paused—until the operation is complete, fails, or times out. The default timeout value is `1800` seconds (30 minutes) and can be changed to a maximum value of `31536000` seconds (one year) for long-running operations using the `connector_params` field. See the [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis).

The connector uses polling to monitor the long-running operation, which might generate additional billable steps. For more information about retries and long-running operations, refer to [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).

The polling policy for the long-running operation can be configured. To set the connector-specific parameters (`connector_params`), refer to [Invoke a connector call](https://docs.cloud.google.com/workflows/docs/reference/googleapis#invoke_a_connector_call).

## Arguments

Parameters  
---  
`name` |  `string` Required. A field name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_path}` A field path may be a simple field name, e.g. `address` or a path to fields within map_value , e.g. `address.city`, or a special field path. The only valid special field is `*`, which represents any field. Field paths may be quoted using `(backtick). The only character that needs to be escaped within a quoted field path is the backtick character itself, escaped using a backslash. Special characters in field paths that must be quoted include:`_`,`.`, ``` (backtick),`[`,`]`, as well as any ascii symbolic characters. Examples: (Note: Comments here are written in markdown syntax, so there is an additional layer of backticks to represent a code block)``address.city``represents a field named`address.city`, not the map key`city`in the field`address`.``_``represents a field named` _`, not any field. A special`Field`contains the default indexing settings for all fields. This field's resource name is:`projects/{project_id}/databases/{database_id}/collectionGroups/**default** /fields/_`Indexes defined on this`Field`will be applied to all fields which do not have their own`Field` index configuration.  
`updateMask` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` A mask, relative to the field. If specified, only configuration specified by this field_mask will be updated in the field.  
`body` |  `object ([GoogleFirestoreAdminV1Field](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Field))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
`OperationError` | If the long-running operation finished unsuccessfully.  
`ResponseTypeError` | If the long-running operation returned a response of the wrong type.  
  
## Response

If successful, the response contains an instance of [`GoogleLongrunningOperation`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleLongrunningOperation).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.fields/patch).

### YAML
    
    
    - patch:
        call: googleapis.firestore.v1.projects.databases.collectionGroups.fields.patch
        args:
            name: ...
            updateMask: ...
            body:
                indexConfig:
                    indexes: ...
                name: ...
        result: patchResult

### JSON
    
    
    [
      {
        "patch": {
          "call": "googleapis.firestore.v1.projects.databases.collectionGroups.fields.patch",
          "args": {
            "name": "...",
            "updateMask": "...",
            "body": {
              "indexConfig": {
                "indexes": "..."
              },
              "name": "..."
            }
          },
          "result": "patchResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
