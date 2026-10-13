---
url: https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs/
title: MCP Tools Reference: datamigration \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:25.784394+00:00
---

# MCP Tools Reference: datamigration  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  MCP Tools Reference: datamigration Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_migration_jobs`

Lists the migration jobs of the provided parent with optional filters.

  * Parent parameter is in the form `projects/{project name}/locations/{location}`, for example: `projects/my-project/locations/us-central1`.
  * You can use any, some or all of the additional parameters to filter the results.
  * You can specify in the 'pageSize' parameter the maximum number of migration jobs to return. The tool may return fewer than this value. If more jobs are available, a 'nextPageToken' value is returned and you can use it in the next call to retrieve the next page of results. If unspecified, at most 50 migration jobs will be returned. The maximum value is 100; values above 100 are coerced to 100.
  * If no 'nextPageToken' is returned, there are no more migration jobs to retrieve.
  * Not all the details of the migration jobs are returned.
  * To get the full details of a specific job use the 'get_migration_job' tool.



For example: `{ create_time_after: 2025-10-02T10:15:33Z create_time_before: 2025-10-03T00:00:00Z display_name: hr running: true page_size: 80 } ` will return up to 80 migration jobs that were created on or after 2025-10-02T10:15:33 UTC and before 2025-10-03T00:00:00 UTC and have `hr` in their display name and are currently running. If there are more than 80 such jobs, a `nextPageToken` value (like `CgtteS1qb2IxM`) will be returned and you can use it in the next call to retrieve the next page of results.

The following sample demonstrate how to use `curl` to invoke the `list_migration_jobs` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://datamigration.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_migration_jobs",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request message for 'ListMigrationJobs' request.

### ListMigrationJobsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "createTimeAfter": string,
      "createTimeBefore": string,
      "displayName": string,
      "running": boolean,
      "failed": boolean,
      "completed": boolean,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The resource name for the location for which migration jobs should be returned. Must be in the format `projects/*/locations/*`. For example: 'projects/my-project/locations/us-central1'  
`createTimeAfter` |  `string` Optional. Use to get migrations jobs that were created on or after the provided date/time, formatted as RFC-3339.  
`createTimeBefore` |  `string` Optional. Use to get migrations jobs that were created before the provided date/time, formatted as RFC-3339.  
`displayName` |  `string` Optional. Use to get migration jobs whose display name contains the provided name.  
`running` |  `boolean` Optional. Use to get migration jobs that are currently running.  
`failed` |  `boolean` Optional. Use to get migration jobs that have failed.  
`completed` |  `boolean` Optional. Use to get migration jobs that are completed.  
`pageSize` |  `integer` Optional. Use to limit the number of migration jobs returned. Valid values are between 1 and 100 inclusive. Defaults to 50 if not provided or outside of the valid range. Note that due to filtering, it is possible to get no results (but a next_page_token) so you should keep calling this method until you get a response with an empty next_page_token.  
`pageToken` |  `string` Optional. A page token, received from a previous `list_migration_jobs` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `list_migration_jobs` must match the call that provided the page token.  
  
## Output Schema

Response message for 'ListMigrationJobs' request.

### ListMigrationJobsResponse

JSON representation  
---  
      
    
    {
      "migrationJobs": [
        {
          object ([MigrationJob](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.MigrationJob))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`migrationJobs[]` |  `object (`[MigrationJob](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.MigrationJob)`)` The list of migration jobs objects.  
`nextPageToken` |  `string` A token which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### MigrationJob

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.State)),
      "phase": enum ([Phase](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.Phase)),
      "type": enum ([Type](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.Type)),
      "dumpPath": string,
      "dumpFlags": {
        object ([DumpFlags](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DumpFlags))
      },
      "source": string,
      "destination": string,
      "duration": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.Status))
      },
      "sourceDatabase": {
        object ([DatabaseType](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DatabaseType))
      },
      "destinationDatabase": {
        object ([DatabaseType](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DatabaseType))
      },
      "endTime": string,
      "conversionWorkspace": {
        object ([ConversionWorkspaceInfo](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.ConversionWorkspaceInfo))
      },
      "filter": string,
      "cmekKeyName": string,
      "performanceConfig": {
        object ([PerformanceConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.PerformanceConfig))
      },
      "postgresHomogeneousConfig": {
        object ([PostgresHomogeneousConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.PostgresHomogeneousConfig))
      },
      "mysqlHomogeneousConfig": {
        object ([MySqlHomogeneousConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.MySqlHomogeneousConfig))
      },
      "sqlserverHomogeneousMigrationJobConfig": {
        object ([SqlServerHomogeneousMigrationJobConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerHomogeneousMigrationJobConfig))
      },
      "dumpType": enum ([DumpType](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DumpType)),
      "objectsConfig": {
        object ([MigrationJobObjectsConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.MigrationJobObjectsConfig))
      },
      "purpose": enum ([Purpose](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.Purpose)),
      "originalMigrationName": string,
    
      // Union field connectivity can be only one of the following:
      "reverseSshConnectivity": {
        object ([ReverseSshConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.ReverseSshConnectivity))
      },
      "vpcPeeringConnectivity": {
        object ([VpcPeeringConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.VpcPeeringConnectivity))
      },
      "staticIpConnectivity": {
        object (StaticIpConnectivity)
      }
      // End of list of possible types for union field connectivity.
    
      // Union field config can be only one of the following:
      "oracleToPostgresConfig": {
        object ([OracleToPostgresConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.OracleToPostgresConfig))
      },
      "sqlserverToPostgresConfig": {
        object ([SqlServerToPostgresConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerToPostgresConfig))
      },
      "postgresToSqlserverConfig": {
        object ([PostgresToSqlServerConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.PostgresToSqlServerConfig))
      }
      // End of list of possible types for union field config.
    
      // Union field _satisfies_pzs can be only one of the following:
      "satisfiesPzs": boolean
      // End of list of possible types for union field _satisfies_pzs.
    
      // Union field _satisfies_pzi can be only one of the following:
      "satisfiesPzi": boolean
      // End of list of possible types for union field _satisfies_pzi.
    }  
  
Fields  
---  
`name` |  `string` The name (URI) of this migration job resource, in the form of: projects/{project}/locations/{location}/migrationJobs/{migrationJob}.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the migration job resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the migration job resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` The resource labels for migration job to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`displayName` |  `string` The migration job display name.  
`state` |  `enum (`[State](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.State)`)` The current migration job state.  
`phase` |  `enum (`[Phase](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.Phase)`)` Output only. The current migration job phase.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.Type)`)` Required. The migration job type.  
`dumpPath` |  `string` The path to the dump file in Google Cloud Storage, in the format: (gs://[BUCKET_NAME]/[OBJECT_NAME]). This field and the "dump_flags" field are mutually exclusive.  
`dumpFlags` |  `object (`[DumpFlags](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DumpFlags)`)` The initial dump flags. This field and the "dump_path" field are mutually exclusive.  
`source` |  `string` Required. The resource name (URI) of the source connection profile.  
`destination` |  `string` Required. The resource name (URI) of the destination connection profile.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The duration of the migration job (in seconds). A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.Status)`)` Output only. The error details in case of state FAILED.  
`sourceDatabase` |  `object (`[DatabaseType](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DatabaseType)`)` The database engine type and provider of the source.  
`destinationDatabase` |  `object (`[DatabaseType](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DatabaseType)`)` The database engine type and provider of the destination.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. If the migration job is completed, the time when it was completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`conversionWorkspace` |  `object (`[ConversionWorkspaceInfo](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.ConversionWorkspaceInfo)`)` The conversion workspace used by the migration.  
`filter` |  `string` This field can be used to select the entities to migrate as part of the migration job. It uses AIP-160 notation to select a subset of the entities configured on the associated conversion-workspace. This field should not be set on migration-jobs that are not associated with a conversion workspace.  
`cmekKeyName` |  `string` The CMEK (customer-managed encryption key) fully qualified key name used for the migration job. This field supports all migration jobs types except for: * Mysql to Mysql (use the cmek field in the cloudsql connection profile instead). * PostrgeSQL to PostgreSQL (use the cmek field in the cloudsql connection profile instead). * PostgreSQL to AlloyDB (use the kms_key_name field in the alloydb connection profile instead). Each Cloud CMEK key has the following format: projects/[PROJECT]/locations/[REGION]/keyRings/[RING]/cryptoKeys/[KEY_NAME]  
`performanceConfig` |  `object (`[PerformanceConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.PerformanceConfig)`)` Optional. Data dump parallelism settings used by the migration.  
`postgresHomogeneousConfig` |  `object (`[PostgresHomogeneousConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.PostgresHomogeneousConfig)`)` Optional. Configuration for PostgreSQL homogeneous migration.  
`mysqlHomogeneousConfig` |  `object (`[MySqlHomogeneousConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.MySqlHomogeneousConfig)`)` Optional. Configuration for MySQL homogeneous migration.  
`sqlserverHomogeneousMigrationJobConfig` |  `object (`[SqlServerHomogeneousMigrationJobConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerHomogeneousMigrationJobConfig)`)` Optional. Configuration for SQL Server homogeneous migration.  
`dumpType` |  `enum (`[DumpType](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DumpType)`)` Optional. The type of the data dump. Supported for MySQL to CloudSQL for MySQL migrations only.  
`objectsConfig` |  `object (`[MigrationJobObjectsConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.MigrationJobObjectsConfig)`)` Optional. The objects that need to be migrated.  
`purpose` |  `enum (`[Purpose](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.Purpose)`)` Output only. Migration job mode. Migration jobs can be standard forward jobs or failback migration jobs.  
`originalMigrationName` |  `string` Optional. A failback replication pointer to the resource name (URI) of the original migration job.  
Union field `connectivity`. The connectivity method. `connectivity` can be only one of the following:  
`reverseSshConnectivity` |  `object (`[ReverseSshConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.ReverseSshConnectivity)`)` The details needed to communicate to the source over Reverse SSH tunnel connectivity.  
`vpcPeeringConnectivity` |  `object (`[VpcPeeringConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.VpcPeeringConnectivity)`)` The details of the VPC network that the source database is located in.  
`staticIpConnectivity` |  `object (`StaticIpConnectivity`)` static ip connectivity data (default, no additional details needed).  
Union field `config`. Configuration for migration. `config` can be only one of the following:  
`oracleToPostgresConfig` |  `object (`[OracleToPostgresConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.OracleToPostgresConfig)`)` Configuration for heterogeneous **Oracle to Cloud SQL for PostgreSQL** and **Oracle to AlloyDB for PostgreSQL** migrations.  
`sqlserverToPostgresConfig` |  `object (`[SqlServerToPostgresConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerToPostgresConfig)`)` Configuration for heterogeneous **SQL Server to Cloud SQL for PostgreSQL** migrations.  
`postgresToSqlserverConfig` |  `object (`[PostgresToSqlServerConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.PostgresToSqlServerConfig)`)` Configuration for heterogeneous failback migrations from **PostgreSQL to SQL Server**.  
Union field `_satisfies_pzs`.`_satisfies_pzs` can be only one of the following:  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
Union field `_satisfies_pzi`.`_satisfies_pzi` can be only one of the following:  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
  
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
  
### DumpFlags

JSON representation  
---  
      
    
    {
      "dumpFlags": [
        {
          object ([DumpFlag](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DumpFlag))
        }
      ]
    }  
  
Fields  
---  
`dumpFlags[]` |  `object (`[DumpFlag](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DumpFlag)`)` The flags for the initial dump.  
  
### DumpFlag

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` The name of the flag  
`value` |  `string` The value of the flag.  
  
### ReverseSshConnectivity

JSON representation  
---  
      
    
    {
      "vmIp": string,
      "vmPort": integer,
      "vm": string,
      "vpc": string
    }  
  
Fields  
---  
`vmIp` |  `string` Required. The IP of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel.  
`vmPort` |  `integer` Required. The forwarding port of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel.  
`vm` |  `string` The name of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel.  
`vpc` |  `string` The name of the VPC to peer with the Cloud SQL private network.  
  
### VpcPeeringConnectivity

JSON representation  
---  
      
    
    {
      "vpc": string
    }  
  
Fields  
---  
`vpc` |  `string` The name of the VPC network to peer with the Cloud SQL private network.  
  
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
  
### DatabaseType

JSON representation  
---  
      
    
    {
      "provider": enum ([DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DatabaseProvider)),
      "engine": enum ([DatabaseEngine](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DatabaseEngine))
    }  
  
Fields  
---  
`provider` |  `enum (`[DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DatabaseProvider)`)` The database provider.  
`engine` |  `enum (`[DatabaseEngine](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DatabaseEngine)`)` The database engine.  
  
### ConversionWorkspaceInfo

JSON representation  
---  
      
    
    {
      "name": string,
      "commitId": string
    }  
  
Fields  
---  
`name` |  `string` The resource name (URI) of the conversion workspace.  
`commitId` |  `string` The commit ID of the conversion workspace.  
  
### PerformanceConfig

JSON representation  
---  
      
    
    {
      "dumpParallelLevel": enum ([DumpParallelLevel](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DumpParallelLevel))
    }  
  
Fields  
---  
`dumpParallelLevel` |  `enum (`[DumpParallelLevel](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.DumpParallelLevel)`)` Initial dump parallelism level.  
  
### PostgresHomogeneousConfig

JSON representation  
---  
      
    
    {
      "isNativeLogical": boolean,
      "maxAdditionalSubscriptions": integer
    }  
  
Fields  
---  
`isNativeLogical` |  `boolean` Required. Whether the migration is native logical.  
`maxAdditionalSubscriptions` |  `integer` Optional. Maximum number of additional subscriptions to use for the migration job.  
  
### MySqlHomogeneousConfig

JSON representation  
---  
      
    
    {
      "isPrimaryDestination": boolean
    }  
  
Fields  
---  
`isPrimaryDestination` |  `boolean` Optional. Whether the destination for the migration job is a primary instance.  
  
### SqlServerHomogeneousMigrationJobConfig

JSON representation  
---  
      
    
    {
      "backupFilePattern": string,
      "databaseBackups": [
        {
          object ([SqlServerDatabaseBackup](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerDatabaseBackup))
        }
      ],
      "useDiffBackup": boolean,
      "promoteWhenReady": boolean,
      "dagConfig": {
        object ([SqlServerDagConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerDagConfig))
      }
    }  
  
Fields  
---  
`backupFilePattern` |  `string` Required. Pattern that describes the default backup naming strategy. The specified pattern should ensure lexicographical order of backups. The pattern must define one of the following capture group sets: Capture group set #1 yy/yyyy - year, 2 or 4 digits mm - month number, 1-12 dd - day of month, 1-31 hh - hour of day, 00-23 mi - minutes, 00-59 ss - seconds, 00-59 Example: For backup file TestDB_20230802_155400.trn, use pattern: (?.*)_backup_(?\d{4})(?\d{2})(?    \d{2})_(?\d{2})(?\d{2})(?\d{2}).trn Capture group set #2 timestamp - unix timestamp Example: For backup file TestDB.1691448254.trn, use pattern: (?.*).(?\d*).trn or (?.*).(?\d*).trn  
`databaseBackups[]` |  `object (`[SqlServerDatabaseBackup](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerDatabaseBackup)`)` Required. Backup details per database in Cloud Storage.  
`useDiffBackup` |  `boolean` Optional. Enable differential backups.  
`promoteWhenReady` |  `boolean` Optional. Promote databases when ready.  
`dagConfig` |  `object (`[SqlServerDagConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerDagConfig)`)` Optional. Configuration for distributed availability group (DAG) for the SQL Server homogeneous migration.  
  
### SqlServerDatabaseBackup

JSON representation  
---  
      
    
    {
      "database": string,
      "encryptionOptions": {
        object ([SqlServerEncryptionOptions](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerEncryptionOptions))
      }
    }  
  
Fields  
---  
`database` |  `string` Required. Name of a SQL Server database for which to define backup configuration.  
`encryptionOptions` |  `object (`[SqlServerEncryptionOptions](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerEncryptionOptions)`)` Optional. Encryption settings for the database. Required if provided database backups are encrypted. Encryption settings include path to certificate, path to certificate private key, and key password.  
  
### SqlServerEncryptionOptions

JSON representation  
---  
      
    
    {
      "certPath": string,
      "pvkPath": string,
      "pvkPassword": string
    }  
  
Fields  
---  
`certPath` |  `string` Required. Path to the Certificate (.cer) in Cloud Storage, in the form `gs://bucketName/fileName`. The instance must have write permissions to the bucket and read access to the file.  
`pvkPath` |  `string` Required. Path to the Certificate Private Key (.pvk) in Cloud Storage, in the form `gs://bucketName/fileName`. The instance must have write permissions to the bucket and read access to the file.  
`pvkPassword` |  `string` Required. Input only. Password that encrypts the private key.  
  
### BoolValue

JSON representation  
---  
      
    
    {
      "value": boolean
    }  
  
Fields  
---  
`value` |  `boolean` The bool value.  
  
### SqlServerDagConfig

JSON representation  
---  
      
    
    {
      "sourceAg": string,
      "linkedServer": string
    }  
  
Fields  
---  
`sourceAg` |  `string` Required. The name of the source availability group. Only used by DAG migrations.  
`linkedServer` |  `string` Required. The name of the linked server that points to the source SQL Server instance. Only used by DAG migrations.  
  
### OracleToPostgresConfig

JSON representation  
---  
      
    
    {
      "oracleSourceConfig": {
        object ([OracleSourceConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.OracleSourceConfig))
      },
      "postgresDestinationConfig": {
        object ([PostgresDestinationConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.PostgresDestinationConfig))
      }
    }  
  
Fields  
---  
`oracleSourceConfig` |  `object (`[OracleSourceConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.OracleSourceConfig)`)` Optional. Configuration for Oracle source.  
`postgresDestinationConfig` |  `object (`[PostgresDestinationConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.PostgresDestinationConfig)`)` Optional. Configuration for Postgres destination.  
  
### OracleSourceConfig

JSON representation  
---  
      
    
    {
    
      // Union field _max_concurrent_full_dump_connections can be only one of the
      // following:
      "maxConcurrentFullDumpConnections": integer
      // End of list of possible types for union field
      // _max_concurrent_full_dump_connections.
    
      // Union field _max_concurrent_cdc_connections can be only one of the
      // following:
      "maxConcurrentCdcConnections": integer
      // End of list of possible types for union field
      // _max_concurrent_cdc_connections.
    
      // Union field _skip_full_dump can be only one of the following:
      "skipFullDump": boolean
      // End of list of possible types for union field _skip_full_dump.
    
      // Union field _cdc_start_position can be only one of the following:
      "cdcStartPosition": string
      // End of list of possible types for union field _cdc_start_position.
    
      // Union field cdc_method can be only one of the following:
      "logMiner": {
        object (LogMiner)
      },
      "binaryLogParser": {
        object ([BinaryLogParser](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.BinaryLogParser))
      }
      // End of list of possible types for union field cdc_method.
    }  
  
Fields  
---  
Union field `_max_concurrent_full_dump_connections`.`_max_concurrent_full_dump_connections` can be only one of the following:  
`maxConcurrentFullDumpConnections` |  `integer` Optional. Maximum number of connections Database Migration Service will open to the source for full dump phase.  
Union field `_max_concurrent_cdc_connections`.`_max_concurrent_cdc_connections` can be only one of the following:  
`maxConcurrentCdcConnections` |  `integer` Optional. Maximum number of connections Database Migration Service will open to the source for CDC phase.  
Union field `_skip_full_dump`.`_skip_full_dump` can be only one of the following:  
`skipFullDump` |  `boolean` Optional. Whether to skip full dump or not.  
Union field `_cdc_start_position`.`_cdc_start_position` can be only one of the following:  
`cdcStartPosition` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The schema change number (SCN) to start CDC data migration from.  
Union field `cdc_method`. Configuration to select the CDC method. `cdc_method` can be only one of the following:  
`logMiner` |  `object (`LogMiner`)` Use LogMiner.  
`binaryLogParser` |  `object (`[BinaryLogParser](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.BinaryLogParser)`)` Use Binary Log Parser.  
  
### BinaryLogParser

JSON representation  
---  
      
    
    {
    
      // Union field log_file_access can be only one of the following:
      "oracleAsmLogFileAccess": {
        object (OracleAsmLogFileAccess)
      },
      "logFileDirectories": {
        object ([LogFileDirectories](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.LogFileDirectories))
      }
      // End of list of possible types for union field log_file_access.
    }  
  
Fields  
---  
Union field `log_file_access`. Configuration to specify how the log file should be accessed. `log_file_access` can be only one of the following:  
`oracleAsmLogFileAccess` |  `object (`OracleAsmLogFileAccess`)` Use Oracle ASM.  
`logFileDirectories` |  `object (`[LogFileDirectories](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.LogFileDirectories)`)` Use Oracle directories.  
  
### LogFileDirectories

JSON representation  
---  
      
    
    {
      "onlineLogDirectory": string,
      "archivedLogDirectory": string
    }  
  
Fields  
---  
`onlineLogDirectory` |  `string` Required. Oracle directory for online logs.  
`archivedLogDirectory` |  `string` Required. Oracle directory for archived logs.  
  
### PostgresDestinationConfig

JSON representation  
---  
      
    
    {
    
      // Union field _max_concurrent_connections can be only one of the following:
      "maxConcurrentConnections": integer
      // End of list of possible types for union field _max_concurrent_connections.
    
      // Union field _transaction_timeout can be only one of the following:
      "transactionTimeout": string
      // End of list of possible types for union field _transaction_timeout.
    }  
  
Fields  
---  
Union field `_max_concurrent_connections`.`_max_concurrent_connections` can be only one of the following:  
`maxConcurrentConnections` |  `integer` Optional. Maximum number of connections Database Migration Service will open to the destination for data migration.  
Union field `_transaction_timeout`.`_transaction_timeout` can be only one of the following:  
`transactionTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Timeout for data migration transactions.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### SqlServerToPostgresConfig

JSON representation  
---  
      
    
    {
      "sqlserverSourceConfig": {
        object ([SqlServerSourceConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerSourceConfig))
      },
      "postgresDestinationConfig": {
        object ([PostgresDestinationConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.PostgresDestinationConfig))
      }
    }  
  
Fields  
---  
`sqlserverSourceConfig` |  `object (`[SqlServerSourceConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerSourceConfig)`)` Optional. Configuration for SQL Server source.  
`postgresDestinationConfig` |  `object (`[PostgresDestinationConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.PostgresDestinationConfig)`)` Optional. Configuration for Postgres destination.  
  
### SqlServerSourceConfig

JSON representation  
---  
      
    
    {
    
      // Union field _max_concurrent_full_dump_connections can be only one of the
      // following:
      "maxConcurrentFullDumpConnections": integer
      // End of list of possible types for union field
      // _max_concurrent_full_dump_connections.
    
      // Union field _max_concurrent_cdc_connections can be only one of the
      // following:
      "maxConcurrentCdcConnections": integer
      // End of list of possible types for union field
      // _max_concurrent_cdc_connections.
    
      // Union field _skip_full_dump can be only one of the following:
      "skipFullDump": boolean
      // End of list of possible types for union field _skip_full_dump.
    
      // Union field _cdc_start_position can be only one of the following:
      "cdcStartPosition": string
      // End of list of possible types for union field _cdc_start_position.
    }  
  
Fields  
---  
Union field `_max_concurrent_full_dump_connections`.`_max_concurrent_full_dump_connections` can be only one of the following:  
`maxConcurrentFullDumpConnections` |  `integer` Optional. Maximum number of connections Database Migration Service will open to the source for full dump phase.  
Union field `_max_concurrent_cdc_connections`.`_max_concurrent_cdc_connections` can be only one of the following:  
`maxConcurrentCdcConnections` |  `integer` Optional. Maximum number of connections Database Migration Service will open to the source for CDC phase.  
Union field `_skip_full_dump`.`_skip_full_dump` can be only one of the following:  
`skipFullDump` |  `boolean` Optional. Whether to skip full dump or not.  
Union field `_cdc_start_position`.`_cdc_start_position` can be only one of the following:  
`cdcStartPosition` |  `string` Optional. The log sequence number (LSN) to start CDC data migration from.  
  
### PostgresToSqlServerConfig

JSON representation  
---  
      
    
    {
      "postgresSourceConfig": {
        object ([PostgresSourceConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.PostgresSourceConfig))
      },
      "sqlserverDestinationConfig": {
        object ([SqlServerDestinationConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerDestinationConfig))
      }
    }  
  
Fields  
---  
`postgresSourceConfig` |  `object (`[PostgresSourceConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.PostgresSourceConfig)`)` Optional. Configuration for PostgreSQL source.  
`sqlserverDestinationConfig` |  `object (`[SqlServerDestinationConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SqlServerDestinationConfig)`)` Optional. Configuration for SQL Server destination.  
  
### PostgresSourceConfig

JSON representation  
---  
      
    
    {
    
      // Union field _skip_full_dump can be only one of the following:
      "skipFullDump": boolean
      // End of list of possible types for union field _skip_full_dump.
    }  
  
Fields  
---  
Union field `_skip_full_dump`.`_skip_full_dump` can be only one of the following:  
`skipFullDump` |  `boolean` Optional. Whether to skip full dump or not.  
  
### SqlServerDestinationConfig

JSON representation  
---  
      
    
    {
    
      // Union field _max_concurrent_connections can be only one of the following:
      "maxConcurrentConnections": integer
      // End of list of possible types for union field _max_concurrent_connections.
    
      // Union field _transaction_timeout can be only one of the following:
      "transactionTimeout": string
      // End of list of possible types for union field _transaction_timeout.
    }  
  
Fields  
---  
Union field `_max_concurrent_connections`.`_max_concurrent_connections` can be only one of the following:  
`maxConcurrentConnections` |  `integer` Optional. Maximum number of connections Database Migration Service will open to the destination for data migration.  
Union field `_transaction_timeout`.`_transaction_timeout` can be only one of the following:  
`transactionTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Timeout for data migration transactions.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### MigrationJobObjectsConfig

JSON representation  
---  
      
    
    {
    
      // Union field migration_job_object_config can be only one of the following:
      "sourceObjectsConfig": {
        object ([SourceObjectsConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SourceObjectsConfig))
      }
      // End of list of possible types for union field migration_job_object_config.
    }  
  
Fields  
---  
Union field `migration_job_object_config`. The config for the objects to be migrated. `migration_job_object_config` can be only one of the following:  
`sourceObjectsConfig` |  `object (`[SourceObjectsConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SourceObjectsConfig)`)` The list of the migration job objects.  
  
### SourceObjectsConfig

JSON representation  
---  
      
    
    {
      "objectConfigs": [
        {
          object ([SourceObjectConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SourceObjectConfig))
        }
      ],
      "objectsSelectionType": enum ([ObjectsSelectionType](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.ObjectsSelectionType))
    }  
  
Fields  
---  
`objectConfigs[]` |  `object (`[SourceObjectConfig](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SourceObjectConfig)`)` Optional. The list of the objects to be migrated.  
`objectsSelectionType` |  `enum (`[ObjectsSelectionType](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.ObjectsSelectionType)`)` Optional. The objects selection type of the migration job.  
  
### SourceObjectConfig

JSON representation  
---  
      
    
    {
      "objectIdentifier": {
        object ([SourceObjectIdentifier](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SourceObjectIdentifier))
      }
    }  
  
Fields  
---  
`objectIdentifier` |  `object (`[SourceObjectIdentifier](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.SourceObjectIdentifier)`)` Optional. The object identifier.  
  
### SourceObjectIdentifier

JSON representation  
---  
      
    
    {
      "database": string,
      "schema": string,
      "table": string,
      "type": enum ([MigrationJobObjectType](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.MigrationJobObjectType))
    }  
  
Fields  
---  
`database` |  `string` Optional. The database name. This will be required only if the object uses a database name as part of its unique identifier.  
`schema` |  `string` Optional. The schema name. This will be required only if the object uses a schema name as part of its unique identifier.  
`table` |  `string` Optional. The table name. This will be required only if the object is a level below database or schema.  
`type` |  `enum (`[MigrationJobObjectType](https://docs.cloud.google.com/database-migration/docs/reference/mcp/tools_list/list_migration_jobs#Output.Schema.MigrationJobObjectType)`)` Required. The type of the migration job object.  
  
### State

The current migration job states.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the migration job is unknown.  
`MAINTENANCE` | The migration job is down for maintenance.  
`DRAFT` | The migration job is in draft mode and no resources are created.  
`CREATING` | The migration job is being created.  
`NOT_STARTED` | The migration job is created and not started.  
`RUNNING` | The migration job is running.  
`FAILED` | The migration job failed.  
`COMPLETED` | The migration job has been completed.  
`DELETING` | The migration job is being deleted.  
`STOPPING` | The migration job is being stopped.  
`STOPPED` | The migration job is currently stopped.  
`DELETED` | The migration job has been deleted.  
`UPDATING` | The migration job is being updated.  
`STARTING` | The migration job is starting.  
`RESTARTING` | The migration job is restarting.  
`RESUMING` | The migration job is resuming.  
  
### Phase

The current migration job phase.

Enums  
---  
`PHASE_UNSPECIFIED` | The phase of the migration job is unknown.  
`FULL_DUMP` | The migration job is in the full dump phase.  
`CDC` | The migration job is CDC phase.  
`PROMOTE_IN_PROGRESS` | The migration job is running the promote phase.  
`WAITING_FOR_SOURCE_WRITES_TO_STOP` | Only RDS flow - waiting for source writes to stop  
`PREPARING_THE_DUMP` | Only RDS flow - the sources writes stopped, waiting for dump to begin  
`READY_FOR_PROMOTE` | The migration job is ready to be promoted.  
  
### Type

The type of migration job (one-time or continuous).

Enums  
---  
`TYPE_UNSPECIFIED` | The type of the migration job is unknown.  
`ONE_TIME` | The migration job is a one time migration.  
`CONTINUOUS` | The migration job is a continuous migration.  
  
### DatabaseProvider

The database providers.

Enums  
---  
`DATABASE_PROVIDER_UNSPECIFIED` | Use this value for on-premise source database instances and ORACLE.  
`CLOUDSQL` | Cloud SQL is the source instance provider.  
`RDS` | Amazon RDS is the source instance provider.  
`AURORA` | Amazon Aurora is the source instance provider.  
`ALLOYDB` | AlloyDB for PostgreSQL is the source instance provider.  
`AZURE_DATABASE` | Microsoft Azure Database for MySQL/PostgreSQL.  
  
### DatabaseEngine

The database engine types.

Enums  
---  
`DATABASE_ENGINE_UNSPECIFIED` | The source database engine of the migration job is unknown.  
`MYSQL` | The source engine is MySQL.  
`POSTGRESQL` | The source engine is PostgreSQL.  
`SQLSERVER` | The source engine is SQL Server.  
`ORACLE` | The source engine is Oracle.  
  
### DumpParallelLevel

Describes the parallelism level during initial dump.

Enums  
---  
`DUMP_PARALLEL_LEVEL_UNSPECIFIED` | Unknown dump parallel level. Will be defaulted to OPTIMAL.  
`MIN` | Minimal parallel level.  
`OPTIMAL` | Optimal parallel level.  
`MAX` | Maximum parallel level.  
  
### DumpType

The type of the data dump.

Enums  
---  
`DUMP_TYPE_UNSPECIFIED` | If not specified, defaults to LOGICAL  
`LOGICAL` | Logical dump.  
`PHYSICAL` | Physical file-based dump. Supported for MySQL to CloudSQL for MySQL migrations only.  
  
### MigrationJobObjectType

The type of the migration job object.

Enums  
---  
`MIGRATION_JOB_OBJECT_TYPE_UNSPECIFIED` | The type of the migration job object is unknown.  
`DATABASE` | The migration job object is a database.  
`SCHEMA` | The migration job object is a schema.  
`TABLE` | The migration job object is a table.  
  
### ObjectsSelectionType

The objects selection type of the migration job.

Enums  
---  
`OBJECTS_SELECTION_TYPE_UNSPECIFIED` | The type of the objects selection is unknown, indicating that the migration job is at instance level.  
`ALL_OBJECTS` | Migrate all of the objects.  
`SPECIFIED_OBJECTS` | Migrate specific objects.  
  
### Purpose

The purpose of the migration job.

Enums  
---  
`PURPOSE_UNSPECIFIED` | Unknown purpose. Will be defaulted to MIGRATE.  
`MIGRATE` | Standard migration job.  
`FAILBACK` | Failback replication job.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
