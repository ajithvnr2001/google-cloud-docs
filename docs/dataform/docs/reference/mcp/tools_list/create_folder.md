---
url: https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/create_folder/
title: MCP Tools Reference: dataform.googleapis.com \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:36.383799+00:00
---

# MCP Tools Reference: dataform.googleapis.com  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/create_folder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  MCP Tools Reference: dataform.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `create_folder`

Create a new Dataform folder in a given Google Cloud project and location.

Folders organize Dataform repositories into a hierarchy. Creating a folder doesn't move any repositories into it. To place a repository inside a folder, set the `containing_folder` parameter value when using the `create_repository` tool.

Don't attempt to move an existing repository into a folder using the `update_repository` tool. Once a repository is created, its `containing_folder` field can't be modified using MCP tools.

The `parent` parameter value must be in the format `projects/{project_id}/locations/{location}`.

The `folder.display_name` parameter value is required and specifies the folder's user-friendly name.

The following code sample shows how to use `curl` to call the `create_folder` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://dataform.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "create_folder",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

`CreateFolder` request message.

### CreateFolderRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "folder": {
        object ([Folder](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/create_folder#Input.Schema.Folder))
      },
      "folderId": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The location in which to create the Folder. Must be in the format `projects/*/locations/*`.  
`folder` |  `object (`[Folder](https://docs.cloud.google.com/dataform/docs/reference/mcp/tools_list/create_folder#Input.Schema.Folder)`)` Required. The Folder to create.  
`folderId  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: This field is not used. The resource name is generated automatically. The ID to use for the Folder, which will become the final component of the Folder's resource name.  
  
### Folder

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "containingFolder": string,
      "teamFolderName": string,
      "createTime": string,
      "updateTime": string,
    
      // Union field _internal_metadata can be only one of the following:
      "internalMetadata": string
      // End of list of possible types for union field _internal_metadata.
    
      // Union field _creator_iam_principal can be only one of the following:
      "creatorIamPrincipal": string
      // End of list of possible types for union field _creator_iam_principal.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The Folder's name.  
`displayName` |  `string` Required. The Folder's user-friendly name.  
`containingFolder` |  `string` Optional. The containing Folder resource name. This should take the format: projects/{project}/locations/{location}/folders/{folder}, projects/{project}/locations/{location}/teamFolders/{teamFolder}, or just "" if this is a root Folder. This field can only be updated through MoveFolder.  
`teamFolderName` |  `string` Output only. The resource name of the TeamFolder that this Folder is associated with. This should take the format: projects/{project}/locations/{location}/teamFolders/{teamFolder}. If this is not set, the Folder is not associated with a TeamFolder and is a UserFolder.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the Folder was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the Folder was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `_internal_metadata`.`_internal_metadata` can be only one of the following:  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
Union field `_creator_iam_principal`.`_creator_iam_principal` can be only one of the following:  
`creatorIamPrincipal` |  `string` Output only. The IAM principal identifier of the creator of the Folder.  
  
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
  
## Output Schema

Represents a Dataform Folder. This is a resource that is used to organize Files and other Folders and provide hierarchical access controls.

### Folder

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "containingFolder": string,
      "teamFolderName": string,
      "createTime": string,
      "updateTime": string,
    
      // Union field _internal_metadata can be only one of the following:
      "internalMetadata": string
      // End of list of possible types for union field _internal_metadata.
    
      // Union field _creator_iam_principal can be only one of the following:
      "creatorIamPrincipal": string
      // End of list of possible types for union field _creator_iam_principal.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The Folder's name.  
`displayName` |  `string` Required. The Folder's user-friendly name.  
`containingFolder` |  `string` Optional. The containing Folder resource name. This should take the format: projects/{project}/locations/{location}/folders/{folder}, projects/{project}/locations/{location}/teamFolders/{teamFolder}, or just "" if this is a root Folder. This field can only be updated through MoveFolder.  
`teamFolderName` |  `string` Output only. The resource name of the TeamFolder that this Folder is associated with. This should take the format: projects/{project}/locations/{location}/teamFolders/{teamFolder}. If this is not set, the Folder is not associated with a TeamFolder and is a UserFolder.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the Folder was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the Folder was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `_internal_metadata`.`_internal_metadata` can be only one of the following:  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
Union field `_creator_iam_principal`.`_creator_iam_principal` can be only one of the following:  
`creatorIamPrincipal` |  `string` Output only. The IAM principal identifier of the creator of the Folder.  
  
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
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
