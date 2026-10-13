---
url: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_odb_subnets/
title: MCP Tools Reference: oracledatabase.googleapis.com \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:58.443132+00:00
---

# MCP Tools Reference: oracledatabase.googleapis.com  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_odb_subnets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  MCP Tools Reference: oracledatabase.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_odb_subnets`

List ODB Subnets in a Google Cloud project in the given location.

The following sample demonstrate how to use `curl` to invoke the `list_odb_subnets` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://oracledatabase.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_odb_subnets",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request for `OdbSubnet.List`.

### ListOdbSubnetsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string,
      "orderBy": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent value for the OdbSubnet in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}.  
`pageSize` |  `integer` Optional. The maximum number of items to return. If unspecified, at most 50 ODB Networks will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. An expression for filtering the results of the request.  
`orderBy` |  `string` Optional. An expression for ordering the results of the request.  
  
## Output Schema

The response for `OdbSubnet.List`.

### ListOdbSubnetsResponse

JSON representation  
---  
      
    
    {
      "odbSubnets": [
        {
          object ([OdbSubnet](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_odb_subnet#Output.Schema.OdbSubnet))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`odbSubnets[]` |  `object (`[OdbSubnet](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_odb_subnet#Output.Schema.OdbSubnet)`)` The list of ODB Subnets.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Unreachable locations when listing resources across all locations using wildcard location '-'.  
  
### OdbSubnet

JSON representation  
---  
      
    
    {
      "name": string,
      "cidrRange": string,
      "purpose": enum (Purpose),
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "state": enum (State)
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the OdbSubnet resource in the following format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}  
`cidrRange` |  `string` Required. The CIDR range of the subnet.  
`purpose` |  `enum (`Purpose`)` Required. Purpose of the subnet.  
`labels` |  `map (key: string, value: string)` Optional. Labels or tags associated with the resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the OdbNetwork was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`State`)` Output only. State of the ODB Subnet.  
  
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

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-17 UTC."],[],[]] 
