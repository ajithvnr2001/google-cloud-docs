---
url: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_exascale_db_storage_vaults/
title: MCP Tools Reference: oracledatabase.googleapis.com \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:56.731245+00:00
---

# MCP Tools Reference: oracledatabase.googleapis.com  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_exascale_db_storage_vaults/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  MCP Tools Reference: oracledatabase.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_exascale_db_storage_vaults`

List Exascale DB Storage Vaults in a Google Cloud project in the given location.

The following sample demonstrate how to use `curl` to invoke the `list_exascale_db_storage_vaults` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://oracledatabase.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_exascale_db_storage_vaults",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request for `ExascaleDbStorageVault.List`.

### ListExascaleDbStorageVaultsRequest

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
`parent` |  `string` Required. The parent value for ExascaleDbStorageVault in the following format: projects/{project}/locations/{location}.  
`pageSize` |  `integer` Optional. The maximum number of items to return. If unspecified, at most 50 ExascaleDbStorageVaults will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. An expression for filtering the results of the request. Filter the list as specified in <https://google.aip.dev/160>.  
`orderBy` |  `string` Optional. An expression for ordering the results of the request. Order results as specified in <https://google.aip.dev/132>.  
  
## Output Schema

The response for `ExascaleDbStorageVault.List`.

### ListExascaleDbStorageVaultsResponse

JSON representation  
---  
      
    
    {
      "exascaleDbStorageVaults": [
        {
          object ([ExascaleDbStorageVault](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exascale_db_storage_vault#Output.Schema.ExascaleDbStorageVault))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`exascaleDbStorageVaults[]` |  `object (`[ExascaleDbStorageVault](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exascale_db_storage_vault#Output.Schema.ExascaleDbStorageVault)`)` The ExascaleDbStorageVaults.  
`nextPageToken` |  `string` A token identifying a page of results the server should return. If present, the next page token can be provided to a subsequent ListExascaleDbStorageVaults call to list the next page. If empty, there are no more pages.  
  
### ExascaleDbStorageVault

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "gcpOracleZone": string,
      "properties": {
        object ([ExascaleDbStorageVaultProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exascale_db_storage_vault#Output.Schema.ExascaleDbStorageVaultProperties))
      },
      "createTime": string,
      "entitlementId": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the ExascaleDbStorageVault. Format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}  
`displayName` |  `string` Required. The display name for the ExascaleDbStorageVault. The name does not have to be unique within your project. The name must be 1-255 characters long and can only contain alphanumeric characters.  
`gcpOracleZone` |  `string` Optional. The GCP Oracle zone where Oracle ExascaleDbStorageVault is hosted. Example: us-east4-b-r2. If not specified, the system will pick a zone based on availability.  
`properties` |  `object (`[ExascaleDbStorageVaultProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exascale_db_storage_vault#Output.Schema.ExascaleDbStorageVaultProperties)`)` Required. The properties of the ExascaleDbStorageVault.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time when the ExascaleDbStorageVault was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`entitlementId` |  `string` Output only. The ID of the subscription entitlement associated with the ExascaleDbStorageVault.  
`labels` |  `map (key: string, value: string)` Optional. The labels or tags associated with the ExascaleDbStorageVault.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### ExascaleDbStorageVaultProperties

JSON representation  
---  
      
    
    {
      "ocid": string,
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_cloud_vm_cluster#Input.Schema.TimeZone))
      },
      "exascaleDbStorageDetails": {
        object ([ExascaleDbStorageDetails](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exascale_db_storage_vault#Output.Schema.ExascaleDbStorageDetails))
      },
      "state": enum (State),
      "description": string,
      "vmClusterIds": [
        string
      ],
      "vmClusterCount": integer,
      "additionalFlashCachePercent": integer,
      "ociUri": string,
      "attachedShapeAttributes": [
        enum (ShapeAttribute)
      ],
      "availableShapeAttributes": [
        enum (ShapeAttribute)
      ]
    }  
  
Fields  
---  
`ocid` |  `string` Output only. The OCID for the ExascaleDbStorageVault.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_cloud_vm_cluster#Input.Schema.TimeZone)`)` Output only. The time zone of the ExascaleDbStorageVault.  
`exascaleDbStorageDetails` |  `object (`[ExascaleDbStorageDetails](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exascale_db_storage_vault#Output.Schema.ExascaleDbStorageDetails)`)` Required. The storage details of the ExascaleDbStorageVault.  
`state` |  `enum (`State`)` Output only. The state of the ExascaleDbStorageVault.  
`description` |  `string` Optional. The description of the ExascaleDbStorageVault.  
`vmClusterIds[]` |  `string` Output only. The list of VM cluster OCIDs associated with the ExascaleDbStorageVault.  
`vmClusterCount` |  `integer` Output only. The number of VM clusters associated with the ExascaleDbStorageVault.  
`additionalFlashCachePercent` |  `integer` Optional. The size of additional flash cache in percentage of high capacity database storage.  
`ociUri` |  `string` Output only. Deep link to the OCI console to view this resource.  
`attachedShapeAttributes[]` |  `enum (`ShapeAttribute`)` Output only. The shape attributes of the VM clusters attached to the ExascaleDbStorageVault.  
`availableShapeAttributes[]` |  `enum (`ShapeAttribute`)` Output only. The shape attributes available for the VM clusters to be attached to the ExascaleDbStorageVault.  
  
### TimeZone

JSON representation  
---  
      
    
    {
      "id": string,
      "version": string
    }  
  
Fields  
---  
`id` |  `string` IANA Time Zone Database time zone. For example "America/New_York".  
`version` |  `string` Optional. IANA Time Zone Database version number. For example "2019a".  
  
### ExascaleDbStorageDetails

JSON representation  
---  
      
    
    {
      "availableSizeGbs": integer,
      "totalSizeGbs": integer
    }  
  
Fields  
---  
`availableSizeGbs` |  `integer` Output only. The available storage capacity for the ExascaleDbStorageVault, in gigabytes (GB).  
`totalSizeGbs` |  `integer` Required. The total storage allocation for the ExascaleDbStorageVault, in gigabytes (GB).  
  
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
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-17 UTC."],[],[]] 
