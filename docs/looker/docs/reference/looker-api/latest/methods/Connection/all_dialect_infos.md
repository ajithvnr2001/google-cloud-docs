---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/all_dialect_infos/
title: Get All Dialect Infos \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:03.382519+00:00
---

# Get All Dialect Infos  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/all_dialect_infos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get All Dialect Infos Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.18 (latest) 

### Get information about all dialects.

## Request

GET /dialect_info 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: Dialect Info

Datatype

Description

(array)

[DialectInfo](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DialectInfo)[] 

can

_lock_

object 

Operations the current user is able to perform on this object

default_max_connections

_lock_

string 

Default number max connections

default_port

_lock_

string 

Default port number

default_max_queries

_lock_

string 

Default number max queries

default_max_queries_per_user

_lock_

string 

Default number max queries per user

installed

_lock_

boolean 

Is the supporting driver installed

label

_lock_

string 

The human-readable label of the connection

label_for_database_equivalent

_lock_

string 

What the dialect calls the equivalent of a normal SQL table

label_for_schema_equivalent

_lock_

string 

What the dialect calls the equivalent of a schema-level namespace

name

_lock_

string 

The name of the dialect

supported_driver_name

_lock_

string 

The name of the driver used for this dialect

supported_driver_versions

[DialectDriverNamesVersion](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DialectDriverNamesVersion)[] 

Expand DialectDriverNamesVersion definition... 

name

_lock_

string 

Name to be passed to the backend

display_name

_lock_

string 

Name to be displayed in the frontend.

supported_options

_lock_

[DialectInfoOptions](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DialectInfoOptions)

Option support details

Expand DialectInfoOptions definition... 

additional_params

_lock_

boolean 

Has additional params support

after_connect_statements

_lock_

boolean 

Has support for issuing statements after connecting to the database

analytical_view_dataset

_lock_

boolean 

Has analytical view support

auth

_lock_

boolean 

Has auth support

cost_estimate

_lock_

boolean 

Has configurable cost estimation

disabled

_lock_

boolean 

Disable this connection. This will prevent any queries from running on this connection.

query_holding_disabled

_lock_

boolean 

Disable query holding for this connection.

disable_context_comment

_lock_

boolean 

Can disable query context comments

host

_lock_

boolean 

Host is required

instance_name

_lock_

boolean 

Instance name is required

key_pair_authentication

_lock_

boolean 

Has support for key pair authentication

max_billing_gigabytes

_lock_

boolean 

Has max billing gigabytes support

oauth_credentials

_lock_

boolean 

Has support for a service account

pdts_for_oauth

_lock_

boolean 

Has OAuth for PDT support

port

_lock_

boolean 

Port can be specified

project_name

_lock_

boolean 

Has project name support

schema

_lock_

boolean 

Schema can be specified

service_account_credentials

_lock_

boolean 

Has support for a service account

ssl

_lock_

boolean 

Has TLS/SSL support

timezone

_lock_

boolean 

Has timezone support

tmp_table

_lock_

boolean 

Has tmp table support

tns

_lock_

boolean 

Has Oracle TNS support

username

_lock_

boolean 

Username can be specified

username_required

_lock_

boolean 

Username is required

supports_connection_pooling

_lock_

boolean 

Has support for connection pooling

user_attribute_certificate

_lock_

boolean 

Has user attribute certificate support

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 429: Too Many Requests

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

## Examples

### Kotlin

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt#L292 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt")  
---  
  
### Swift

[https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift ](https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift#L225 "https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
