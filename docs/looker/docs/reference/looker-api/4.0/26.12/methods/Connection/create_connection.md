---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/Connection/create_connection/
title: Create Connection \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:12.443389+00:00
---

# Create Connection  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/Connection/create_connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Create Connection Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.12 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Create a connection using the specified configuration.

## Request

POST /connections 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[DBConnection](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/DBConnection)

Connection

Expand DBConnection definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

name

string 

Name of the connection. Also used as the unique identifier

dialect

_lock_

[Dialect](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Dialect)

(Read-only) SQL Dialect details

snippets

[Snippet](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Snippet)[] 

pdts_enabled

_lock_

boolean 

True if PDTs are enabled on this connection

named_driver_version_requested

string 

Requested JDBC driver version name

named_driver_version_actual

_lock_

string 

Resolved JDBC driver version

host

string 

Host name/address of server; or the string 'localhost' in case of a connection over an SSH tunnel.

port

string 

Port number on server. If the connection is over an SSH tunnel, then the local port associated with the SSH tunnel.

username

string 

Username for server authentication

password

string 

(Write-Only) Password for server authentication

has_password

_lock_

boolean 

Whether or not the password is present

uses_oauth

_lock_

boolean 

Whether the connection uses OAuth for authentication.

uses_key_pair_auth

boolean 

Whether the connection uses key-pair for authentication.

uses_instance_oauth

_lock_

boolean 

Whether the integration uses the oauth instance account.

uses_service_auth

_lock_

boolean 

Whether the connection uses service authentication certificate.

certificate

string 

(Write-Only) Base64 encoded Certificate body for server authentication (when appropriate for dialect).

file_type

string 

(Write-Only) Certificate keyfile type - .json, .p8 or .p12

database

string 

Database name

db_timezone

string 

Time zone of database

query_timezone

string 

Timezone to use in queries

schema

string 

Schema name

max_connections

integer 

Maximum number of concurrent connection to use

max_queries

integer 

Maximum number of concurrent queries to begin on this connection

max_queries_per_user

integer 

Maximum number of concurrent queries per user to begin on this connection

max_billing_gigabytes

string 

Maximum size of query in GBs (BigQuery only, can be a user_attribute name)

ssl

boolean 

Use SSL/TLS when connecting to server

verify_ssl

boolean 

Verify the SSL

tmp_db_name

string 

Name of temporary database (if used)

tmp_db_host

string 

Name of temporary host (if used)

jdbc_additional_params

string 

Additional params to add to JDBC connection string

pool_timeout

integer 

Connection Pool Timeout, in seconds

dialect_name

string 

(Read/Write) SQL Dialect name

supports_data_studio_link

_lock_

boolean 

Database connection has the ability to support open data studio from explore

created_at

_lock_

string 

Creation date for this connection

user_id

_lock_

string 

Id of user who last modified this connection configuration

example

_lock_

boolean 

Is this an example connection?

user_db_credentials

boolean 

(Limited access feature) Are per user db credentials enabled. Enabling will remove previously set username and password

user_attribute_fields

string[] 

maintenance_cron

string 

Cron string specifying when maintenance such as PDT trigger checks and drops should be performed

last_regen_at

_lock_

string 

Unix timestamp at start of last completed PDT trigger check process

last_reap_at

_lock_

string 

Unix timestamp at start of last completed PDT reap process

sql_runner_precache_tables

boolean 

Precache tables in the SQL Runner

sql_writing_with_info_schema

boolean 

Fetch Information Schema For SQL Writing

after_connect_statements

string 

SQL statements (semicolon separated) to issue after connecting to the database. Requires `custom_after_connect_statements` license feature

pdt_context_override

[DBConnectionOverride](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/DBConnectionOverride)

db_connection_override for this connection in the `pdt` maintenance context

managed

_lock_

boolean 

Is this connection created and managed by Looker

custom_local_port

integer 

This field is only applicable to connections over an SSH Tunnel. The value of this field would be the local port associated with the SSH tunnel if configured manually. Otherwise either enter NULL or exclude this field.

tunnel_id

string 

The Id of the ssh tunnel this connection uses

uses_tns

boolean 

Enable Transparent Network Substrate (TNS) connections

pdt_concurrency

integer 

Maximum number of threads to use to build PDTs in parallel

disable_context_comment

boolean 

When disable_context_comment is true comment will not be added to SQL

oauth_application_id

string 

An External OAuth Application to use for authenticating to the database

always_retry_failed_builds

boolean 

When true, error PDTs will be retried every regenerator cycle

uses_application_default_credentials

boolean 

Whether the connection should authenticate with the Application Default Credentials of the host environment (limited to GCP and certain dialects).

impersonated_service_account

string 

An alternative Service Account to use for querying datasets (used primarily with `uses_application_default_credentials`) (limited to GCP and certain dialects).

cost_estimate_enabled

boolean 

When true, query cost estimate will be displayed in explore.

pdt_api_control_enabled

boolean 

PDT builds on this connection can be kicked off and cancelled via API.

connection_pooling

boolean 

Enable database connection pooling.

default_bq_connection

_lock_

boolean 

When true, represents that this connection is the default BQ connection.

bq_storage_project_id

string 

The project id of the default BigQuery storage project.

bq_roles_verified

boolean 

When true, represents that all project roles have been verified.

p4sa_name

_lock_

string 

The name of P4SA service account that is associated with the Looker instance

query_holding_disabled

boolean 

Disable query holding for this connection.

service_name

string 

Service name used for connections with TNS enabled

## Response

### 200: Connection

Datatype

Description

(object)

[DBConnection](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/DBConnection)

can

_lock_

object 

Operations the current user is able to perform on this object

name

string 

Name of the connection. Also used as the unique identifier

dialect

_lock_

[Dialect](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Dialect)

(Read-only) SQL Dialect details

Expand Dialect definition... 

name

_lock_

string 

The name of the dialect

label

_lock_

string 

The human-readable label of the connection

supports_cost_estimate

_lock_

boolean 

Whether the dialect supports query cost estimates

cost_estimate_style

_lock_

string 

How the dialect handles cost estimation

persistent_table_indexes

_lock_

string 

PDT index columns

persistent_table_sortkeys

_lock_

string 

PDT sortkey columns

persistent_table_distkey

_lock_

string 

PDT distkey column

supports_streaming

_lock_

boolean 

Supports streaming results

automatically_run_sql_runner_snippets

_lock_

boolean 

Should SQL Runner snippets automatically be run

connection_tests

string[] 

supports_inducer

_lock_

boolean 

Is supported with the inducer (i.e. generate from sql)

supports_multiple_databases

_lock_

boolean 

Can multiple databases be accessed from a connection using this dialect

supports_persistent_derived_tables

_lock_

boolean 

Whether the dialect supports allowing Looker to build persistent derived tables

has_ssl_support

_lock_

boolean 

Does the database have client SSL support settable through the JDBC string explicitly?

snippets

[Snippet](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Snippet)[] 

Expand Snippet definition... 

name

_lock_

string 

Name of the snippet

label

_lock_

string 

Label of the snippet

sql

_lock_

string 

SQL text of the snippet

pdts_enabled

_lock_

boolean 

True if PDTs are enabled on this connection

named_driver_version_requested

string 

Requested JDBC driver version name

named_driver_version_actual

_lock_

string 

Resolved JDBC driver version

host

string 

Host name/address of server; or the string 'localhost' in case of a connection over an SSH tunnel.

port

string 

Port number on server. If the connection is over an SSH tunnel, then the local port associated with the SSH tunnel.

username

string 

Username for server authentication

password

string 

(Write-Only) Password for server authentication

has_password

_lock_

boolean 

Whether or not the password is present

uses_oauth

_lock_

boolean 

Whether the connection uses OAuth for authentication.

uses_key_pair_auth

boolean 

Whether the connection uses key-pair for authentication.

uses_instance_oauth

_lock_

boolean 

Whether the integration uses the oauth instance account.

uses_service_auth

_lock_

boolean 

Whether the connection uses service authentication certificate.

certificate

string 

(Write-Only) Base64 encoded Certificate body for server authentication (when appropriate for dialect).

file_type

string 

(Write-Only) Certificate keyfile type - .json, .p8 or .p12

database

string 

Database name

db_timezone

string 

Time zone of database

query_timezone

string 

Timezone to use in queries

schema

string 

Schema name

max_connections

integer 

Maximum number of concurrent connection to use

max_queries

integer 

Maximum number of concurrent queries to begin on this connection

max_queries_per_user

integer 

Maximum number of concurrent queries per user to begin on this connection

max_billing_gigabytes

string 

Maximum size of query in GBs (BigQuery only, can be a user_attribute name)

ssl

boolean 

Use SSL/TLS when connecting to server

verify_ssl

boolean 

Verify the SSL

tmp_db_name

string 

Name of temporary database (if used)

tmp_db_host

string 

Name of temporary host (if used)

jdbc_additional_params

string 

Additional params to add to JDBC connection string

pool_timeout

integer 

Connection Pool Timeout, in seconds

dialect_name

string 

(Read/Write) SQL Dialect name

supports_data_studio_link

_lock_

boolean 

Database connection has the ability to support open data studio from explore

created_at

_lock_

string 

Creation date for this connection

user_id

_lock_

string 

Id of user who last modified this connection configuration

example

_lock_

boolean 

Is this an example connection?

user_db_credentials

boolean 

(Limited access feature) Are per user db credentials enabled. Enabling will remove previously set username and password

user_attribute_fields

string[] 

maintenance_cron

string 

Cron string specifying when maintenance such as PDT trigger checks and drops should be performed

last_regen_at

_lock_

string 

Unix timestamp at start of last completed PDT trigger check process

last_reap_at

_lock_

string 

Unix timestamp at start of last completed PDT reap process

sql_runner_precache_tables

boolean 

Precache tables in the SQL Runner

sql_writing_with_info_schema

boolean 

Fetch Information Schema For SQL Writing

after_connect_statements

string 

SQL statements (semicolon separated) to issue after connecting to the database. Requires `custom_after_connect_statements` license feature

pdt_context_override

[DBConnectionOverride](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/DBConnectionOverride)

db_connection_override for this connection in the `pdt` maintenance context

Expand DBConnectionOverride definition... 

context

string 

Context in which to override (`pdt` is the only allowed value)

host

string 

Host name/address of server

pdt_host

string 

Host name/address of server (same as host)

port

string 

Port number on server

pdt_port

string 

Port number on server (same as port)

username

string 

Username for server authentication

pdt_username

string 

Username for server authentication (same as username)

password

string 

(Write-Only) Password for server authentication

pdt_password

string 

(Write-Only) Password for server authentication (same as password)

has_password

_lock_

boolean 

Whether or not the password is overridden in this context

certificate

string 

(Write-Only) Base64 encoded Certificate body for server authentication (when appropriate for dialect).

pdt_certificate

string 

(Write-Only) Base64 encoded Certificate body for server authentication (when appropriate for dialect) (same as certificate).

file_type

string 

(Write-Only) Certificate keyfile type - .json or .p12

pdt_file_type

string 

(Write-Only) Certificate keyfile type - .json or .p12 (same as file_type)

database

string 

Database name

pdt_database

string 

Database name (same as database)

schema

string 

Schema name

pdt_schema

string 

Schema name (same as schema)

jdbc_additional_params

string 

Additional params to add to JDBC connection string

pdt_jdbc_additional_params

string 

Additional params to add to JDBC connection string (same as jdbc_additional_params)

after_connect_statements

string 

SQL statements (semicolon separated) to issue after connecting to the database. Requires `custom_after_connect_statements` license feature

pdt_after_connect_statements

string 

SQL statements (semicolon separated) to issue after connecting to the database. Requires `custom_after_connect_statements` license feature (same as after_connect_statements)

pdt_service_name

string 

Service name used for connections with TNS enabled

managed

_lock_

boolean 

Is this connection created and managed by Looker

custom_local_port

integer 

This field is only applicable to connections over an SSH Tunnel. The value of this field would be the local port associated with the SSH tunnel if configured manually. Otherwise either enter NULL or exclude this field.

tunnel_id

string 

The Id of the ssh tunnel this connection uses

uses_tns

boolean 

Enable Transparent Network Substrate (TNS) connections

pdt_concurrency

integer 

Maximum number of threads to use to build PDTs in parallel

disable_context_comment

boolean 

When disable_context_comment is true comment will not be added to SQL

oauth_application_id

string 

An External OAuth Application to use for authenticating to the database

always_retry_failed_builds

boolean 

When true, error PDTs will be retried every regenerator cycle

uses_application_default_credentials

boolean 

Whether the connection should authenticate with the Application Default Credentials of the host environment (limited to GCP and certain dialects).

impersonated_service_account

string 

An alternative Service Account to use for querying datasets (used primarily with `uses_application_default_credentials`) (limited to GCP and certain dialects).

cost_estimate_enabled

boolean 

When true, query cost estimate will be displayed in explore.

pdt_api_control_enabled

boolean 

PDT builds on this connection can be kicked off and cancelled via API.

connection_pooling

boolean 

Enable database connection pooling.

default_bq_connection

_lock_

boolean 

When true, represents that this connection is the default BQ connection.

bq_storage_project_id

string 

The project id of the default BigQuery storage project.

bq_roles_verified

boolean 

When true, represents that all project roles have been verified.

p4sa_name

_lock_

string 

The name of P4SA service account that is associated with the Looker instance

query_holding_disabled

boolean 

Disable query holding for this connection.

service_name

string 

Service name used for connections with TNS enabled

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 403: Permission Denied

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 404: Not Found

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 409: Resource Already Exists

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 422: Validation Error

Datatype

Description

(object)

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ValidationError)

message

_lock_

string 

Error details

errors

[ValidationErrorDetail](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/ValidationErrorDetail)[] 

Expand ValidationErrorDetail definition... 

field

_lock_

string 

Field with error

code

_lock_

string 

Error code

message

_lock_

string 

Error info message

documentation_url

_lock_

string 

Documentation link

documentation_url

_lock_

string 

Documentation link

### 429: Too Many Requests

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

## Examples

### Python

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/create_db_connections.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/create_db_connections.py#L16 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/python/create_db_connections.py")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
