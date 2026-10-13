---
url: https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql_readonly/
title: MCP Tools Reference: cloud-sql \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:16.479933+00:00
---

# MCP Tools Reference: cloud-sql  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql_readonly/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  MCP Tools Reference: cloud-sql Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `execute_sql_readonly`

Execute any valid read-only SQL statement on a Cloud SQL for MySQL, Cloud SQL for PostgreSQL, or Cloud SQL for SQL Server instance.

To support the `execute_sql_readonly` tool, a Cloud SQL instance and request must meet the following requirements:

  * The value of `data_api_access` must be set to `ALLOW_DATA_API`.
  * For PostgreSQL and SQL Server instances, the `database` field is required. For MySQL instances, the `database` field is optional.
  * For built-in database users (supported for MySQL, PostgreSQL, and SQL Server, and required for SQL Server because Cloud SQL for SQL Server doesn't support IAM database authentication):

    * Specify the `user` field and the `password_secret_version` field.
    * The value of `password_secret_version` must be the resource name of a regional secret version in Secret Manager stored in the same region as the Cloud SQL instance, such as `projects/12345/locations/us-central1/secrets/my-password-secret/versions/1` or `projects/12345/locations/us-central1/secrets/my-password-secret/versions/latest`.
    * The caller must have the `secretmanager.secretVersions.access` permission on the secret version.
  * For IAM database authentication (supported for MySQL and PostgreSQL only; not supported for SQL Server):

    * For a MySQL instance, the database flag `cloudsql_iam_authentication` must be set to `on`.
    * For a PostgreSQL instance, the database flag `cloudsql.iam_authentication` must be set to `on`.
    * An IAM user account or IAM service account (`CLOUD_IAM_USER` or `CLOUD_IAM_SERVICE_ACCOUNT`) is required when authenticating with IAM database authentication. The tool executes the SQL statements using the privileges of the database user logged in with IAM database authentication.
    * After you use the `create_instance` tool to create a MySQL or PostgreSQL instance, you can use the `create_user` tool to create an IAM user account for the user currently logged in to the project.



The `execute_sql_readonly` tool has the following limitations:

  * If a SQL statement returns a response larger than 10 MB, then the response will be truncated.
  * The tool has a default timeout of 30 seconds. If a query runs longer than 30 seconds, then the tool returns a `DEADLINE_EXCEEDED` error.



If you receive errors similar to "IAM authentication is not enabled for the instance" on a MySQL or PostgreSQL instance, then you can use the `get_instance` tool to check the value of the IAM database authentication flag for the instance.

If you receive errors like "The instance doesn't allow using executeSql to access this instance", then you can use the `get_instance` tool to check the `data_api_access` setting.

When you receive authentication errors for a built-in database user (including all SQL Server requests):

  1. Check if the specified database user exists on the instance using the `list_users` tool.
  2. Verify that `password_secret_version` references a valid regional Secret Manager secret version in the same region as the Cloud SQL instance and that the caller has the `secretmanager.secretVersions.access` permission on the secret version.
  3. Check if the caller has the `cloudsql.instances.executeSql` IAM permission on the project (included in roles such as Cloud SQL Instance User (`roles/cloudsql.instanceUser`) or Cloud SQL Admin (`roles/cloudsql.admin`)).



When you receive authentication errors for IAM database authentication (MySQL and PostgreSQL only):

  1. Check if the currently logged-in user account exists as an IAM user on the instance using the `list_users` tool.
  2. If the IAM user account doesn't exist, then use the `create_user` tool to create the IAM user account for the logged-in user.
  3. If the currently logged-in user doesn't have the proper database user roles, then you can use the `update_user` tool to grant database roles to the user. For example, the `cloudsqlsuperuser` role can provide an IAM user with many required permissions.
  4. Check if the currently logged-in user has the correct IAM permissions assigned for the project. You can use the `gcloud projects get-iam-policy [PROJECT_ID]` command to check if the user has the proper IAM roles or permissions assigned for the project.

     * The user must have `cloudsql.instances.login` permission to do automatic IAM database authentication.
     * The user must have `cloudsql.instances.executeSql` permission to execute SQL statements using the `execute_sql_readonly` tool or `executeSql` API.
     * Common IAM roles that contain the required permissions: Cloud SQL Instance User (`roles/cloudsql.instanceUser`) or Cloud SQL Admin (`roles/cloudsql.admin`).



When receiving an `ExecuteSqlResponse`, always check the `message` and `status` fields within the response body. A successful HTTP status code doesn't guarantee full success of all SQL statements. The `message` and `status` fields will indicate if there were any partial errors or warnings during SQL statement execution.

The following code sample shows how to use `curl` to call the `execute_sql_readonly` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://sqladmin.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "execute_sql_readonly",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Instance execute sql request for MCP.

### SqlInstancesExecuteSqlMcpRequest

JSON representation  
---  
      
    
    {
      "instance": string,
      "project": string,
      "sqlStatement": string,
      "database": string,
      "user": string,
      "passwordSecretVersion": string,
      "sqlCommenterEnabled": boolean
    }  
  
Fields  
---  
`instance` |  `string` Required. Database instance ID. This does not include the project ID.  
`project` |  `string` Required. Project ID of the project that contains the instance.  
`sqlStatement` |  `string` Required. SQL statements to run on the database. It can be a single statement or a sequence of statements separated by semicolons.  
`database` |  `string` Optional. Name of the database on which the statement will be executed. For Postgres and SQL Server it's required, for MySQL it's optional. For Postgres, if your query is not scoped to an existing database, like list databases / create new database / grant roles, you can pass in default value as `postgres` (or `master` for SQL Server).  
`user` |  `string` Optional. The name of an existing database user to connect to the database. This field is used together with the `password_secret_version` field. When not both are set, the API caller's identity is used for database authentication.  
`passwordSecretVersion` |  `string` Optional. The resource name of the Secret Manager secret holding the password for the user to log into the database. The secret should be created using the regional endpoint (for API) or from the Regional Secrets page (for UI), and stored in the same region as the Cloud SQL instance. The expected resource name format is `projects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}`. This field is used together with the `user` field. When not both are set, the API caller's identity is used for database authentication. The secret resource name will not be stored.  
`sqlCommenterEnabled` |  `boolean` Optional. If set to true, enables sqlcommenter-style tagging. Automatically collects and populates mcp.server, mcp.tool, mcp.client, and user.identity. See <https://google.github.io/sqlcommenter/> for detail about sqlcommenter.  
  
## Output Schema

### SqlInstancesExecuteSqlResponse

JSON representation  
---  
      
    
    {
      "messages": [
        {
          object ([Message](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Message))
        }
      ],
      "metadata": {
        object ([Metadata](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Metadata))
      },
      "results": [
        {
          object ([QueryResult](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.QueryResult))
        }
      ],
      "status": {
        object ([Status](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Status))
      }
    }  
  
Fields  
---  
`messages[]` |  `object (`[Message](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Message)`)` A list of notices and warnings generated during query execution. For PostgreSQL, this includes all notices and warnings. For MySQL, this includes warnings generated by the last executed statement. To retrieve all warnings for a multi-statement query, `SHOW WARNINGS` must be executed after each statement.  
`metadata` |  `object (`[Metadata](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Metadata)`)` The additional metadata information regarding the execution of the SQL statements.  
`results[]` |  `object (`[QueryResult](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.QueryResult)`)` The list of results after executing all the SQL statements.  
`status` |  `object (`[Status](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Status)`)` Contains the error from the database if the SQL execution failed.  
  
### Message

JSON representation  
---  
      
    
    {
    
      // Union field _message can be only one of the following:
      "message": string
      // End of list of possible types for union field _message.
    
      // Union field _severity can be only one of the following:
      "severity": string
      // End of list of possible types for union field _severity.
    }  
  
Fields  
---  
Union field `_message`.`_message` can be only one of the following:  
`message` |  `string` The full message string. For PostgreSQL, this is a formatted string that may include severity, code, and the notice/warning message. For MySQL, this contains the warning message.  
Union field `_severity`.`_severity` can be only one of the following:  
`severity` |  `string` The severity of the message (e.g., "NOTICE" for PostgreSQL, "WARNING" for MySQL).  
  
### Metadata

JSON representation  
---  
      
    
    {
      "sqlStatementExecutionTime": string
    }  
  
Fields  
---  
`sqlStatementExecutionTime` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The time taken to execute the SQL statements.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### QueryResult

JSON representation  
---  
      
    
    {
      "columns": [
        {
          object ([Column](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Column))
        }
      ],
      "rows": [
        {
          object ([Row](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Row))
        }
      ],
      "message": string,
      "partialResult": boolean,
      "status": {
        object ([Status](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Status))
      }
    }  
  
Fields  
---  
`columns[]` |  `object (`[Column](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Column)`)` List of columns included in the result. This also includes the data type of the column.  
`rows[]` |  `object (`[Row](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Row)`)` Rows returned by the SQL statement.  
`message` |  `string` Message related to the SQL execution result.  
`partialResult` |  `boolean` Set to true if the SQL execution's result is truncated due to size limits or an error retrieving results.  
`status` |  `object (`[Status](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Status)`)` If results were truncated due to an error, details of that error.  
  
### Column

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string
    }  
  
Fields  
---  
`name` |  `string` Name of the column.  
`type` |  `string` Datatype of the column.  
  
### Row

JSON representation  
---  
      
    
    {
      "values": [
        {
          object ([Value](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Value))
        }
      ]
    }  
  
Fields  
---  
`values[]` |  `object (`[Value](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/mysql/mcp/tools_list/execute_sql#Output.Schema.Value)`)` The values for the row.  
  
### Value

JSON representation  
---  
      
    
    {
      "value": string,
      "nullValue": boolean
    }  
  
Fields  
---  
`value` |  `string` The cell value in string format.  
`nullValue` |  `boolean` If cell value is null, then this flag will be set to true.  
  
### Status

JSON representation  
---  
      
    
    {
      "code": integer,
      "message": string,
      "details": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Any

JSON representation  
---  
      
    
    {
      "typeUrl": string,
      "value": string
    }  
  
Fields  
---  
`typeUrl` |  `string` Identifies the type of the serialized Protobuf message with a URI reference consisting of a prefix ending in a slash and the fully-qualified type name.Example: type.googleapis.com/google.protobuf.StringValueThis string must contain at least one `/` character, and the content after the last `/` must be the fully-qualified name of the type in canonical form, without a leading dot. Do not write a scheme on these URI references so that clients do not attempt to contact them.The prefix is arbitrary and Protobuf implementations are expected to simply strip off everything up to and including the last `/` to identify the type. `type.googleapis.com/` is a common default prefix that some legacy implementations require. This prefix does not indicate the origin of the type, and URIs containing it are not expected to respond to any requests.All type URL strings must be legal URI references with the additional restriction (for the text format) that the content of the reference must consist only of alphanumeric characters, percent-encoded escapes, and characters in the following set (not including the outer backticks): `/-.~_!$&()*+,;=`. Despite our allowing percent encodings, implementations should not unescape them to prevent confusion with existing parsers. For example, `type.googleapis.com%2FFoo` should be rejected.In the original design of `Any`, the possibility of launching a type resolution service at these type URLs was considered but Protobuf never implemented one and considers contacting these URLs to be problematic and a potential security issue. Do not attempt to contact type URLs.  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Holds a Protobuf serialization of the type described by type_url.A base64-encoded string.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
