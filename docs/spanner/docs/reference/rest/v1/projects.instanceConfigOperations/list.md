---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigOperations/list/
title: Method: projects.instanceConfigOperations.list \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:59.295758+00:00
---

# Method: projects.instanceConfigOperations.list  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigOperations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instanceConfigOperations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the user-managed instance configuration long-running operations in the given project. An instance configuration operation has a name of the form `projects/<project>/instanceConfigs/<instanceConfig>/operations/<operation>`. The long-running operation metadata field type `metadata.type_url` describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations. Operations returned are ordered by `operation.metadata.value.start_time` in descending order starting from the most recently started operation.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`GET https://spanner.googleapis.com/v1/{parent=projects/*}/instanceConfigOperations`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project of the instance configuration operations. Values are of the form `projects/<project>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.instanceConfigOperations.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` An expression that filters the list of returned operations.A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive.The following fields in the Operation are eligible for filtering:

  * `name` \- The name of the long-running operation
  * `done` \- False if the operation is in progress, else true.
  * `metadata.@type` \- the type of metadata. For example, the type string for `[CreateInstanceConfigMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateInstanceConfigMetadata)` is `type.googleapis.com/google.spanner.admin.instance.v1.CreateInstanceConfigMetadata`.
  * `metadata.<field_name>` \- any field in metadata.value. `metadata.@type` must be specified first, if filtering on metadata fields.
  * `error` \- Error associated with the long-running operation.
  * `response.@type` \- the type of response.
  * `response.<field_name>` \- any field in response.value.

You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic. However, you can specify AND, OR, and NOT logic explicitly.Here are a few examples:

  * `done:true` \- The operation is complete.
  * `(metadata.@type=` \ `type.googleapis.com/google.spanner.admin.instance.v1.CreateInstanceConfigMetadata) AND` \ `(metadata.instance_config.name:custom-config) AND` \ `(metadata.progress.start_time < \"2021-03-28T14:50:00Z\") AND` \ `(error:*)` \- Return operations where: 
    * The operation's metadata type is `[CreateInstanceConfigMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateInstanceConfigMetadata)`.
    * The instance configuration name contains "custom-config".
    * The operation started before 2021-03-28T14:50:00Z.
    * The operation resulted in an error.

  
`pageSize` |  `integer` Number of operations to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`pageToken` |  `string` If non-empty, `pageToken` should contain a `[nextPageToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigOperations/list#body.ListInstanceConfigOperationsResponse.FIELDS.next_page_token)` from a previous `[ListInstanceConfigOperationsResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigOperations/list#body.ListInstanceConfigOperationsResponse)` to the same `parent` and with the same `filter`.  
  
### Request body

The request body must be empty.

### Response body

The response for `[instanceConfigOperations.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigOperations/list#google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigOperations)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "operations": [
        {
          object ([Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`operations[]` |  `object (`[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`)` The list of matching instance configuration long-running operations. Each operation's name will be prefixed by the name of the instance configuration. The operation's metadata field type `metadata.type_url` describes the type of the metadata.  
`nextPageToken` |  `string` `nextPageToken` can be sent in a subsequent `[instanceConfigOperations.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigOperations/list#google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigOperations)` call to fetch more of the matching metadata.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
