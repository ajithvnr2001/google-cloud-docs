---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/list/
title: Method: projects.instances.list \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:01.793285+00:00
---

# Method: projects.instances.list  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all instances in the given project.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`GET https://spanner.googleapis.com/v1/{parent=projects/*}/instances`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the project for which a list of instances is requested. Values are of the form `projects/<project>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.instances.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Number of instances to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`pageToken` |  `string` If non-empty, `pageToken` should contain a `[nextPageToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/list#body.ListInstancesResponse.FIELDS.next_page_token)` from a previous `[ListInstancesResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/list#body.ListInstancesResponse)`.  
`filter` |  `string` An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are:

  * `name`
  * `displayName`
  * `labels.key` where key is the name of a label

Some examples of using filters are:

  * `name:*` \--> The instance has a name.
  * `name:Howl` \--> The instance's name contains the string "howl".
  * `name:HOWL` \--> Equivalent to above.
  * `NAME:howl` \--> Equivalent to above.
  * `labels.env:*` \--> The instance has the label "env".
  * `labels.env:dev` \--> The instance has the label "env" and the value of the label contains the string "dev".
  * `name:howl labels.env:dev` \--> The instance's name contains "howl" and it has the label "env" with its value containing "dev".

  
`instanceDeadline` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Deadline used while retrieving metadata for instances. Instances whose metadata cannot be retrieved within this deadline will be added to `[unreachable](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/list#body.ListInstancesResponse.FIELDS.unreachable)` in `[ListInstancesResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/list#body.ListInstancesResponse)`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Request body

The request body must be empty.

### Response body

The response for `[instances.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/list#google.spanner.admin.instance.v1.InstanceAdmin.ListInstances)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instances": [
        {
          object ([Instance](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#Instance))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`instances[]` |  `object (`[Instance](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances#Instance)`)` The list of requested instances.  
`nextPageToken` |  `string` `nextPageToken` can be sent in a subsequent `[instances.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/list#google.spanner.admin.instance.v1.InstanceAdmin.ListInstances)` call to fetch more of the matching instances.  
`unreachable[]` |  `string` The list of unreachable instances. It includes the names of instances whose metadata could not be retrieved within `[instanceDeadline](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances/list#body.QUERY_PARAMETERS.instance_deadline)`.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
