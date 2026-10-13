---
url: https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_data_tables/
title: MCP Tools Reference: chronicle.googleapis.com \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:15.202110+00:00
---

# MCP Tools Reference: chronicle.googleapis.com  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/list_data_tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  MCP Tools Reference: chronicle.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_data_tables`

List data tables in Chronicle SIEM.

Retrieves a list of data tables available in the Chronicle SIEM instance. This is useful for discovering available tables, auditing their configuration, and managing security context data.

**Agent Responsibilities:**

  * Parse the JSON response to extract the list from the `dataTables` key.
  * Handle the `nextPageToken` for pagination to retrieve subsequent pages if they exist.



**Workflow Integration:**

  * Use to verify data table contents after creation or updates.
  * Essential for auditing data quality and consistency in security context tables.
  * Helps understand available data when developing or troubleshooting detection rules.
  * Supports data governance by providing visibility into managed security datasets.



**Use Cases:**

  * Review threat intelligence data before creating detection rules.
  * Verify that asset inventory data is current and accurate.
  * Audit user role mappings for consistency and completeness.
  * Troubleshoot detection rule issues by examining referenced table data.
  * Generate reports on security context data for compliance or operational reviews.



**Example Usage:**

  * `list_data_tables(projectId="my-project", customerId="my-customer", region="us", pageSize=50)`
  * `list_data_tables(projectId="my-project", customerId="my-customer", region="us")`



**Next Steps (using MCP-enabled tools):**

  * Use `list_data_table_rows` to inspect the contents of a specific table.
  * Use `create_data_table` to add new tables.
  * Use the `nextPageToken` to fetch more tables if available.
  * Add more rows using `add_rows_to_data_table` if the table needs additional data.
  * Delete specific rows using `delete_data_table_rows` if outdated or incorrect data is found.
  * Reference the table data in detection rules to enhance security monitoring.
  * Export the data for analysis or integration with other security tools.
  * Set up regular reviews to maintain data quality and relevance.



The following sample demonstrate how to use `curl` to invoke the `list_data_tables` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://chronicle.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_data_tables",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for ListDataTables.

### ListDataTablesRequest

JSON representation  
---  
      
    
    {
      "projectId": string,
      "customerId": string,
      "region": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`projectId` |  `string` Required. Google Cloud project ID.  
`customerId` |  `string` Required. Chronicle customer ID.  
`region` |  `string` Required. Chronicle region (e.g., "us", "europe").  
`pageSize` |  `integer` The maximum number of data tables to return per page. Defaults to 100, max 1000.  
`pageToken` |  `string` A page token from a previous call to fetch the next page.  
  
## Output Schema

Response message for listing data tables.

### ListDataTablesResponse

JSON representation  
---  
      
    
    {
      "dataTables": [
        {
          object ([DataTable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/create_data_table#Output.Schema.DataTable))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`dataTables[]` |  `object (`[DataTable](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/create_data_table#Output.Schema.DataTable)`)` The list of the data tables returned.  
`nextPageToken` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### DataTable

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "columnInfo": [
        {
          object ([DataTableColumnInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/create_data_table#Input.Schema.DataTableColumnInfo))
        }
      ],
      "dataTableUuid": string,
      "rules": [
        string
      ],
      "ruleAssociationsCount": integer,
      "rowTimeToLive": string,
      "approximateRowCount": string,
      "scopeInfo": {
        object ([DataTableScopeInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/create_data_table#Output.Schema.DataTableScopeInfo))
      },
      "updateSource": enum ([DataTableUpdateSource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/create_data_table#Output.Schema.DataTableUpdateSource)),
      "rowTimeToLiveUpdateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the data table Format: "{project}/locations/{location}/instances/{instance}/dataTables/{data_table}"  
`displayName` |  `string` Output only. The unique display name of the data table.  
`description` |  `string` Required. A user-provided description of the data table.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Table create timeUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Table update timeUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`columnInfo[]` |  `object (`[DataTableColumnInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/create_data_table#Input.Schema.DataTableColumnInfo)`)` Immutable. Details of all the columns in the table  
`dataTableUuid` |  `string` Output only. Data table unique id  
`rules[]` |  `string` Output only. The resource names for the associated Rules that use this data table. Format: projects/{project}/locations/{location}/instances/{instance}/rules/{rule}. {rule} here refers to the rule id.  
`ruleAssociationsCount` |  `integer` Output only. The count of rules using the data table.  
`rowTimeToLive` |  `string` Optional. User-provided TTL of the data table.  
`approximateRowCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The count of rows in the data table.  
`scopeInfo` |  `object (`[DataTableScopeInfo](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/create_data_table#Output.Schema.DataTableScopeInfo)`)` Optional. The scope info of the data table. During data table creation, if this field is not set, the data table without scopes (an unscoped table) will be created for a global user. For a scoped user, this field must be set. During data table update, if scope_info is requested to be updated, this field must be set.  
`updateSource` |  `enum (`[DataTableUpdateSource](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/create_data_table#Output.Schema.DataTableUpdateSource)`)` Output only. Source of the data table update.  
`rowTimeToLiveUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of the TTL of the data table.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
  
### DataTableColumnInfo

JSON representation  
---  
      
    
    {
      "columnIndex": integer,
      "originalColumn": string,
      "keyColumn": boolean,
      "repeatedValues": boolean,
    
      // Union field path_or_type can be only one of the following:
      "mappedColumnPath": string,
      "columnType": enum ([DataTableColumnType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/create_data_table#Input.Schema.DataTableColumnType))
      // End of list of possible types for union field path_or_type.
    }  
  
Fields  
---  
`columnIndex` |  `integer` Required. Column Index. 0,1,2...  
`originalColumn` |  `string` Required. Original column name of the Data Table (present in the CSV header in case of creation of data tables using file uploads). It must satisfy the following requirements: - Starts with letter. - Contains only letters, numbers and underscore. - Must be unique and has length < 256.  
`keyColumn` |  `boolean` Optional. Whether to include this column in the calculation of the row ID. If no columns have key_column = true, all columns will be included in the calculation of the row ID.  
`repeatedValues` |  `boolean` Optional. Whether the column is a repeated values column.  
Union field `path_or_type`.`path_or_type` can be only one of the following:  
`mappedColumnPath` |  `string` Entity proto field path that the column is mapped to  
`columnType` |  `enum (`[DataTableColumnType](https://docs.cloud.google.com/chronicle/docs/reference/mcp/tools_list/create_data_table#Input.Schema.DataTableColumnType)`)` Column type can be STRING, CIDR (Ex- 10.1.1.0/24), REGEX  
  
### DataTableScopeInfo

JSON representation  
---  
      
    
    {
      "dataAccessScopes": [
        string
      ]
    }  
  
Fields  
---  
`dataAccessScopes[]` |  `string` Required. Contains the list of scope names of the data table. If the list is empty, the data table is treated as unscoped. The scope names should be full resource names and should be of the format: "projects/{project}/locations/{location}/instances/{instance}/dataAccessScopes/{scope_name}"  
  
### DataTableColumnType

DataTableColumnType denotes the type of the column to be referenced in the rule.

Enums  
---  
`DATA_TABLE_COLUMN_TYPE_UNSPECIFIED` | The default Data Table Column Type.  
`STRING` | Denotes the type of the column as STRING.  
`REGEX` | Denotes the type of the column as REGEX.  
`CIDR` | Denotes the type of the column as CIDR.  
`NUMBER` | Denotes the type of the column as NUMBER (includes int and float).  
  
### DataTableUpdateSource

DataTableUpdateSource denotes the source that updated the data table.

Enums  
---  
`DATA_TABLE_UPDATE_SOURCE_UNSPECIFIED` | The data table is updated by the user.  
`USER` | The data table is updated by the user.  
`RULE` | The data table is updated by the rule.  
`SEARCH` | The data table is updated by the search.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-27 UTC."],[],[]] 
