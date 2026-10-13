---
url: https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries/
title: MCP Tools Reference: dataplex.googleapis.com \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:29.683115+00:00
---

# MCP Tools Reference: dataplex.googleapis.com  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  MCP Tools Reference: dataplex.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `search_entries`

Searches for data assets matching the given query and scope in the Knowledge Catalog (formerly known as Dataplex).

Use this method to discover data assets (such as BigQuery tables, datasets, Cloud Storage buckets) across your Google Cloud organization or projects.

**Best Practices for Agents** : - Always make queries as specific as possible to reduce latency and token usage. Instead of searching broadly, combine filters like `system`, `type`, and `name`. Example: `system:bigquery AND type:table AND name:customers` \- Use `page_size` to limit the volume of returned results, especially during exploratory phases. - This method returns basic entry information. To retrieve rich, LLM-ready metadata (including schemas, quality scores, and usage patterns), parse the `dataplex_entry.name` from the results and pass them to `LookupContext`. Alternatively, you can use `LookupEntry` to get detailed metadata about the entry.

The following sample demonstrate how to use `curl` to invoke the `search_entries` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://dataplex.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "search_entries",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for Knowledge Catalog (formerly known as Dataplex) SearchEntries method.

### SearchEntriesRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "query": string,
      "pageSize": integer,
      "orderBy": enum ([OrderBy](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Input.Schema.OrderBy)),
      "scopeType": enum ([ScopeType](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Input.Schema.ScopeType)),
      "scopeId": string,
      "pageToken": string
    }  
  
Fields  
---  
`projectId` |  `string` Required. The project to which the request should be attributed. To execute the search, the caller must have the `dataplex.projects.search` permission on the project field.  
`query` |  `string` Required. A query string for searching entries, following Knowledge Catalog search syntax. Supports logical operators (AND, OR, NOT) and grouping.**Syntax Guide** : - **Filter by System** : `system:bigquery`, `system:storage` (for Cloud Storage) - **Filter by Type** : `type:table`, `type:dataset`, `type:fileset` \- **Filter by Name/Title** : `name:my_table` or `title:"My Table"` \- **Free Text** : Search for words like `sales` or `finance` anywhere in the metadata.**Examples** : - Find a specific BigQuery table: `system:bigquery AND type:table AND name:orders` \- Find filesets in a specific bucket area: `system:storage AND type:fileset AND path:prod` \- Find anything related to "marketing" that is a table: `type:table AND marketing`Warning: Performing broad searches without specific filters (e.g., type:table) can be slow and consume significant resources. When performing exploratory searches, always use the page_size parameter to limit the number of results returned.  
`pageSize` |  `integer` Optional. Number of results in the search page. If <=0, then defaults to 10. Max limit for page_size is 1000. Throws an invalid argument for page_size > 1000.  
`orderBy` |  `enum (`[OrderBy](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Input.Schema.OrderBy)`)` Optional. Specifies the ordering of results.  
`scopeType` |  `enum (`[ScopeType](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Input.Schema.ScopeType)`)` Optional. Type of the scope to limit the search space.  
`scopeId` |  `string` Optional. The ID of the scope to limit the search space (e.g. organization ID, or project ID/number depending on the scope_type).  
`pageToken` |  `string` Optional. Page token received from a previous `SearchEntries` call. Provide this to retrieve the subsequent page.  
  
### OrderBy

Specifies the ordering of results.

Enums  
---  
`ORDER_BY_UNSPECIFIED` | Default unspecified value.  
`RELEVANCE` | Order by relevance.  
`LAST_MODIFIED_TIMESTAMP` | Order by last modified timestamp.  
`LAST_MODIFIED_TIMESTAMP_ASC` | Order by last modified timestamp in ascending order.  
`LAST_MODIFIED_TIMESTAMP_DESC` | Order by last modified timestamp in descending order.  
  
### ScopeType

Type of scope to limit the search space.

Enums  
---  
`SCOPE_TYPE_UNSPECIFIED` | Default unspecified value.  
`ORGANIZATION` | Limit the search to an organization.  
`PROJECT` | Limit the search to a project.  
  
## Output Schema

Response message for Knowledge Catalog (formerly known as Dataplex) SearchEntries method.

### SearchEntriesResponse

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([SearchEntriesResult](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.SearchEntriesResult))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`results[]` |  `object (`[SearchEntriesResult](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.SearchEntriesResult)`)` The list of entries that match the search query.  
`nextPageToken` |  `string` Optional. Token to retrieve the next page of results, or empty if there are no more results in the list.  
  
### SearchEntriesResult

JSON representation  
---  
      
    
    {
      "dataplexEntry": {
        object ([Entry](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.Entry))
      }
    }  
  
Fields  
---  
`dataplexEntry` |  `object (`[Entry](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.Entry)`)` The entry that matches the search query.  
  
### Entry

JSON representation  
---  
      
    
    {
      "name": string,
      "entryType": string,
      "createTime": string,
      "updateTime": string,
      "aspects": {
        string: {
          object ([Aspect](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.Aspect))
        },
        ...
      },
      "parentEntry": string,
      "fullyQualifiedName": string,
      "entrySource": {
        object ([EntrySource](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.EntrySource))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The relative resource name of the entry, in the format `projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}`.  
`entryType` |  `string` Required. Immutable. The relative resource name of the entry type that was used to create this entry, in the format `projects/{project_id_or_number}/locations/{location_id}/entryTypes/{entry_type_id}`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the entry was created in Dataplex Universal Catalog.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the entry was last updated in Dataplex Universal Catalog.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`aspects` |  `map (key: string, value: object (`[Aspect](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.Aspect)`))` Optional. The aspects that are attached to the entry. Depending on how the aspect is attached to the entry, the format of the aspect key can be one of the following:

  * If the aspect is attached directly to the entry: `{project_id_or_number}.{location_id}.{aspect_type_id}`
  * If the aspect is attached to an entry's path: `{project_id_or_number}.{location_id}.{aspect_type_id}@{path}`

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`parentEntry` |  `string` Optional. Immutable. The resource name of the parent entry, in the format `projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}`.  
`fullyQualifiedName` |  `string` Optional. A name for the entry that can be referenced by an external system. For more information, see [Fully qualified names](https://cloud.google.com/data-catalog/docs/fully-qualified-names). The maximum size of the field is 4000 characters.  
`entrySource` |  `object (`[EntrySource](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.EntrySource)`)` Optional. Information related to the source system of the data resource that is represented by the entry.  
  
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
  
### AspectsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([Aspect](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.Aspect))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[Aspect](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.Aspect)`)`  
  
### Aspect

JSON representation  
---  
      
    
    {
      "aspectType": string,
      "path": string,
      "createTime": string,
      "updateTime": string,
      "data": {
        object
      },
      "aspectSource": {
        object ([AspectSource](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.AspectSource))
      }
    }  
  
Fields  
---  
`aspectType` |  `string` Output only. The resource name of the type used to create this Aspect.  
`path` |  `string` Output only. The path in the entry under which the aspect is attached.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the Aspect was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the Aspect was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`data` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. The content of the aspect, according to its aspect type schema. The maximum size of the field is 120KB (encoded as UTF-8).  
`aspectSource` |  `object (`[AspectSource](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.AspectSource)`)` Optional. Information related to the source system of the aspect.  
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### AspectSource

JSON representation  
---  
      
    
    {
      "createTime": string,
      "updateTime": string,
      "dataVersion": string
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the aspect was created in the source system.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the aspect was last updated in the source system.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`dataVersion` |  `string` The version of the data format used to produce this data. This field is used to indicated when the underlying data format changes (e.g., schema modifications, changes to the source URL format definition, etc).  
  
### EntrySource

JSON representation  
---  
      
    
    {
      "resource": string,
      "system": string,
      "platform": string,
      "displayName": string,
      "description": string,
      "labels": {
        string: string,
        ...
      },
      "ancestors": [
        {
          object ([Ancestor](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.Ancestor))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "location": string
    }  
  
Fields  
---  
`resource` |  `string` The name of the resource in the source system. Maximum length is 4,000 characters.  
`system` |  `string` The name of the source system. Maximum length is 64 characters.  
`platform` |  `string` The platform containing the source system. Maximum length is 64 characters.  
`displayName` |  `string` A user-friendly display name. Maximum length is 500 characters.  
`description` |  `string` A description of the data resource. Maximum length is 2,000 characters.  
`labels` |  `map (key: string, value: string)` User-defined labels. The maximum size of keys and values is 128 characters each.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`ancestors[]` |  `object (`[Ancestor](https://docs.cloud.google.com/knowledge-catalog/docs/reference/mcp/tools_list/search_entries#Output.Schema.Ancestor)`)` Immutable. The entries representing the ancestors of the data resource in the source system.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the resource was created in the source system.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the resource was last updated in the source system. If the entry exists in the system and its `EntrySource` has `update_time` populated, further updates to the `EntrySource` of the entry must provide incremental updates to its `update_time`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`location` |  `string` Output only. Location of the resource in the source system. You can search the entry by this location. By default, this should match the location of the entry group containing this entry. A different value allows capturing the source location for data external to Google Cloud.  
  
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
  
### Ancestor

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string
    }  
  
Fields  
---  
`name` |  `string` Optional. The name of the ancestor resource.  
`type` |  `string` Optional. The type of the ancestor resource.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
