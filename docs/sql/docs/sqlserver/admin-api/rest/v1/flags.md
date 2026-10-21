---
url: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/flags/
title: REST Resource: flags \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:37.028899+00:00
---

# REST Resource: flags  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/flags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  REST Resource: flags Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Flag
    * JSON representation
  * SqlFlagType
  * SqlFlagScope
  * Methods



## Resource: Flag

A flag resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([SqlFlagType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/flags#SqlFlagType)),
      "appliesTo": [
        enum ([SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/SqlDatabaseVersion))
      ],
      "allowedStringValues": [
        string
      ],
      "minValue": string,
      "maxValue": string,
      "requiresRestart": boolean,
      "kind": string,
      "inBeta": boolean,
      "allowedIntValues": [
        string
      ],
      "flagScope": enum ([SqlFlagScope](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/flags#SqlFlagScope)),
    
      // Union field recommended_value can be only one of the following:
      "recommendedStringValue": string,
      "recommendedIntValue": string
      // End of list of possible types for union field recommended_value.
    }  
  
Fields  
---  
`name` |  `string` This is the name of the flag. Flag names always use underscores, not hyphens, for example: `max_allowed_packet`  
`type` |  `enum (`[SqlFlagType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/flags#SqlFlagType)`)` The type of the flag. Flags are typed to being `BOOLEAN`, `STRING`, `INTEGER` or `NONE`. `NONE` is used for flags that do not take a value, such as `skip_grant_tables`.  
`appliesTo[]` |  `enum (`[SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/SqlDatabaseVersion)`)` The database version this flag applies to. Can be MySQL instances: `MYSQL_8_0`, `MYSQL_8_0_18`, `MYSQL_8_0_26`, `MYSQL_5_7`, or `MYSQL_5_6`. PostgreSQL instances: `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11` or `POSTGRES_12`. SQL Server instances: `SQLSERVER_2017_STANDARD`, `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`, `SQLSERVER_2019_STANDARD`, `SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`, or `SQLSERVER_2019_WEB`. See [the complete list](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/SqlDatabaseVersion).  
`allowedStringValues[]` |  `string` For `STRING` flags, a list of strings that the value can be set to.  
`minValue` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` For `INTEGER` flags, the minimum allowed value.  
`maxValue` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` For `INTEGER` flags, the maximum allowed value.  
`requiresRestart` |  `boolean` Indicates whether changing this flag will trigger a database restart. Only applicable to Second Generation instances.  
`kind` |  `string` This is always `sql#flag`.  
`inBeta` |  `boolean` Whether or not the flag is considered in beta.  
`allowedIntValues[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Use this field if only certain integers are accepted. Can be combined with minValue and maxValue to add additional values.  
`flagScope` |  `enum (`[SqlFlagScope](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/flags#SqlFlagScope)`)` Scope of flag.  
Union field `recommended_value`. Recommended flag value for UI display. `recommended_value` can be only one of the following:  
`recommendedStringValue` |  `string` Recommended string value in string format for UI display.  
`recommendedIntValue` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` Recommended int value in integer format for UI display.  
  
## SqlFlagType

Enums  
---  
`SQL_FLAG_TYPE_UNSPECIFIED` | This is an unknown flag type.  
`BOOLEAN` | Boolean type flag.  
`STRING` | String type flag.  
`INTEGER` | Integer type flag.  
`NONE` | Flag type used for a server startup option.  
`MYSQL_TIMEZONE_OFFSET` | Type introduced specially for MySQL TimeZone offset. Accept a string value with the format [-12:59, 13:00].  
`FLOAT` | Float type flag.  
`REPEATED_STRING` | Comma-separated list of the strings in a SqlFlagType enum.  
  
## SqlFlagScope

Scopes of a flag describe where the flag is used.

Enums  
---  
`SQL_FLAG_SCOPE_UNSPECIFIED` | Assume database flags if unspecified  
`SQL_FLAG_SCOPE_DATABASE` | database flags  
`SQL_FLAG_SCOPE_CONNECTION_POOL` | connection pool configuration flags  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/flags/list)`

|  Lists all available database flags for Cloud SQL instances.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
