---
url: https://docs.cloud.google.com/resource-manager/reference/mcp/search_projects/
title: MCP Tools Reference: cloudresourcemanager.googleapis.com \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:18.027776+00:00
---

# MCP Tools Reference: cloudresourcemanager.googleapis.com  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/mcp/search_projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  MCP Tools Reference: cloudresourcemanager.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `search_projects`

Searches for Google Cloud projects. This tool may be used whenever any tools or conversation context requires a GCP project. A SearchProjects call with an empty query will return all projects the user has access to, which can be used to determine a curated list of projects. The tool can find projects by parent (e.g., 'parent:folders/223'), project ID (e.g., 'projectId:my-project-id'), or other filters.

The following sample demonstrate how to use `curl` to invoke the `search_projects` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://cloudresourcemanager.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "search_projects",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request sent to the `SearchProjects` method.

### SearchProjectsRequest

JSON representation  
---  
      
    
    {
      "query": string,
      "pageToken": string,
      "pageSize": integer
    }  
  
Fields  
---  
`query` |  `string` Optional. A query string for searching for projects that the caller has `resourcemanager.projects.get` permission to. If multiple fields are included in the query, then it will return results that match any of the fields. Some eligible fields are:
    
    
    | Field                   | Description                                  |
    |-------------------------|----------------------------------------------|
    | displayName, name       | Filters by displayName.                      |
    | parent                  | Project's parent (for example: folders/123, organizations/*). Prefer parent field over parent.type and parent.id.|
    | parent.type             | Parent's type: `folder` or `organization`.   |
    | parent.id               | Parent's id number (for example: 123)        |
    | id, projectId           | Filters by projectId.                        |
    | state, lifecycleState   | Filters by state.                            |
    | labels                  | Filters by label name or value.              |
    | labels.\<key\> (where *key* is the name of a label) | Filters by label name.|
    

Search expressions are case insensitive.Some examples queries:
    
    
    | Query            | Description                                         |
    |------------------|-----------------------------------------------------|
    | name:how*        | The project's name starts with "how".               |
    | name:Howl        | The project's name is `Howl` or `howl`.             |
    | name:HOWL        | Equivalent to above.                                |
    | NAME:howl        | Equivalent to above.                                |
    | labels.color:*   | The project has the label `color`.                  |
    | labels.color:red | The project's label `color` has the value `red`.    |
    | labels.color:red labels.size:big | The project's label `color` has the
    value `red` or its label `size` has the value `big`.                     |
    

If no query is specified, the call will return projects for which the user has the `resourcemanager.projects.get` permission.  
`pageToken` |  `string` Optional. A pagination token returned from a previous call to `ListProjects` that indicates from where listing should continue.  
`pageSize` |  `integer` Optional. The maximum number of projects to return in the response. The server can return fewer projects than requested. If unspecified, server picks an appropriate default.  
  
## Output Schema

A page of the response received from the `SearchProjects` method.

A paginated response where more pages are available has `next_page_token` set. This token can be used in a subsequent request to retrieve the next request page.

### SearchProjectsResponse

JSON representation  
---  
      
    
    {
      "projects": [
        {
          object ([Project](https://docs.cloud.google.com/resource-manager/reference/mcp/search_projects#Output.Schema.Project))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`projects[]` |  `object (`[Project](https://docs.cloud.google.com/resource-manager/reference/mcp/search_projects#Output.Schema.Project)`)` The list of Projects that matched the list filter query. This list can be paginated.  
`nextPageToken` |  `string` Pagination token.If the result set is too large to fit in a single response, this token is returned. It encodes the position of the current result cursor. Feeding this value into a new list request with the `page_token` parameter gives the next page of the results.When `next_page_token` is not filled in, there is no next page and the list returned is the last page in the result set.Pagination tokens have a limited lifetime.  
  
### Project

JSON representation  
---  
      
    
    {
      "name": string,
      "parent": string,
      "projectId": string,
      "state": enum (State),
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "etag": string,
      "labels": {
        string: string,
        ...
      },
      "tags": {
        string: string,
        ...
      },
      "configuredCapabilities": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. The unique resource name of the project. It is an int64 generated number prefixed by "projects/".Example: `projects/415104041262`  
`parent` |  `string` Optional. A reference to a parent Resource. eg., `organizations/123` or `folders/876`.  
`projectId` |  `string` Immutable. The unique, user-assigned id of the project. It must be 6 to 30 lowercase ASCII letters, digits, or hyphens. It must start with a letter. Trailing hyphens are prohibited.Example: `tokyo-rain-123`  
`state` |  `enum (`State`)` Output only. The project lifecycle state.  
`displayName` |  `string` Optional. A user-assigned display name of the project. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point.Example: `My Project`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time this resource was modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this resource was requested for deletion.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. A checksum computed by the server based on the current value of the Project resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`labels` |  `map (key: string, value: string)` Optional. The labels associated with this project.Label keys must be between 1 and 63 characters long and must conform to the following regular expression: [a-z]([-a-z0-9]*[a-z0-9])?.Label values must be between 0 and 63 characters long and must conform to the regular expression ([a-z]([-a-z0-9]*[a-z0-9])?)?.No more than 64 labels can be associated with a given resource.Clients should store labels in a representation such as JSON that does not depend on specific characters being disallowed.Example: `"myBusinessDimension" : "businessValue"`An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tag keys/values directly bound to this project. Each item in the map must be expressed as " : ". For example: "123/environment" : "production", "123/costCenter" : "marketing"Note: Currently this field is in Preview.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`configuredCapabilities[]` |  `string` Output only. If this project is a Management Project, list of capabilities configured on the parent folder. Note, presence of any capability implies that this is a Management Project. Example: `folders/123/capabilities/app-management`. OUTPUT ONLY.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### TagsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ✅

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-02 UTC."],[],[]] 
