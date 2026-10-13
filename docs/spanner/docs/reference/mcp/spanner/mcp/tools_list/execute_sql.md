---
url: https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql/
title: MCP Tools Reference: spanner.googleapis.com \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:29.124961+00:00
---

# MCP Tools Reference: spanner.googleapis.com  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  MCP Tools Reference: spanner.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `execute_sql`

Execute SQL statement using a given session.

  * execute_sql tool can be used to execute DQL as well as DML statements.
  * Prefer using parameterized queries over literal values.
  * Use commit tool to commit result of a DML statement.
  * DDL statements are only supported using update_database_schema tool.



The following sample demonstrate how to use `curl` to invoke the `execute_sql` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://spanner.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "execute_sql",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request for `ExecuteSql`.

### ExecuteSqlRequest

JSON representation  
---  
      
    
    {
      "session": string,
      "sql": string,
      "seqno": string,
      "parameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Parameter))
        }
      ],
    
      // Union field transaction can be only one of the following:
      "singleUseTransaction": boolean,
      "readOnlyTransaction": boolean,
      "readWriteTransaction": boolean,
      "existingTransactionId": string
      // End of list of possible types for union field transaction.
    }  
  
Fields  
---  
`session` |  `string` Required. The session in which the SQL query is executed. Format: `projects/{project}/instances/{instance}/databases/{database}/sessions/{session}`  
`sql` |  `string` Required. The SQL query to execute.  
`seqno` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Sequence number of the request within a transaction. The sequence number must be monotonically increasing within the transaction. If a request arrives for the first time with an out-of-order sequence number, the transaction can be aborted.  
`parameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Parameter)`)` Optional. The SQL query parameters.  
Union field `transaction`. The transaction in which the SQL query is executed. If not set, a single use transaction will be used. For DML, use read_write_transaction or specify existing_transaction_id for previously created read-write transaction when multiple statements are part of transaction. `transaction` can be only one of the following:  
`singleUseTransaction` |  `boolean` Use a single use transaction for query execution.  
`readOnlyTransaction` |  `boolean` Begin a new read-only transaction.  
`readWriteTransaction` |  `boolean` Begin a new read-write transaction.  
`existingTransactionId` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Use an existing transaction.A base64-encoded string.  
  
### Parameter

JSON representation  
---  
      
    
    {
      "name": string,
      "value": value,
      "type": {
        object ([Type](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Type))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the parameter.  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The value of the parameter. Use `string_value` for integers.  
`type` |  `object (`[Type](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Type)`)` It is not always possible for Spanner to infer the right SQL type from a JSON value. For example, values of type `BYTES` and values of type `STRING` are encoded in JSON as strings. Recommendation: set the type of the parameter.  
  
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
  
### Type

JSON representation  
---  
      
    
    {
      "code": enum (TypeCode),
      "arrayElementType": {
        object ([Type](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Type))
      },
      "structType": {
        object ([StructType](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.StructType))
      },
      "typeAnnotation": enum (TypeAnnotationCode),
      "protoTypeFqn": string
    }  
  
Fields  
---  
`code` |  `enum (`TypeCode`)` Required. The `TypeCode` for this type.  
`arrayElementType` |  `object (`[Type](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Type)`)` If `code` == `ARRAY`, then `array_element_type` is the type of the array elements.  
`structType` |  `object (`[StructType](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.StructType)`)` If `code` == `STRUCT`, then `struct_type` provides type information for the struct's fields.  
`typeAnnotation` |  `enum (`TypeAnnotationCode`)` The `TypeAnnotationCode` that disambiguates SQL type that Spanner will use to represent values of this type during query processing. This is necessary for some type codes because a single `TypeCode` can be mapped to different SQL types depending on the SQL dialect. `type_annotation` typically is not needed to process the content of a value (it doesn't affect serialization) and clients can ignore it on the read path.  
`protoTypeFqn` |  `string` If `code` == `PROTO` or `code` == `ENUM`, then `proto_type_fqn` is the fully qualified name of the proto type representing the proto/enum definition.  
  
### StructType

JSON representation  
---  
      
    
    {
      "fields": [
        {
          object ([Field](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Field))
        }
      ]
    }  
  
Fields  
---  
`fields[]` |  `object (`[Field](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Field)`)` The list of fields that make up this struct. Order is significant, because values of this struct type are represented as lists, where the order of field values matches the order of fields in the `[StructType](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.StructType)`. In turn, the order of fields matches the order of columns in a read request, or the order of fields in the `SELECT` clause of a query.  
  
### Field

JSON representation  
---  
      
    
    {
      "name": string,
      "type": {
        object ([Type](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Type))
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the field. For reads, this is the column name. For SQL queries, it is the column alias (e.g., `"Word"` in the query `"SELECT 'hello' AS Word"`), or the column name (e.g., `"ColName"` in the query `"SELECT ColName FROM Table"`). Some columns might have an empty name (e.g., `"SELECT UPPER(ColName)"`). Note that a query result can contain multiple fields with the same name.  
`type` |  `object (`[Type](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Type)`)` The type of the field.  
  
## Output Schema

Results for `execute_sql` tool

### ResultSet

JSON representation  
---  
      
    
    {
      "metadata": {
        object ([ResultSetMetadata](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Output.Schema.ResultSetMetadata))
      },
      "rows": [
        array
      ],
      "precommitToken": {
        object ([MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Output.Schema.MultiplexedSessionPrecommitToken))
      }
    }  
  
Fields  
---  
`metadata` |  `object (`[ResultSetMetadata](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Output.Schema.ResultSetMetadata)`)` Metadata about the result set, such as row type information.  
`rows[]` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Each element in `rows` is a row whose format is defined by [metadata.row_type][ResultSetMetadata.row_type]. The ith element in each row matches the ith field in [metadata.row_type][ResultSetMetadata.row_type]. Elements are encoded based on type as described `here`.  
`precommitToken` |  `object (`[MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Output.Schema.MultiplexedSessionPrecommitToken)`)` Optional. A precommit token is included if the read-write transaction is on a multiplexed session. Pass the precommit token with the highest sequence number from this transaction attempt to the `Commit` request for this transaction.  
  
### ResultSetMetadata

JSON representation  
---  
      
    
    {
      "rowType": {
        object ([StructType](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.StructType))
      },
      "transaction": {
        object ([Transaction](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Output.Schema.Transaction))
      },
      "undeclaredParameters": {
        object ([StructType](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.StructType))
      }
    }  
  
Fields  
---  
`rowType` |  `object (`[StructType](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.StructType)`)` Indicates the field names and types for the rows in the result set. For example, a SQL query like `"SELECT UserId, UserName FROM Users"` could return a `row_type` value like:
    
    
    "fields": [
      { "name": "UserId", "type": { "code": "INT64" } },
      { "name": "UserName", "type": { "code": "STRING" } },
    ]
      
  
`transaction` |  `object (`[Transaction](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Output.Schema.Transaction)`)` If the read or SQL query began a transaction as a side-effect, the information about the new transaction is yielded here.  
`undeclaredParameters` |  `object (`[StructType](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.StructType)`)` A SQL query can be parameterized. In PLAN mode, these parameters can be undeclared. This indicates the field names and types for those undeclared parameters in the SQL query. For example, a SQL query like `"SELECT * FROM Users where UserId = @userId and UserName = @userName "` could return a `undeclared_parameters` value like:
    
    
    "fields": [
      { "name": "UserId", "type": { "code": "INT64" } },
      { "name": "UserName", "type": { "code": "STRING" } },
    ]
      
  
### StructType

JSON representation  
---  
      
    
    {
      "fields": [
        {
          object ([Field](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Field))
        }
      ]
    }  
  
Fields  
---  
`fields[]` |  `object (`[Field](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Field)`)` The list of fields that make up this struct. Order is significant, because values of this struct type are represented as lists, where the order of field values matches the order of fields in the `[StructType](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.StructType)`. In turn, the order of fields matches the order of columns in a read request, or the order of fields in the `SELECT` clause of a query.  
  
### Field

JSON representation  
---  
      
    
    {
      "name": string,
      "type": {
        object ([Type](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Type))
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the field. For reads, this is the column name. For SQL queries, it is the column alias (e.g., `"Word"` in the query `"SELECT 'hello' AS Word"`), or the column name (e.g., `"ColName"` in the query `"SELECT ColName FROM Table"`). Some columns might have an empty name (e.g., `"SELECT UPPER(ColName)"`). Note that a query result can contain multiple fields with the same name.  
`type` |  `object (`[Type](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Type)`)` The type of the field.  
  
### Type

JSON representation  
---  
      
    
    {
      "code": enum (TypeCode),
      "arrayElementType": {
        object ([Type](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Type))
      },
      "structType": {
        object ([StructType](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.StructType))
      },
      "typeAnnotation": enum (TypeAnnotationCode),
      "protoTypeFqn": string
    }  
  
Fields  
---  
`code` |  `enum (`TypeCode`)` Required. The `TypeCode` for this type.  
`arrayElementType` |  `object (`[Type](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.Type)`)` If `code` == `ARRAY`, then `array_element_type` is the type of the array elements.  
`structType` |  `object (`[StructType](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Input.Schema.StructType)`)` If `code` == `STRUCT`, then `struct_type` provides type information for the struct's fields.  
`typeAnnotation` |  `enum (`TypeAnnotationCode`)` The `TypeAnnotationCode` that disambiguates SQL type that Spanner will use to represent values of this type during query processing. This is necessary for some type codes because a single `TypeCode` can be mapped to different SQL types depending on the SQL dialect. `type_annotation` typically is not needed to process the content of a value (it doesn't affect serialization) and clients can ignore it on the read path.  
`protoTypeFqn` |  `string` If `code` == `PROTO` or `code` == `ENUM`, then `proto_type_fqn` is the fully qualified name of the proto type representing the proto/enum definition.  
  
### Transaction

JSON representation  
---  
      
    
    {
      "id": string,
      "readTimestamp": string,
      "precommitToken": {
        object ([MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Output.Schema.MultiplexedSessionPrecommitToken))
      }
    }  
  
Fields  
---  
`id` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` `id` may be used to identify the transaction in subsequent `Read`, `ExecuteSql`, `Commit`, or `Rollback` calls.Single-use read-only transactions do not have IDs, because single-use transactions do not support multiple requests.A base64-encoded string.  
`readTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` For snapshot read-only transactions, the read timestamp chosen for the transaction. Not returned by default: see `TransactionOptions.ReadOnly.return_read_timestamp`.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`precommitToken` |  `object (`[MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql#Output.Schema.MultiplexedSessionPrecommitToken)`)` A precommit token is included in the response of a BeginTransaction request if the read-write transaction is on a multiplexed session and a mutation_key was specified in the `BeginTransaction`. The precommit token with the highest sequence number from this transaction attempt should be passed to the `Commit` request for this transaction.  
  
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
  
### MultiplexedSessionPrecommitToken

JSON representation  
---  
      
    
    {
      "precommitToken": string,
      "seqNum": integer
    }  
  
Fields  
---  
`precommitToken` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Opaque precommit token.A base64-encoded string.  
`seqNum` |  `integer` An incrementing seq number is generated on every precommit token that is returned. Clients should remember the precommit token with the highest sequence number from the current transaction attempt.  
  
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
  
### Tool Annotations

Destructive Hint: ✅ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
